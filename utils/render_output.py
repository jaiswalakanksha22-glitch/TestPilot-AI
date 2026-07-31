import re
import pandas as pd
import streamlit as st


def markdown_table_to_df(table_text):
    """Convert a markdown table into a dataframe."""

    lines = [line.strip() for line in table_text.split("\n") if line.strip()]

    if len(lines) < 3:
        return None

    headers = [h.strip() for h in lines[0].strip("|").split("|")]

    rows = []

    for line in lines[2:]:

        if not line.startswith("|"):
            continue

        cols = [c.strip() for c in line.strip("|").split("|")]

        if len(cols) == len(headers):
            rows.append(cols)

    if not rows:
        return None

    return pd.DataFrame(rows, columns=headers)


def render_output(result, feature):

    # Plain markdown outputs
    if feature in [
        "Requirement Summary",
        "Generate SQL Validation",
        "Risk Analysis"
    ]:
        st.markdown(result)
        return

    # Remove markdown fences
    result = result.replace("```markdown", "")
    result = result.replace("```", "")

    # Overall report title
    report = re.search(r"#\s+(.+)", result)

    if report:
        st.markdown(f"## 📄 {report.group(1)}")

    # Split using every ## heading
    sections = re.split(r"(?=^#{1,2}\s)", result, flags=re.MULTILINE)

    icons = {
        "Positive Test Cases": "✅",
        "Negative Test Cases": "❌",
        "Boundary Test Cases": "📏",
        "Edge Test Cases": "⚠️",
        "Regression Test Cases": "🔄",
        "Positive API Tests": "✅",
        "Negative API Tests": "❌",
        "Boundary API Tests": "📏",
        "Edge API Tests": "⚠️",
        "API Test Cases": "🌐",
        "Generated Test Data": "📊",
        "Test Data": "📊"
    }

    for section in sections:

        if not section.strip():
            continue

        lines = section.strip().split("\n")

        title = re.sub(r"^#{1,2}\s*", "", lines[0]).strip()

        # Remove numbering such as "1. Positive Test Cases"
        title = re.sub(r"^\d+\.\s*", "", title)

        st.subheader(f"{icons.get(title,'📄')} {title}")

        table_match = re.search(
            r"(\|.+\|\n\|[-:| ]+\|\n(?:\|.*\|\n?)*)",
            section
        )

        if table_match:

            df = markdown_table_to_df(table_match.group(1))

            if df is not None:
                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

        else:
            body = "\n".join(lines[1:])
            st.markdown(body)

        st.divider()