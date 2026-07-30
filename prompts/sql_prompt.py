def build_sql_prompt(requirement):

    return f"""
You are a Senior QA Automation Engineer.

Requirement:

{requirement}

Generate SQL validation queries for backend verification.

Return:

# SQL Validation Queries

Generate:

1. Record existence query
2. Count validation query
3. Data integrity validation
4. Status validation
5. Timestamp validation

Then generate a section called:

# Validation Checklist

Use Markdown formatting.
"""