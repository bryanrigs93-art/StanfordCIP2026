# AgentIAHub Simulator

https://codeinplace.stanford.edu/cip6/share/zNop9IMl04UcxtGAy1il

AgentIAHub Simulator is a learning project that simulates a corporate AI Agent Hub.

The project shows how a manager can coordinate specialized task-oriented assistants for different business areas. It combines Python logic, terminal interaction, a visual dashboard, session reports, and optional AI-assisted recommendations.

## Project Purpose

The main purpose of this project is to demonstrate how an AI Agent Manager can coordinate specialized business agents.

Instead of using one generic chatbot, AgentIAHub delegates work to assistants with specific roles. Each assistant receives inputs, processes the information with Python, and produces a manager-ready recommendation.

This is a learning simulation. It does not replace real legal, financial, payroll, HR, operations, cybersecurity, or management decisions.

## System Architecture

AgentIAHub works in three layers:

### 1. Interface Layer

- Interactive terminal menu
- Visual dashboard with `graphics.Canvas`
- Screens that show workflow progress and final reports

### 2. Control Layer

- Python functions route the user to the correct assistant
- CSV files provide employee and business data
- Calculations are handled with deterministic Python logic
- Reports are saved during the session

### 3. Cognitive Layer

- Structured prompts are used when GPT support is available
- The project attempts to use `from ai import call_gpt`
- If GPT is not available, the app uses rule-based fallback recommendations

## Specialized Agents

| Agent | Inputs | Python Processing | Recommendation Role |
|---|---|---|---|
| HR Assistant | Salary, tenure, vacation days, exit reason | Calculates estimated payout | Suggests handover, retention, and policy review actions |
| Payroll Assistant | Salary, bonus, deductions, overtime, attendance | Calculates gross pay, net pay, and exception flags | Suggests approval checks before payroll decisions |
| Team Lead KPI Assistant | AHT, QA, CSAT, adherence, attendance | Calculates KPI score and bonus eligibility | Generates coaching or recognition recommendations |
| Sales Assistant | Sales, target, commission rate | Calculates achievement, commission, and target gap | Suggests coaching or sales follow-up actions |
| Finance Assistant | Budget and actual spending | Calculates budget variance and percentage difference | Suggests cost control or reallocation actions |
| Operations Assistant | Ticket title, hours open, affected customers | Classifies priority level | Suggests escalation and follow-up actions |
| IT/Security Assistant | Alert indicators and business impact signals | Applies safe defensive classification logic | Suggests documentation, review, and escalation actions |

## Human-in-the-Loop Workflow

The system follows this pattern:

```text
Human Manager
    -> Central Hub
    -> Specialized Assistant
    -> Python Logic and Business Rules
    -> GPT Recommendation or Fallback Recommendation
    -> Visual and Terminal Report
    -> Human Manager Final Review
```

The system does not make final decisions. It provides decision support for a human manager.

## AI Agent Simulation vs. Traditional Automation

### AI Agent Simulation

These elements simulate AI agent behavior:

- Specialized roles
- Context-aware recommendations
- Optional GPT-assisted reasoning
- Workflow progress visualization
- Human-in-the-loop review
- Business-oriented reporting

### Traditional Automation

These elements are traditional software automation:

- Fixed menu options
- Input validation
- CSV reading
- Mathematical formulas
- Rule-based thresholds
- Dashboard rendering

The project intentionally combines both. This reflects how real business AI systems often work: AI recommendations are supported by deterministic software, business rules, and human governance.

## Key Features

- Interactive terminal menu
- Visual dashboard
- Multiple business assistants
- Employee data loading from CSV
- Session report history
- GPT-assisted recommendations when available
- Rule-based fallback when GPT is unavailable
- Human-review disclaimer
- Manager-friendly reports

## Example Use Cases

### HR Exit Review

The HR Assistant calculates an estimated payout and suggests a careful manager review action.

### Payroll Review

The Payroll Assistant calculates pay values and highlights possible exceptions that require approval.

### KPI Coaching

The KPI Assistant reviews performance metrics and prepares either recognition or coaching guidance.

### Sales Review

The Sales Assistant checks target achievement and estimates commission.

### Finance Review

The Finance Assistant compares approved budget against actual spending and explains the variance.

### Operations Review

The Operations Assistant classifies ticket priority based on time open and customer impact.

### IT/Security Review

The IT/Security Assistant provides a safe defensive learning simulation for reviewing alerts and deciding when human escalation is needed.

## Governance Principles

This project reflects core AI Agent Manager ideas:

- Clear agent roles
- Defined scope
- Human review required
- Business metrics matter
- Fallback logic improves reliability
- Final decisions remain with humans
- Recommendations should be reviewed before action

## Future Improvements

Possible improvements include:

1. Add local memory with SQLite.
2. Save reports permanently.
3. Add a natural language interface.
4. Let the Hub route requests automatically based on user intent.
5. Add audit logs for each assistant action.
6. Improve the dashboard with charts and trend analysis.
7. Add more realistic governance settings such as autonomy levels, approval thresholds, and escalation rules.

## Suggested Folder Structure

```text
Workshop/
└── AgentIAHub-Simulator/
    ├── README.md
    ├── main.py
    ├── employees_smart_company.csv
    └── assets/
        └── architecture.png
```

## How to Run

1. Open the project in the Stanford / Code in Place environment or clone the repository.
2. Make sure the Python file and CSV file are in the same folder.
3. Run the main Python file.
4. Choose an assistant from the terminal menu.
5. Review the report in the terminal and dashboard.

## Requirements

- Python 3
- `csv`
- `random`
- `graphics.Canvas`
- Optional Stanford / Code in Place AI helper: `from ai import call_gpt`

## Disclaimer

This project is a learning simulation. The recommendations may vary depending on company policy, local laws, business context, and available data. A human manager should always review the final decision.

## Author

Created by Bryan Bodegas as a workshop project to demonstrate how Python, visual interfaces, business logic, and AI-assisted recommendations can work together in a simulated AI Agent Hub.

## One-Sentence Summary

AgentIAHub Simulator is a Python learning project that demonstrates how specialized AI-style business assistants can support managers through calculations, workflow automation, and contextual recommendations while keeping humans in control.
