import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from IPython.display import display

# Load data from a pickle file
df = pd.read_pickle("../../data/interim/Processed_School_Data_W_Functions.pkl")
df = df.set_index("name")

for category in df["category"].unique():
    category_df = df[df["category"] == category]
    # display(category_df)
    plt.subplots()
    plt.plot(
        category_df["study_hours_per_week"],
        marker="o",
        linestyle="-.",
        label=category,
        color="green",
    )
    plt.title(f"Study Hours per Week - {category}")
    plt.xlabel("Student Names")
    plt.ylabel("Study Hours")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()