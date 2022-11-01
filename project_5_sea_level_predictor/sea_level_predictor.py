import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 8))
    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    reg_full = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    pred_full_df = pd.DataFrame()
    pred_full_df["Year"] = range(1880, 2051)
    pred_full_df["Predicted"] = (
        reg_full.intercept + reg_full.slope * pred_full_df["Year"]
    )

    plt.plot(pred_full_df["Year"], pred_full_df["Predicted"])

    # Create second line of best fit
    recent_df = df.loc[df["Year"] >= 2000]
    reg_recent = linregress(
        x=recent_df["Year"], y=recent_df["CSIRO Adjusted Sea Level"]
    )
    pred_recent_df = pd.DataFrame()
    pred_recent_df["Year"] = range(2000, 2051)
    pred_recent_df["Predicted"] = (
        reg_recent.intercept + reg_recent.slope * pred_recent_df["Year"]
    )

    plt.plot(pred_recent_df["Year"], pred_recent_df["Predicted"])

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
