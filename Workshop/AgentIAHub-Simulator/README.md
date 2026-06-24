# AgentIAHub Simulator

https://codeinplace.stanford.edu/cip6/share/zNop9IMl04UcxtGAy1il

AgentIAHub Simulator is a Python learning project that simulates a corporate AI Agent Hub for managers. It combines a terminal menu, a visual dashboard built with `graphics.Canvas`, CSV-based employee data, business calculations, workflow screens, optional GPT recommendations, and rule-based fallback logic.

The current code includes HR, Payroll, Team Lead KPI, Sales, and IT/Security assistant flows. The system is designed as a human-in-the-loop simulation: the program generates reports and recommendations, but a human manager must review the final decision.

## Project Purpose

The goal of this project is to demonstrate how a manager could coordinate specialized AI-style agents inside a company. Instead of one generic chatbot, the system routes work to task-specific assistants that analyze a business case, apply Python logic, and produce a manager-ready recommendation.

This project is educational. It does not replace real HR, payroll, finance, sales, operations, cybersecurity, legal, or management decisions.

## Main Menu

The program starts with a terminal menu called **SMART COMPANY AI HUB**:

```text
1. HR Assistant
2. Payroll Assistant
3. Team Lead KPI Assistant
4. Sales Assistant
5. IT/Security Assistant
6. View All Reports
7. Exit
```

The dashboard is visual, but the user selects actions through the terminal. Each option opens a specialized workflow and saves a summary to the session report history.

## System Architecture

AgentIAHub works in three layers:

### 1. Interface Layer

- Interactive terminal menu
- Visual dashboard using `graphics.Canvas`
- Department cards for HR, Payroll, KPI, Sales, and IT/Security
- Progress screens that show automated steps
- Final report screens with calculated values and recommendations

### 2. Control Layer

- Python functions route the user to the correct assistant
- The program loads employee records from `employees_smart_company.csv`
- Deterministic Python calculations are used for pay, KPI, sales, and classifications
- Logical thresholds classify results and generate fallback guidance
- Reports are stored in `session_reports` during the current run

### 3. Cognitive Layer

- The function `get_ai_recommendation()` tries to use `from ai import call_gpt`
- If GPT is available, the system sends a structured business prompt
- If GPT is not available, the system returns a rule-based fallback recommendation
- This makes the app usable even when AI support is not enabled in the environment

## Specialized Assistants

| Assistant | Main Inputs | Python Processing | Recommendation Output |
|---|---|---|---|
| HR Assistant | Employee, exit reason, salary, tenure, vacation days | Calculates estimated payout and exit-related values | Suggests handover, retention, policy, or final review actions |
| Payroll Assistant | Salary, bonus, deductions, overtime, attendance | Calculates gross pay, net pay, annual net, and review flags | Suggests payroll approval checks |
| Team Lead KPI Assistant | AHT, QA, CSAT, attendance, schedule adherence | Normalizes metrics, calculates composite KPI score, and bonus eligibility | Generates recognition or coaching guidance |
| Sales Assistant | Monthly sales, target, commission rate | Calculates achievement percentage, commission, and target gap | Suggests sales coaching or follow-up actions |
| IT/Security Assistant | Alert indicators, email indicators, log data, user decisions | Applies safe defensive classification and learning simulations | Suggests documentation, review, and escalation actions |

## Important Code Components

### User Input Helpers

The code includes reusable functions for clean input handling:

- `get_menu_choice()` validates the main menu choice
- `get_positive_float()` accepts numbers greater than zero
- `get_non_negative_float()` accepts zero or positive numbers
- `get_non_negative_int()` accepts whole numbers
- `get_yes_no()` converts yes/no answers to boolean values
- `get_required_text()` prevents empty text inputs

These functions make the app easier to use and reduce invalid data errors.

### Data Loading

The function `load_employee_database()` reads employee data from:

```text
employees_smart_company.csv
```

The assistant workflows use this CSV data to select employees and calculate reports.

### Workflow Visualization

The function `run_agent_step()` simulates an agent workflow by showing one automated task at a time. It displays:

- The assistant name
- The task name
- Step number and total steps
- A short explanation
- A progress bar
- A pause so the manager can follow the process

This makes the project feel like an AI agent workflow instead of a simple calculator.

### AI Recommendation Logic

The function `get_ai_recommendation(context, fallback_message)` is the central AI-style reasoning function.

It tries to call GPT using:

