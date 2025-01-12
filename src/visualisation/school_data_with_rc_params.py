import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import IPython.display as display

mpl.rcParams["figure.figsize"] = (10, 6)  # Default figure size
mpl.rcParams["axes.titlesize"] = 14  # Title font size
mpl.rcParams["axes.labelsize"] = 12  # Axis label font size
mpl.rcParams["xtick.labelsize"] = 10  # X-axis tick label size
mpl.rcParams["ytick.labelsize"] = 10  # Y-axis tick label size
mpl.rcParams["legend.fontsize"] = 10  # Legend font size
mpl.rcParams["lines.linewidth"] = 2  # Line width
mpl.rcParams["lines.markersize"] = 6  # Marker size
mpl.rcParams["lines.linestyle"] = "-."  # Default line style
mpl.rcParams["lines.marker"] = "o"  # Default marker style
mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=["green"])

# Load data from a pickle file
df = pd.read_pickle("../../data/interim/Processed_School_Data_W_Functions.pkl")
df = df.set_index("name")


for category in df["category"].unique():
    category_df = df[df["category"] == category]
    # Uncomment the following line to display the DataFrame for each category
    # display(category_df)

    plt.subplots()  # Create a new subplot for each category
    plt.plot(
        category_df["score"],
        label=category,  # Label is specific to each plot and remains in the function
    )
    plt.title(f"Score - {category}")
    plt.xlabel("Student Names")
    plt.ylabel("Score")
    plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
    plt.legend()  # Add legend for the category
    plt.tight_layout()  # Adjust the layout to avoid clipping
    plt.show()