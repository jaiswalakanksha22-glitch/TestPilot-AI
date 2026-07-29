def generate_test_cases(requirement):
    """
    Temporary implementation to verify that the UI works.
    """

    return f"""
# Generated Test Cases

## Positive Test Cases

| Test Case ID | Scenario | Expected Result |
|---------------|-----------------------------|----------------|
| TC001 | Verify requirement | User should be able to complete the action successfully |

## Negative Test Cases

| Test Case ID | Scenario | Expected Result |
|---------------|-----------------------------|----------------|
| TC002 | Invalid input | Proper validation message displayed |

---

Requirement received:

{requirement}
"""