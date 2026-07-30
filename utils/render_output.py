import re
import pandas as pd
import streamlit as st


def render_output(result: str, feature: str):

    # Features that don't contain tables
    if feature in [
        "Requirement Summary",
        "Generate SQL Validation",
        "Risk Analysis"
    ]:
        st.markdown(result)
        return

    # Remove markdown fences
    result = re.sub(r"```[\w]*", "", result)
    result = result.replace("```", "")

    # Find every markdown table
    tables = re.findall(
        r"((?:#+.*?\n)?\|.+?\|\n\|[-:| ]+\|\n(?:\|.*?\|\n?)*)",
        result,
        flags=re.DOTALL
    )

    if not tables:
        st.markdown(result)
        return

    icons = {
        "Positive": "✅",
        "Negative": "❌",
        "Boundary": "📏",
        "Edge": "⚠️",
        "Regression": "🔄",
        "API": "🌐",
        "Test Data": "📊"
    }

    for table in tables:

        lines = table.strip().split("\n")

        title = "Generated Output"

        # Detect heading before the table
        if lines[0].startswith("#"):
            title = lines[0].replace("#", "").strip()
            table_lines = lines[1:]
        else:
            table_lines = lines

        icon = "📄"

        for key in icons:
            if key.lower() in title.lower():
                icon = icons[key]
                break

        st.subheader(f"{icon} {title}")

        headers = [
            h.strip()
            for h in table_lines[0].strip("|").split("|")
        ]

        rows = []

        for row in table_lines[2:]:

            cols = [
                c.strip()
                for c in row.strip("|").split("|")
            ]

            if len(cols) == len(headers):
                rows.append(cols)

        df = pd.DataFrame(rows, columns=headers)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()