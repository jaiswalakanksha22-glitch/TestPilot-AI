import streamlit as st
from services.llm_service import generate_test_cases
from utils.export_excel import export_to_excel

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="TestPilot AI",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🚀 TestPilot AI")

    st.caption("AI-Powered Software Testing Assistant")

    st.markdown("""
    Welcome to **TestPilot AI**.

    Generate high-quality software testing artifacts from natural language requirements.

    ### Current Features
    - ✅ Functional Test Cases
    - ✅ Positive Test Cases
    - ✅ Negative Test Cases
    - ✅ Boundary Test Cases
    - ✅ Edge Test Cases

    ### Coming Soon
    - 📄 PDF Requirement Upload
    - 🌐 API Test Case Generation
    - 🗄 SQL Validation Queries
    - 📊 Test Data Generator
    """)
    st.markdown("---")

    feature = st.selectbox(
        "Choose AI Feature",
        [
            "Generate Test Cases",
            "Generate API Test Cases",
            "Generate SQL Validation",
            "Generate Test Data",
            "Requirement Summary",
            "Risk Analysis"
        ]
    )

    st.markdown("---")

    st.success("Version 1.0")

    test_type = st.multiselect(
        "Test Types",
        [
            "Positive",
            "Negative",
            "Boundary",
            "Edge",
            "Regression"
        ],
        default=[
            "Positive",
            "Negative",
            "Boundary",
            "Edge"
        ]
    )

    st.info("Version 1.0")

# -----------------------------
# Main Screen
# -----------------------------
st.title("🤖 TestPilot AI")

st.write(
    """
Generate intelligent software test cases, API test scenarios,
SQL validation queries, test data, and requirement summaries
using Large Language Models.
"""
)

user_story = st.text_area(
    "Enter Requirement / User Story",
    height=220,
    placeholder="""Example:

As a registered user,
I should be able to log in using my email and password
so that I can access my dashboard.
"""
)

generate = st.button("🚀 Generate Test Cases")

if generate:

    if not user_story.strip():
        st.warning("Please enter a requirement.")

    else:

        with st.spinner("🤖 AI is generating professional test cases..."):

            try:

                result = generate_test_cases(user_story)

                st.success("✅ Test Cases Generated Successfully")

                st.divider()

                st.subheader("Generated Test Cases")

                st.markdown(result)

                # Export to Excel
                file = export_to_excel(result)

                with open(file, "rb") as f:
                    st.download_button(
                    label="📥 Download Excel",
                    data=f,
                    file_name="TestCases.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            except Exception as e:

                st.error(str(e))
        