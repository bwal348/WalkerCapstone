import tkinter as tk
from tkinter import messagebox, Toplevel
import joblib
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from rule_based import calculate_water_intake
from data_visualization import plot_water_vs_weight, plot_water_by_activity, plot_water_distribution, file_path

# loads the trained model
model = joblib.load("water_intake_model.pkl")

# function to predict the water intake
def predict_water_intake(weight_lbs, activity_level):
    """predicts water intake using regression model"""
    input_data = np.array([[weight_lbs, activity_level]])
    predicted_water_oz = model.predict(input_data)
    return round(predicted_water_oz[0], 2)

#gets water intake and displays the result
def calculate():
    try:
        age = int(age_entry.get())
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        activity_level = int(activity_var.get())

        # chose model type
        if model_var.get()== "Regression Model":
            water_needed = predict_water_intake(weight, activity_level)
        else:
            water_needed = calculate_water_intake(weight, activity_level)
            #display result
        result_label.config(text=f"Recommended water intake: {water_needed} ounces")
        #data is saved
        save_user_data(age, height, weight, activity_level, water_needed)

    except ValueError:
        messagebox.showerror("Input Error. Please enter valid numerical values.")

# function to save the user data to CSV
def save_user_data(age, height, weight, activity_level, water_needed):

    file_path = "user_data.csv"
    data = {
        "Age": [age],
        "Height_in": [height],
        "Weight_lbs": [weight],
        "Activity_Level": [activity_level],
        "Water_Intake_oz": [water_needed]
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, mode='a', header=not os.path.exists(file_path), index=False)

#function to show the chart selected by the user
def show_chart(chart_function, title):
    """creates new window and displays the selected chart"""
    try:
        df = pd.read_csv("user_data.csv")

        if df.empty:
            messagebox.showwarning("No Data", "No data available.")
            return

        fig = chart_function(df)
        if fig is None:
            messagebox.showerror("chart error", "unable to generate chart")
            return

        chart_window = Toplevel(root)
        chart_window.title(title)
        chart_window.geometry("700x500")

        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except FileNotFoundError:
        messagebox.showerror("file not found", "user data file not found")


root = tk.Tk()
root.title("Water Intake Calculator")
root.geometry("400x600")

tk.Label(root, text="Age: ").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Height (inches): ").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Label(root, text="Weight (pounds): ").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Activity Level (1 = Low, 2 = Moderate, 3 = High): ").pack()
activity_var = tk.StringVar(value="1")
activity_dropdown = tk.OptionMenu(root, activity_var, "1", "2", "3")
activity_dropdown.pack()

tk.Label(root, text="Selection Model:").pack()

model_var = tk.StringVar(root)
model_var.set("Regression Model")
tk.Label(root, text="Select Model:").pack()

regression_button = tk.Radiobutton(root, text="Regression Model", variable=model_var, value="Regression Model")
regression_button.pack()

rule_button = tk.Radiobutton(root, text="Rule-Based System", variable=model_var, value="Rule-Based System")
rule_button.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

tk.Label(root, text="View Data Visualization:").pack(pady=5)
scatter_button = tk.Button(root, text="Scatter Plot (Weight vs Water)",
                           command=lambda: show_chart(plot_water_vs_weight, "Weight vs Water Intake"))
scatter_button.pack(pady=2)

bar_button = tk.Button(root, text="Bar Chart (Activity Level vs Water)",
                       command=lambda: show_chart(plot_water_by_activity, "Activity Level vs Water Intake"))
bar_button.pack(pady=2)

hist_button = tk.Button(root, text="Histogram (Water Intake Distribution)",
                        command=lambda: show_chart(plot_water_distribution, "Water Intake Distribution"))
hist_button.pack(pady=2)

root.mainloop()