import re
import pandas as pd
import streamlit as st


def markdown_table_to_df(table_text):
    lines = [line.strip() for line in table_text.split("\n") if line.strip()]

    if len(lines) < 3:
        return None

    headers = [h.strip() for h in lines[0].strip("|").split("|")]

    rows = []

    for line in lines[2:]:
        if not line.startswith("|"):
            continue

        cols = [c.strip() for c in line.strip("|").split("|")]

        # Skip malformed rows
        if len(cols) != len(headers):
            continue

        rows.append(cols)

    if not rows:
        return None

    return pd.DataFrame(rows, columns=headers)


def render_output(result, feature):

    # Normal markdown features
    if feature in [
        "Requirement Summary",
        "Generate SQL Validation",
        "Risk Analysis"
    ]:
        st.markdown(result)
        return

    # Remove markdown code fences
    result = result.replace("```markdown", "")
    result = result.replace("```", "")

    # Show report title
    title_match = re.search(r"# (.+)", result)

    if title_match:
        st.header(title_match.group(1))

    # Find every section
    section_pattern = r"##\s*(?:\d+\.\s*)?(.+?)\n(.*?)(?=\n##|\Z)"

    sections = re.findall(section_pattern, result, re.S)

    icons = {
        "Positive Test Cases": "✅",
        "Negative Test Cases": "❌",
        "Boundary Test Cases": "📏",
        "Edge Test Cases": "⚠️",
        "Regression Test Cases": "🔄",
        "API Test Cases": "🌐",
        "Test Data": "📊"
    }

    for title, content in sections:

        title = title.strip()

        st.subheader(f"{icons.get(title,'📄')} {title}")

        table_match = re.search(
            r"\|.*?\|\n\|[-| :]+\|\n(?:\|.*\|\n?)+",
            content,
            re.S
        )

        if table_match:

            df = markdown_table_to_df(table_match.group())

            if df is not None:
                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

        else:
            st.markdown(content)

        st.divider()