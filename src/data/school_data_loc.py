import pandas as pd
from glob import glob

# --------------------------------------------------------------
# Define paths and filenames
# --------------------------------------------------------------

output_path = "../../data/processed/"

# Load the data
data_files = glob(output_path + "Processed_School_Data.csv")
df = pd.read_csv(data_files[0])
df["epoch (ms)"] = pd.to_datetime(df["epoch (ms)"])

# Filter rows where school is 'Maplewood Academy'
maplewood_students = df.loc[df["school"] == "Maplewood Academy"]
print(maplewood_students)


# top_students_df = df.loc[df["score"] <90 ]

# Select rows with 'A-level' category and specific columns
a_level_data = df.loc[df["category"] == "A-level", ["name", "subject", "score","category"]]
print(a_level_data)

# Get the score of James in Physics
james_score = df.loc[df["name"] == "James", "score"].iloc[0]
print(james_score)

# Get the first row
first_row = df.iloc[4]
print(first_row)

# Get rows 1 to 3 and columns 2 to 4
subset = df.iloc[0:6, 1:5]
print(subset)

# Get the subject of the second student
subject = df.iloc[11,2]
print(subject)