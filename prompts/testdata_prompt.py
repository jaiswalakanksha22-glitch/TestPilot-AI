def build_testdata_prompt(requirement):

    return f"""
You are a Senior Software QA Engineer.

Requirement:
{requirement}

Generate software testing data.

Return ALL of the following sections.

## Valid Test Data

Create a Markdown table with 10 rows containing:

| First Name | Last Name | Email | Phone | Password |

---

## Boundary Test Data

Include a Markdown table containing:

- Minimum valid values
- Maximum valid values
- Empty values

---

## Invalid Test Data

Create a Markdown table containing at least 10 invalid records.

Include examples of:

- Invalid email format
- Empty email
- Invalid phone number
- Phone containing letters
- Empty phone
- Weak password
- Password shorter than minimum length
- SQL Injection input
- XSS input
- Special characters only

This section is MANDATORY.

Return ONLY Markdown.
"""