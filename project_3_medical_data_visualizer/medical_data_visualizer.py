import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df["bmi"] = df.weight / np.square(df.height / 100)
df["overweight"] = 0
df.loc[df.bmi > 25, "overweight"] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.cholesterol = np.where(df.cholesterol == 1, 0, 1)
df.gluc = np.where(df.gluc == 1, 0, 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df[
        ["id", "cholesterol", "gluc", "smoke", "alco", "active", "overweight", "cardio"]
    ].melt(id_vars=["id", "cardio"])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = (
        df_cat.groupby(["variable", "value", "cardio"])
        .count()
        .rename(columns={"id": "total"})
        .reset_index()
    )

    # Draw the catplot with 'sns.catplot()'
    cardio_plot = sns.catplot(
        data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar"
    )

    # Get the figure for the output
    fig = cardio_plot.fig

    # Do not modify the next two lines
    fig.savefig("catplot.png")
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.copy()

    df_heat["valid"] = 1
    df_heat.loc[df["ap_lo"] > df["ap_hi"], "valid"] = 0
    df_heat.loc[df["height"] < df["height"].quantile(0.025)] = 0
    df_heat.loc[df["height"] > df["height"].quantile(0.975)] = 0
    df_heat.loc[df["weight"] < df["weight"].quantile(0.025)] = 0
    df_heat.loc[df["weight"] > df["weight"].quantile(0.975)] = 0

    df_heat = df_heat.loc[df_heat.valid == True].drop(columns=["valid", "bmi"])

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(
        data=corr,
        mask=mask,
        ax=ax,
        annot=True,
        fmt=".1f",
        vmin=-1,
        vmax=1,
        cmap="icefire",
    )

    # Do not modify the next two lines
    fig.savefig("heatmap.png")
    return fig
