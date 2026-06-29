# Restaurant Tips Analysis & High Tip Prediction

## Project Overview

This is a functional beginner-friendly data science project built in Google Colab.

The project loads a restaurant tips dataset from a GitHub raw CSV file, analyzes tipping behavior, creates visualizations, and trains a simple machine learning model to classify high-tip records.

## Data Source

The notebook loads the dataset directly from GitHub:

```python
DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(DATA_URL)
```

If the GitHub CSV cannot be loaded, the notebook creates a fallback dataset so the project can still run from start to finish.

## Tools Used

- Python
- pandas
- NumPy
- Matplotlib
- scikit-learn
- Google Colab

## Main Steps

1. Install dependencies
2. Set up helper functions
3. Load dataset from GitHub
4. Review data quality
5. Clean the dataset
6. Create analytical features
7. Build KPI summary
8. Create grouped analysis tables
9. Generate visualizations
10. Classify high-tip records using NumPy
11. Train a Random Forest model
12. Validate the project
13. Export results
14. Print final insights

## Features Created

- `tip_percentage`
- `bill_per_person`
- `tip_per_person`
- `high_tip`

## Machine Learning Task

The model predicts whether a restaurant bill is a high-tip record.

A high-tip record is defined as a record where `tip_percentage` is greater than or equal to the 75th percentile.

## How to Run

Open the notebook in Google Colab and run:

```text
Runtime > Restart runtime and run all
```

At the end, the notebook should print:

```text
Project validation passed.
```

## Portfolio Summary

**Restaurant Tips Analysis & High Tip Prediction**  
Built a functional data science project using Python, pandas, NumPy, Matplotlib, and scikit-learn. Loaded a restaurant tips dataset from GitHub, cleaned and transformed the data, created tip percentage metrics, visualized tipping behavior, classified high-tip records using NumPy, trained a Random Forest model, validated the workflow, and exported results.

## Possible Improvements

- Add a Power BI dashboard
- Add SQL analysis
- Compare multiple machine learning models
- Create a Streamlit dashboard
- Add more explanatory markdown for each result
