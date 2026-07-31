# 🤖 TestPilot AI

## Overview

TestPilot AI is an AI-powered software testing assistant that helps QA engineers, testers, and students generate professional QA artifacts from natural language software requirements using Large Language Models (LLMs).

The application automates repetitive QA documentation and improves productivity by generating comprehensive testing outputs in seconds.

---

## Features

### ✅ Test Case Generation
- Positive Test Cases
- Negative Test Cases
- Boundary Test Cases
- Edge Test Cases

### 📄 Requirement Summary
Generate structured requirement summaries including:
- Project Summary
- Purpose
- Actors
- Functional Requirements
- Business Rules
- Assumptions

### 🗄 SQL Validation
Generate SQL validation queries for backend and database testing.

### 🌐 API Test Cases
Generate API test scenarios including positive, negative, and validation cases.

### 📊 Test Data Generator
Generate realistic positive, negative, boundary, and invalid test data.

### 📂 Sample Requirements
Includes sample business requirements for:
- User Login
- User Registration
- Payment
- Appointment Booking
- API Login

### 📥 Export
- Export generated outputs to Excel (.xlsx)

---

## Tech Stack

- Python
- Streamlit
- Hugging Face Inference API
- Qwen 2.5-7B-Instruct
- Pandas
- OpenPyXL
- Git
- GitHub

---

## Project Structure

```
TestPilot-AI/
│
├── app.py
├── prompts/
├── services/
├── utils/
├── sample_requirements/
├── screenshots/
├── exports/
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/jaiswalakanksha22-glitch/TestPilot-AI.git
```

Navigate to the project

```bash
cd TestPilot-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
HF_TOKEN=your_huggingface_token
```

Run the application

```bash
streamlit run app.py
```

---

## Screenshots

### Home Page

<img width="2734" height="1572" alt="home_page" src="https://github.com/user-attachments/assets/85401dd0-df79-4a9b-a56c-aa58a68218a2" />



---

## Future Enhancements

- Requirement document upload (PDF/DOCX)
- PDF report export
- Dashboard & Analytics
- AI-generated Test Plans
- Requirement Traceability Matrix (RTM)
- Defect Report Generator

---

## Author

**Akanksha Jaiswal**

MS in Artificial Intelligence | QA Engineer | AI Enthusiast

---

## Version

**Version 1.0**
