def build_api_prompt(requirement):

    return f"""
You are a Senior API Test Engineer.

Requirement:

{requirement}

Generate professional REST API test cases.

Return the following sections:

# Positive API Tests

# Negative API Tests

# Authentication Tests

# Authorization Tests

# Status Code Validation

# Request Validation

# Response Validation

# Performance Checks

Use Markdown tables.

Each test case must include:

- Test Case ID
- Scenario
- Request
- Expected Status Code
- Expected Response
- Priority

Return Markdown only.
"""