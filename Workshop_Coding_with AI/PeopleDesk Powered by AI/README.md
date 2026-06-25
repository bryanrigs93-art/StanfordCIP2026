# PeopleDesk Powered by AI

> Learning simulation — under active review. Not intended for production use.

**PeopleDesk Powered by AI** is a Python desktop-style learning app that simulates AI-assisted HR, payroll, and team performance workflows using employee data from a CSV file.

Project link: https://codeinplace.stanford.edu/cip6/share/zNop9IMl04UcxtGAy1il

Built as a final project for Stanford's Code in Place 2025.

## What it does

PeopleDesk helps a manager review simulated employee cases through three guided assistants:

- **HR Assistant** — estimates exit payouts for layoff, resignation, or mutual agreement cases.
- **Payroll Assistant** — reviews gross pay, net pay, deductions, overtime, attendance, and payroll exceptions.
- **Team Lead KPI Assistant** — evaluates performance metrics and generates recognition or coaching briefs.

Each module runs rule-based calculations in Python and attempts to generate an AI-style recommendation through GPT when available. If GPT is not available, the app safely falls back to structured rule-based logic.

## Main Features

- Interactive terminal menu
- Visual dashboard using `graphics.Canvas`
- Employee data loaded from `employees_smart_company.csv`
- HR payout calculations
- Payroll exception review
- KPI scorecard and coaching recommendations
- Session report history
- GPT recommendation support when available
- Rule-based fallback when GPT is unavailable
- Human-in-the-loop disclaimer on the dashboard

## Main Menu

```text
PeopleDesk Powered by AI
=================================
1. HR Assistant
2. Payroll Assistant
3. Team Lead KPI Assistant
4. View All Reports
5. Exit
```

## Stack

- Python 3
- `graphics.py` / `graphics.Canvas` from the Code in Place environment
- `csv` from the Python standard library
- `pathlib.Path` for file path handling
- Optional: `ai.call_gpt` from the Code in Place GPT helper

## Project Structure

```text
PeopleDesk Powered by AI/
├── main.py
├── employees_smart_company.csv
└── README.md
```

## How it works

The application follows a human-in-the-loop workflow:

```text
Human Manager
    -> Terminal Menu
    -> Visual Dashboard
    -> Selected Assistant
    -> Python Calculation / Classification
    -> GPT Recommendation or Rule-Based Fallback
    -> Final Report
    -> Human Manager Review
```

The system does not make final decisions. It produces simulated reports and recommendations that a human manager must review.

## Assistant Details

### HR Assistant

The HR Assistant loads an employee from the CSV file and asks for the exit reason:

- Layoff
- Resignation
- Mutual agreement

It calculates:

- Daily salary
- Severance when applicable
- Unused vacation payout
- Estimated total payout

It also generates a cautious manager-style recommendation based on the exit context.

### Payroll Assistant

The Payroll Assistant loads salary, bonus, deductions, overtime, and attendance data from the CSV file.

It calculates:

- Gross pay
- Net pay
- Estimated annual net pay
- Payroll review flags

It flags simulated exceptions such as:

- Overtime requiring manager validation
- Deductions above the review threshold
- Attendance below the expected level

### Team Lead KPI Assistant

The KPI Assistant reviews performance metrics such as:

- Average Handle Time (AHT)
- Quality Assurance score (QA)
- Customer Satisfaction score (CSAT)
- Schedule adherence
- Attendance rate

It calculates a composite KPI score and determines whether the employee should receive recognition or focused coaching.

## AI Recommendation Design

The function `get_ai_recommendation()` attempts to call GPT using:

```python
from ai import call_gpt
```

The prompt asks for a short professional recommendation based only on the case context.

If the GPT helper is not available, the program continues working by using a fallback message created from business rules. This makes the project more reliable in different Code in Place environments.

## Why this is an AI-assisted simulation

This project is not a fully autonomous AI system. It is an AI-assisted workflow simulation.

It simulates AI agent behavior through:

- Specialized assistant roles
- Structured inputs
- Business calculations
- Contextual recommendations
- Workflow steps
- Human review

At the same time, it also uses traditional programming:

- Menu options
- CSV data loading
- Input validation
- Mathematical formulas
- Rule-based thresholds
- Dashboard drawing functions

This combination is realistic because many business AI tools combine deterministic logic with AI-generated explanations.

## How to run

```bash
python main.py
```

Make sure this file is in the same folder:

```text
employees_smart_company.csv
```

## Requirements

- Python 3
- Code in Place graphics environment
- `employees_smart_company.csv` in the same folder as `main.py`
- Optional GPT helper support for AI recommendations

## Status

Active learning project. Logic, UI, and recommendations are being revised.

Current focus areas:

- Improve the dashboard experience
- Make reports clearer
- Reduce user friction in the terminal flow
- Strengthen the explanation of human-in-the-loop review
- Improve the README and project documentation

## Future Improvements

Possible future improvements:

- Make dashboard cards clickable
- Save reports to a file
- Add charts for KPI and payroll trends
- Add manager login
- Add dashboard metrics
- Add more sample employee records
- Improve prompt engineering for recommendations
- Add clearer troubleshooting messages when the CSV file is missing

## Disclaimer

This project is a learning simulation. All recommendations are illustrative.

A human manager must review any decision involving real employees, company policy, payroll, performance, or local labor law.

This app should not be used for production HR decisions.

## Author

Created by **Bryan Bodegas** as a Stanford Code in Place project.

## One-sentence summary

PeopleDesk Powered by AI is a Python learning project that simulates how AI-assisted assistants can support HR, payroll, and team performance decisions while keeping the human manager in control.
