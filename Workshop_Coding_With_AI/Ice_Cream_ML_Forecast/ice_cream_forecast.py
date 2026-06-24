"""
Program: Ice Cream Sales Forecast

This is an extra Coding With AI practice project.
It shows the basic machine learning workflow with a small CSV dataset.

Important note:
This is a learning demo, not a real business forecasting model.
The dataset is small, so the results should be interpreted carefully.
"""

# Code in Place IDE demo:
# Open this link and click Run to execute the program in the CIP IDE.
# https://codeinplace.stanford.edu/cip6/share/7DVtnaNolUE73DDVcFnK

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


# 1. Load the dataset
data = pd.read_csv("ice_cream_sales_dataset.csv")

# 2. Choose the input columns and the target column
features = [
    "Temperature",
    "isWeekend",
    "isHoliday",
    "PreviousDaySales",
    "Price",
    "Promotion",
    "Rain_mm",
    "Humidity"
]

X = data[features]
y = data["Sales"]

# 3. Split the data into training data and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 4. Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Test the model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model trained successfully!")
print("--------------------------------")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)
print()

print("Model interpretation:")
print("The Mean Absolute Error shows the average prediction error in sales units.")
print("The R2 Score shows how well the model explains the sales pattern.")
print("Because this is a small learning dataset, the score may not be strong.")
print()

# 6. Make a new prediction
new_day = pd.DataFrame([{
    "Temperature": 30,
    "isWeekend": 1,
    "isHoliday": 0,
    "PreviousDaySales": 80,
    "Price": 3.00,
    "Promotion": 0,
    "Rain_mm": 2.5,
    "Humidity": 70
}])

predicted_sales = model.predict(new_day)

print("New day scenario:")
print(new_day)
print()
print("Predicted ice cream sales:", round(predicted_sales[0], 2))
