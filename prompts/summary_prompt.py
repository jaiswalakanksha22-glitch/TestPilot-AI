def build_summary_prompt(requirement):

    return f"""
You are a Senior Business Analyst.

Requirement:

{requirement}

Generate a professional software requirement summary.

Include these sections:

# Project Summary

## Purpose

## Actors

## Functional Requirements

## Business Rules

## Assumptions

Return clean Markdown.

Do not generate test cases.
"""