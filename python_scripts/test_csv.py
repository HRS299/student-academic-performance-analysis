import pandas as pd

# Read CSV file
df = pd.read_csv("data/Student_Data.csv")

# Show first 5 rows
print(df.head())

# Show total rows and columns
print("\nDataset Shape:")
print(df.shape)

# Show column names
print("\nColumns:")
print(df.columns)