from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_test_cases(requirement: str):

    prompt = f"""
You are an experienced QA Engineer.

Generate professional software test cases.

Requirement:

{requirement}

Return the output in the following sections:

1. Positive Test Cases
2. Negative Test Cases
3. Boundary Test Cases
4. Edge Test Cases

Use a table with:

- Test Case ID
- Test Scenario
- Expected Result
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert Software QA Engineer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content