def build_api_prompt(requirement):

    return f"""
You are a Senior QA Automation Engineer and REST API Testing Expert.

Requirement:
{requirement}

Generate COMPLETE REST API test cases.

IMPORTANT RULES:

1. Generate ALL of the following sections.
2. NEVER skip any section.
3. Every section must contain AT LEAST 5 test cases.
4. If a section is not applicable, create realistic generic test cases instead of omitting it.
5. Return ONLY Markdown.
6. Do NOT include explanations.
7. Use proper Markdown tables.

---------------------------------------------------------

## Positive API Tests

| Test Case ID | Scenario | Request | Expected Status Code | Expected Response | Priority |

(Generate minimum 5)

---------------------------------------------------------

## Negative API Tests

| Test Case ID | Scenario | Request | Expected Status Code | Expected Response | Priority |

(Generate minimum 5)

---------------------------------------------------------

## Authentication Tests

| Test Case ID | Scenario | Request | Expected Status Code | Expected Response | Priority |

(Generate minimum 5)

---------------------------------------------------------

## Authorization Tests

| Test Case ID | Scenario | Request | Expected Status Code | Expected Response | Priority |

(Generate minimum 5)

---------------------------------------------------------

## Status Code Validation

| Test Case ID | Scenario | Request | Expected Status Code | Expected Response | Priority |

(Generate minimum 5)

---------------------------------------------------------

## Request Validation

| Test Case ID | Scenario | Request | Expected Status Code | Expected Response | Priority |

(Generate minimum 5)

---------------------------------------------------------

## Response Validation

| Test Case ID | Scenario | Request | Expected Status Code | Expected Response | Priority |

(Generate minimum 5)

---------------------------------------------------------

## Performance Checks

| Test Case ID | Scenario | Request | Expected Status Code | Expected Response | Priority |

(Generate minimum 5)

Return Markdown only.
"""