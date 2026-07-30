def build_prompt(requirement: str):

    return f"""
You are a Senior Software QA Engineer with over 15 years of experience in testing enterprise applications.

Based on the requirement below, generate comprehensive software test cases.

Requirement:
{requirement}

Generate:

1. Positive Test Cases
2. Negative Test Cases
3. Boundary Test Cases
4. Edge Test Cases

For every test case provide:

- Test Case ID
- Test Scenario
- Preconditions
- Test Steps
- Expected Result
- Priority (High/Medium/Low)

Return everything in clean Markdown tables.

Be concise but professional.
"""