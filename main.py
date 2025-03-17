import os
import joblib
import numpy as np
import pandas as pd
from rule_based import calculate_water_intake

#Load the regression model
model = joblib.load("water_intake_model.pkl")

def predict_water_intake(weight_lbs, activity_level):
    """Predicts water intake using the regression model"""
    input_data = np.array([[weight_lbs, activity_level]])
    predicted_water_oz = model.predict(input_data)
    return round(predicted_water_oz[0], 2)


def save_user_data(age, height, weight, activity_level, water_needed):
    """saves user input data to later be analysed"""
    file_path = "user_data.csv"
    data = {
        "Age": [age],
        "Height_in": [height],
        "Weight_lbs": [weight],
        "Activity_level": [activity_level],
        "Water_Intake_oz": [water_needed]
    }
    df = pd.DataFrame(data)

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, mode='w', header=True, index=False)

    print("user data saved to CSV")

if __name__ == "__main__":
    age = int(input("Enter your age in years: "))
    height = float(input("Enter your height in inches: "))
    weight = float(input("Please enter your weight in pounds: "))

    while True:
        try:
            activity = int(input("Enter your activity level (1 = Low, 2 = Moderate, 3 = High): "))
            if activity in [1, 2, 3]:
                break
            else:
                print("Invalid input. Please enter 1, 2 , or 3 for activity level.")
        except ValueError:
            print("Invalid input. Please ensure all inputs are correct.")

    water_needed = calculate_water_intake(weight, activity)

    print(f"Your recommended daily water intake is: {water_needed} ounces")

    save_user_data(age, height, weight, activity, water_needed)