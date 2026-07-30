import os
print("✅ Using Hugging Face LLM Service")
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from prompts.testcase_prompt import build_prompt


load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

MODEL = "Qwen/Qwen2.5-7B-Instruct"

def ask_llm(system_role, prompt):

    messages = [
        {
            "role": "system",
            "content": system_role
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=1200,
        temperature=0.3
    )

    return response.choices[0].message.content


def generate_test_cases(requirement):

    prompt = build_prompt(requirement)

    return ask_llm(
        "You are a Senior Software QA Engineer.",
        prompt
    )

from prompts.summary_prompt import build_summary_prompt


def summarize_requirement(requirement):

    prompt = build_summary_prompt(requirement)

    return ask_llm(
        "You are a Senior Business Analyst.",
        prompt
    )

from prompts.sql_prompt import build_sql_prompt


def generate_sql_queries(requirement):

    prompt = build_sql_prompt(requirement)

    return ask_llm(
        "You are a Senior Software QA Engineer.",
        prompt
    )

from prompts.testdata_prompt import build_testdata_prompt


def generate_test_data(requirement):

    prompt = build_testdata_prompt(requirement)

    return ask_llm(
        "You are a Senior Software QA Engineer.",
        prompt
    )

from prompts.api_prompt import build_api_prompt

def generate_api_test_cases(requirement):

    prompt = build_api_prompt(requirement)

    return ask_llm(
        "You are a Senior API QA Engineer.",
        prompt
    )