```python
from ai import call_gpt
```

If the call works, the model generates a short professional recommendation. If it fails, the program safely continues with the fallback recommendation. This is useful for Code in Place or workshop environments where GPT support may differ.

### Report System

The program stores session summaries using:

- `add_report()`
- `view_reports()`
- `draw_reports_screen()`

Option 6 in the main menu lets the user review all reports created during the current session.

## Human-in-the-Loop Pattern

The system follows this workflow:

```text
Human Manager
    -> Terminal Menu
    -> Visual Hub
    -> Specialized Assistant
    -> Python Calculation and Classification
    -> GPT Recommendation or Rule-Based Fallback
    -> Dashboard Report and Terminal Report
    -> Human Manager Final Review
```

The program does not make final real-world decisions. It only supports the manager.

## AI Agent Simulation vs. Traditional Automation

### AI Agent Simulation Elements

- Specialized assistant roles
- Context-aware recommendations
- Optional GPT-assisted reasoning
- Workflow progress screens
- Business-focused reports
- Human review before final action

### Traditional Automation Elements

- Fixed terminal menus
- CSV loading
- Input validation
- Mathematical formulas
- Rule-based thresholds
- Dashboard drawing functions

The project intentionally combines both because many real business AI systems use deterministic logic plus AI-generated explanations.

## Example Workflows

### HR Exit Review

The HR workflow loads or receives employee information, calculates estimated payout values, and generates a manager-style recommendation. It includes a disclaimer reminding the user that company policy and local law must be reviewed.

### Payroll Review

The Payroll workflow calculates gross pay, deductions, net pay, and annual net pay. It flags simulated payroll exceptions such as high overtime, high deductions, or low attendance.

### Team Lead KPI Review

The KPI workflow analyzes AHT, QA, CSAT, attendance, and schedule adherence. It calculates a composite KPI score, determines bonus eligibility, and prepares either recognition or focused coaching.

### Sales Review

The Sales workflow calculates target achievement and commission. It classifies whether the employee achieved the target, is close to target, or needs follow-up.

### IT/Security Learning Module

The IT/Security workflow is a defensive training simulation. It includes alert review, phishing/social-engineering indicator review, SOC training cases, and log parsing for SIEM-style preparation. Everything is simulated and intended for safe learning only.

## Safety and Governance Principles

This project follows several governance ideas:

- Human review is required
- Each assistant has a clear role
- The program explains that recommendations are simulated
- Business rules remain visible in Python
- GPT is optional, not required
- Fallback logic prevents the app from breaking
- Reports are decision support, not automatic approval
- Security-related content is defensive and educational only

## Requirements

- Python 3
- `csv`
- `random`
- `graphics.Canvas`
- `employees_smart_company.csv`
- Optional: Stanford / Code in Place AI helper with `from ai import call_gpt`

## Suggested Folder Structure

```text
Workshop/
└── AgentIAHub-Simulator/
    ├── README.md
    ├── main.py
    └── employees_smart_company.csv
```

## How to Run

1. Open the project in the Stanford / Code in Place environment.
2. Make sure `main.py` and `employees_smart_company.csv` are in the same folder.
3. Run the Python file.
4. Choose an assistant from the terminal menu.
5. Follow the questions in the terminal.
6. Review the dashboard report and terminal report.
7. Use option 6 to view session reports.

## Future Improvements

Possible improvements include:

1. Save reports to a file or database.
2. Add clickable dashboard cards.
3. Add charts and trend visualizations.
4. Add login or manager roles.
5. Add permanent memory with SQLite.
6. Add natural language routing instead of fixed menus.
7. Add audit logs for every recommendation.
8. Add more realistic governance settings such as autonomy level, approval thresholds, and escalation rules.

## Disclaimer

This is a learning simulation. Results and recommendations may vary depending on company policy, country law, business context, and data quality. A human manager should always review the final decision.

The IT/Security assistant is only for safe defensive learning and simulated analysis. It should not be used as a real security response system.

## Author

Created by Bryan Bodegas as a Stanford / Code in Place workshop project to demonstrate how Python, visual interfaces, business logic, and AI-assisted recommendations can work together in a simulated AI Agent Hub.

## One-Sentence Summary

AgentIAHub Simulator is a Python learning project that demonstrates how specialized AI-style business assistants can support managers through calculations, workflow automation, dashboard reports, and contextual recommendations while keeping humans in control.
