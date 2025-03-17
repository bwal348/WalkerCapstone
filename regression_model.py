import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

#sample data to begin learning
data = {
    "weight_lbs": [120, 140, 160, 180, 200, 220, 250, 284, 300, 193, 410, 235],
    "activity_level": [1, 2, 3, 2, 2, 1, 3, 2, 1, 2, 1, 3],
    "water_oz": [60, 84, 96, 90, 102, 120, 104, 124, 152, 98, 150, 120]
}

df = pd.DataFrame(data)

X = df [["weight_lbs", "activity_level"]]
y = df["water_oz"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "water_intake_model.pkl")

print("regression model trained and saved successfully")

