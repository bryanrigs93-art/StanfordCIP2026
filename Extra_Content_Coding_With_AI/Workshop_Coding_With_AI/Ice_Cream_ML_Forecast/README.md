# Ice Cream Sales Forecast

## Overview

This extra project explores a beginner-friendly machine learning workflow using Python.

The goal is to predict estimated ice cream sales using a small CSV dataset with store, weather, price, promotion, and previous sales information.

## Important Note

This is a learning demo, not a real business forecasting model.

The dataset is small, so the model result should be interpreted carefully. The main purpose is to understand the workflow, not to create a production-ready prediction system.

## Main Concepts

- CSV data
- Pandas
- Feature selection
- Linear Regression
- Train/test split
- Mean Absolute Error
- R2 Score
- Simple prediction
- Business forecasting idea

## Files

- `ice_cream_forecast.py` — Python script that trains and tests the model.
- `ice_cream_sales_dataset.csv` — Small sample dataset used by the program.

## What the Program Does

1. Loads the CSV file.
2. Chooses input features such as temperature, weekend, price, promotion, rain, and humidity.
3. Uses sales as the target value.
4. Splits the data into training and testing sets.
5. Trains a Linear Regression model.
6. Prints model metrics.
7. Predicts estimated sales for a new day scenario.

## Takeaway

This project helped me understand that machine learning starts with data. Before a model can make predictions, Python needs to load the dataset, choose useful columns, train the model, test the result, and interpret the output.
