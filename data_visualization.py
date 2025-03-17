import os

import matplotlib
matplotlib.use("Agg")
import pandas as pd
import matplotlib.pyplot as plt

# load CSV
file_path = "user_data.csv"

def load_data():
    """Load user data from CSV"""
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print("Error. user_data.csv is empty. Run main.py to collect user data first.")
            return None
        print(f"Loaded {len(df)} entries from user_data.csv.csv")
        print("Columns found: ", df.columns.tolist())
        return df
    except FileNotFoundError:
        print("Error: user_data.csv.csv not found. Run main.py to collect user data first.")
        return None
    except pd.errors.EmptyDataError:
        print("error. user_data.csv is empty. run main.py first to collect data.")
        return None

def plot_water_vs_weight(df):
    """creates and returns a scatter plot of water intake vs weight"""
    plt.figure(figsize=(8, 5))
    if "Weight_lbs" not in df.columns or "Water_Intake_oz" not in df.columns:
        print("error: weight or water intake columns are not found")
        return None

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df["Weight_lbs"], df["Water_Intake_oz"], color="blue", alpha=0.6)
    ax.set_xlabel("Weight (lbs)")
    ax.set_ylabel("Recommended Water Intake (oz)")
    ax.set_title("Water Intake vs Weight")
    ax.grid(True)

    return fig

def plot_water_by_activity(df):
    """Bar chart showing average water intake per activity level"""

    fig, ax = plt.subplots(figsize=(6, 5))
    activity_avg = df.groupby("Activity_level")["Water_Intake_oz"].mean()
    activity_avg.plot(kind="bar", color=["green", "orange", "red"], ax=ax)
    ax.set_xlabel("Activity Level (1 = Low, 2 = Moderate, 3 = High)")
    ax.set_ylabel("Average water intake (oz)")
    ax.set_title("Average water intake by activity level")
    ax.grid(axis="y")

    return fig

def plot_water_distribution(df):
    """creates a histogram of water intake distribution"""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["Water_Intake_oz"], bins=10, color="purple", alpha=0.7, edgecolor="black")
    ax.set_xlabel("Water intake (oz)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of water intake recommendations")
    ax.grid(axis="y")

    return fig

if __name__=="__main__":
    data = load_data()
    if data is not None:
        plot_water_vs_weight(data)
        plot_water_by_activity(data)
        plot_water_distribution(data)

