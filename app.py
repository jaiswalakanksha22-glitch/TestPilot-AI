import streamlit as st

# Configure the page
st.set_page_config(
    page_title="AI QA Copilot",
    page_icon="🤖",
    layout="wide"
)

# Main title
st.title("🤖 AI QA Copilot")

st.subheader("AI-powered Software Testing Assistant")

st.write(
    """
    Welcome!

    This application helps QA Engineers generate intelligent software test cases
    using Generative AI.
    """
)

# User Story Input
user_story = st.text_area(
    "Enter User Story",
    height=200,
    placeholder="Example: As a user, I want to log into the application using my email and password..."
)

# Generate Button
if st.button("Generate Test Cases"):
    if user_story.strip():
        st.success("Great! AI integration will be added in the next step.")
    else:
        st.warning("Please enter a user story first.")