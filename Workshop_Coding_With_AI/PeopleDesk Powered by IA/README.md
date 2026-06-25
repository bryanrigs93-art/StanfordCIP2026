# PeopleDesk Powered by IA

> Learning simulation — under active review. Not intended for production use.

**PeopleDesk Powered by IA** is a Python desktop-style learning app that simulates AI-assisted HR, payroll, and team performance workflows using employee data from a CSV file.

Project link: https://codeinplace.stanford.edu/cip6/share/zNop9IMl04UcxtGAy1il

Built as a final project for Stanford's Code in Place 2025.

## What it does

PeopleDesk helps a manager review simulated employee cases through three guided assistants:

- **HR Assistant** — estimates exit payouts for layoff, resignation, or mutual agreement cases.
- **Payroll Assistant** — reviews gross pay, net pay, deductions, overtime, attendance, and payroll exceptions.
- **Team Lead KPI Assistant** — evaluates performance metrics and generates coaching briefs.

Each module runs rule-based calculations in Python and attempts an AI-style recommendation via GPT when available, falling back to structured logic otherwise.

## Stack

- Python 3
- `graphics.py` / `graphics.Canvas` from the Code in Place environment
- `csv` from the Python standard library
- `pathlib.Path` for file path handling
- Optional: `ai.call_gpt` from the Code in Place GPT helper

## Main menu

```text
PeopleDesk Powered by AI
=================================
1. HR Assistant
2. Payroll Assistant
3. Team Lead KPI Assistant
4. View All Reports
5. Exit
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

## Assistant details

### HR Assistant

The HR Assistant loads an employee from the CSV file and asks for the exit reason: layoff, resignation, or mutual agreement.

It calculates daily salary, severance when applicable, unused vacation payout, and estimated total payout. It also generates a cautious manager-style recommendation based on the exit context.

### Payroll Assistant

The Payroll Assistant loads salary, bonus, deductions, overtime, and attendance data from the CSV file.

It calculates gross pay, net pay, estimated annual net pay, and review flags. It can flag simulated exceptions such as overtime requiring validation, deductions above the review threshold, or attendance below the expected level.

### Team Lead KPI Assistant

The KPI Assistant reviews performance metrics such as AHT, QA, CSAT, schedule adherence, and attendance rate.

It calculates a composite KPI score and determines whether the employee should receive recognition or focused coaching.

## AI recommendation design

The function `get_ai_recommendation()` attempts to call GPT using:

```python
from ai import call_gpt
```

The prompt asks for a short professional recommendation based only on the case context.

If the GPT helper is not available, the program continues working by using a fallback message created from business rules. This makes the project more reliable in different Code in Place environments.

## How to run

```bash
python main.py
```

Requires `employees_smart_company.csv` in the same folder.

## Status

Active learning project. Logic, UI, and recommendations are being revised.

Current focus areas:

- Improve the dashboard experience
- Make reports clearer
- Reduce user friction in the terminal flow
- Strengthen the explanation of human-in-the-loop review
- Improve the README and project documentation

## Future improvements

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

PeopleDesk Powered by IA is a Python learning project that simulates how AI-assisted assistants can support HR, payroll, and team performance decisions while keeping the human manager in control.
