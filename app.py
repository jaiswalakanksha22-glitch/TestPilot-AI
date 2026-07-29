import streamlit as st
from services.ai_service import generate_test_cases

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI QA Copilot",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("⚙️ Settings")

    model = st.selectbox(
        "Select AI Model",
        [
            "GPT-4.1",
            "GPT-4.1-mini"
        ]
    )

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
st.title("🤖 AI QA Copilot")

st.write(
    """
Generate intelligent software test cases using Artificial Intelligence.
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

    if user_story.strip() == "":
        st.warning("Please enter a requirement.")

    else:

        with st.spinner("Generating AI Test Cases..."):

            result = generate_test_cases(user_story)

        st.success("Done!")

        st.markdown(result)