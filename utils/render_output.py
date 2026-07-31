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

        if len(cols) == len(headers):
            rows.append(cols)

    if not rows:
        return None

    return pd.DataFrame(rows, columns=headers)


def render_output(result, feature):

    if feature in [
        "Requirement Summary",
        "Generate SQL Validation",
        "Risk Analysis"
    ]:
        st.markdown(result)
        return

    result = result.replace("```markdown", "")
    result = result.replace("```", "")

    title = re.search(r"#\s+(.+)", result)

    if title:
        st.header(title.group(1))

    # Accept headings with or without numbering
    section_pattern = r"##\s*(?:\d+\.\s*)?(.+?)\n(.*?)(?=\n##|\Z)"

    sections = re.findall(section_pattern, result, flags=re.S)

    if not sections:
        sections = [("Results", result)]

    icons = {

        "Positive Test Cases":"✅",
        "Negative Test Cases":"❌",
        "Boundary Test Cases":"📏",
        "Edge Test Cases":"⚠️",
        "Regression Test Cases":"🔄",

        "Positive API Tests":"🌐✅",
        "Negative API Tests":"🌐❌",
        "Boundary API Tests":"🌐📏",
        "Edge API Tests":"🌐⚠️",

        "API Test Cases":"🌐",
        "Test Data":"📊"

    }

    for heading, content in sections:

        heading = heading.strip()

        st.subheader(f"{icons.get(heading,'📄')} {heading}")

        tables = re.findall(
            r"\|.*?\|\n\|[-:| ]+\|\n(?:\|.*\|\n?)+",
            content,
            flags=re.S
        )

        if tables:

            for table in tables:

                df = markdown_table_to_df(table)

                if df is not None:
                    st.dataframe(
                        df,
                        use_container_width=True,
                        hide_index=True
                    )

        else:
            st.markdown(content)

        st.divider()