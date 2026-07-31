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

/* Main background */
.stApp{
    background-color:#FFFFFF;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#F7F8FA;
}

/* Buttons */
.stButton>button{
    background:#2563EB;
    color:white;
    border-radius:8px;
    border:none;
    height:45px;
    font-weight:600;
}

.stButton>button:hover{
    background:#1D4ED8;
}

/* Text Area */
textarea{
    border-radius:8px !important;
}

/* Metric Cards */
[data-testid="stMetric"]{
    background:#F8FAFC;
    border:1px solid #E5E7EB;
    padding:15px;
    border-radius:10px;
}

/* Tabs */
button[data-baseweb="tab"]{
    font-size:16px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

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
# Enterprise Section Header
# -----------------------------
def section_header(title, color="#2563EB"):
    st.markdown(
        f"""
<div style="
background:#F8FAFC;
border-left:6px solid {color};
padding:10px 14px;
border-radius:8px;
font-size:18px;
font-weight:600;
margin-top:8px;
margin-bottom:12px;
">
{title}
</div>
""",
        unsafe_allow_html=True,
    )
# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("TestPilot AI")

    st.caption(
    "Enterprise AI Assistant for Software Testing"
    )

    st.markdown("""
    AI-Powered QA Assistant

    Generate high-quality software testing artifacts from natural language requirements.

    Feature

    ✅ Test Cases

    ✅ Requirement Summary

    ✅ SQL Validation

    ✅ API Test Cases

    ✅ Test Data Generator

    """)
    st.markdown("---")

    section_header("🚀 AI Features", "#2563EB")
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
    
    section_header("📂 Sample Requirements", "#0F766E")

    sample = st.selectbox(
        "Choose Sample Requirement",
        ["None"] + list(SAMPLES.keys())
    )
    st.markdown("---")
    
    sample_text = ""

    if sample != "None":
        sample_text = load_sample(sample)
    
    if sample != "None":
        st.markdown(f"""
    <div style="
    background:#E8F1FD;
    padding:12px;
    border-left:5px solid #2563EB;
    border-radius:8px;
    margin-bottom:10px;
    ">
    <b>📄 Sample Requirement Loaded</b><br>
    {sample}
    </div>
    """, unsafe_allow_html=True)

    
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
#Removing space above the heading
st.markdown("""
<style>

/* Remove Streamlit top padding */
.block-container{
    padding-top:0rem;
    padding-bottom:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* Remove extra top spacing */
div[data-testid="stAppViewContainer"]{
    padding-top:0rem;
}

/* Optional: remove space above first element */
.main .block-container{
    margin-top:0rem;
}

</style>
""", unsafe_allow_html=True)

#adding coloured bar and heading
st.markdown("""
<div style="
background:linear-gradient(90deg,#1E3A8A,#2563EB);
padding:28px 40px;
margin:-1rem -2rem 30px -2rem;
border-radius:0px;
color:white;
display:flex;
justify-content:space-between;
align-items:center;
">

<div>
<h1 style="
margin:0;
font-size:42px;
font-weight:700;
color:white;
">
🤖 TestPilot AI
</h1>

<p style="
margin:6px 0 0 0;
font-size:18px;
color:#DBEAFE;
">
Enterprise AI Assistant for Software Testing
</p>
</div>

<div style="text-align:right;">
<div style="font-size:14px;color:#BFDBFE;">Powered by</div>
<div style="font-size:24px;font-weight:bold;">Qwen 2.5</div>
</div>

</div>
""", unsafe_allow_html=True)

#The app details tab

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

    st.metric("Available Features", len(features))

with col2:
    st.metric("LLM AI Model", "Qwen 2.5")

with col3:
    st.metric("Current Version", "1.0")

section_header("📝 Requirement Input", "#7C3AED")

st.caption(
    "Describe your software requirement below and let TestPilot AI generate professional QA artifacts."
)

label = "📝 Requirement / User Story"

if sample != "None":
    label = "📝 Sample Requirement (Editable)"

user_story = st.text_area(
    label,
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

st.markdown("<br>", unsafe_allow_html=True)

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
                    section_header(f"📄 {section_title}", "#059669")
                    render_output(result, feature)

                with tab2:
                    st.markdown("### Project Information")

                    st.markdown(f"""
                    **Feature**

                    {feature}

                    **AI Model**

                    Qwen 2.5-7B-Instruct

                    **Developer**

                    Akanksha Jaiswal

                    **Framework**

                    Python • Streamlit • Hugging Face
                    """)

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