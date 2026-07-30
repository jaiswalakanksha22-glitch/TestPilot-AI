import streamlit as st
import traceback
from services.llm_service import (
    generate_test_cases,
    summarize_requirement,
    generate_sql_queries,
    generate_test_data,
    generate_api_test_cases
)
from utils.export_excel import export_to_excel
from utils.render_output import render_output
from utils.sample_loader import (
    load_sample,
    SAMPLES
)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="TestPilot AI",
    page_icon="🤖",
    layout="wide"
)
st.markdown("""
<style>
[data-testid="stMetricValue"] {
    font-size: 0.8rem;
}

[data-testid="stMetricLabel"] {
    font-size: 1.4rem;
}
</style>
""", unsafe_allow_html=True)
# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🚀 TestPilot AI")

    st.caption("AI-Powered Software Testing Assistant")

    st.markdown("""
    Welcome to **TestPilot AI**.

    Generate high-quality software testing artifacts from natural language requirements.

    Current Features

    ✅ Test Cases

    ✅ Requirement Summary

    ✅ SQL Validation

    ✅ API Test Cases

    ✅ Test Data Generator

    Coming Soon

    📄 Requirement Upload

    📊 Dashboard

    📑 PDF Export
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

    st.subheader("📂 Sample Requirements")

    sample = st.selectbox(
        "Choose Sample Requirement",
        ["None"] + list(SAMPLES.keys())
    )
    st.markdown("---")
    
    sample_text = ""

    if sample != "None":
        sample_text = load_sample(sample)

    if sample != "None":
        st.success(f"✅ {sample} loaded")

        with st.expander("Preview Requirement"):
            preview = sample_text

            if len(preview) > 350:
                preview = preview[:350] + "..."

            st.text(preview)

    st.caption("TestPilot AI v1.0")

    st.caption("Built with")

    st.markdown("""
    - Python
    - Streamlit
    - Hugging Face
    - OpenPyXL
    """)

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
col1, col2, col3 = st.columns(3)

with col1:
    features = [
    "Generate Test Cases",
    "Generate API Test Cases",
    "Generate SQL Validation",
    "Generate Test Data",
    "Requirement Summary",
    "Risk Analysis"
    ]

    st.metric("AI Features", len(features))

with col2:
    st.metric("LLM", "Qwen 2.5")

with col3:
    st.metric("Version", "1.0")

st.markdown(
    "Describe your software requirement below and let TestPilot AI generate professional QA artifacts."
)


user_story = st.text_area(
    "📝 Requirement / User Story",
    value=sample_text,
    height=220,
    placeholder="""Example:

As a registered user,
I should be able to log in using my email and password
so that I can access my dashboard.
"""
)

button_labels = {
    "Generate Test Cases": "🚀 Generate Test Cases",
    "Requirement Summary": "📄 Generate Summary",
    "Generate SQL Validation": "🗄 Generate SQL",
    "Generate Test Data": "📊 Generate Test Data",
    "Generate API Test Cases": "🌐 Generate API Tests",
    "Risk Analysis": "⚠️ Analyze Risks"
}

col1, col2 = st.columns(2)

with col1:
    generate = st.button(
        button_labels[feature],
        use_container_width=True
    )

with col2:
    clear = st.button(
        "🗑 Clear",
        use_container_width=True
    )

if clear:
    st.rerun()

if generate:

    if not user_story.strip():
        st.warning("Please enter a requirement.")

    else:
        messages = {
            "Generate Test Cases": (
                "🤖 AI is generating professional test cases...",
                "✅ Test Cases Generated Successfully",
                "Generated Test Cases"
            ),
            "Requirement Summary": (
                "📄 AI is analyzing the requirement...",
                "✅ Requirement Summary Generated",
                "Requirement Summary"
            ),
            "Generate SQL Validation": (
                "🗄 AI is generating SQL validation queries...",
                "✅ SQL Validation Generated",
                "SQL Validation Queries"
            ),
            "Generate Test Data": (
                "📊 AI is generating test data...",
                "✅ Test Data Generated",
                "Generated Test Data"
            ),
            "Generate API Test Cases": (
                "🌐 AI is generating API test cases...",
                "✅ API Test Cases Generated",
                "API Test Cases"
            ),
            "Risk Analysis": (
                "⚠️ AI is analyzing project risks...",
                "✅ Risk Analysis Generated",
                "Risk Analysis"
            )
        }

        spinner_msg, success_msg, section_title = messages[feature]
        with st.spinner(spinner_msg):

            try:

                if feature == "Generate Test Cases":
                    result = generate_test_cases(user_story)

                elif feature == "Requirement Summary":
                    result = summarize_requirement(user_story)
                
                elif feature == "Generate SQL Validation":
                    result = generate_sql_queries(user_story)
                
                elif feature == "Generate Test Data":
                    result = generate_test_data(user_story)
                
                elif feature == "Generate API Test Cases":
                    result = generate_api_test_cases(user_story)

                else:
                    result = "🚧 This feature is coming soon."

                st.success(success_msg)

                st.divider()

                tab1, tab2 = st.tabs(["📄 AI Output", "ℹ️ About"])

                with tab1:
                    st.subheader(section_title)
                    render_output(result, feature)

                with tab2:
                    st.write("### Feature")
                    st.info(feature)

                    st.write("### AI Model")
                    st.success("Qwen 2.5-7B-Instruct")

                    st.write("### Generated By")
                    st.write("TestPilot AI")

                    st.write("### Generated On")
                    from datetime import datetime
                    st.caption(datetime.now().strftime("%d %b %Y | %I:%M %p"))

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
                st.exception(e)
                traceback.print_exc()
        
st.markdown("---")

st.caption(
    "© 2026 TestPilot AI | Built by Akanksha Jaiswal | Powered by Hugging Face"
)