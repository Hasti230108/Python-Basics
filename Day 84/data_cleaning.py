import pandas as pd
import numpy as np

data = {
    "Name": ["Hasti", "Mahek", "Siddh", "Nehal", "Mahek", "Risha", "Kriish"],
    "Age": [19, 20, np.nan, 19, 20, 21, 18],
    "Course": ["AI & ML", "BSc CS", "AI & ML", "BSc CS", "BSc CS", None, "AI & ML"],
    "Marks": [93, 85, 78, np.nan, 85, 95, 89]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Check Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated())

# Remove Duplicate Rows
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# Fill Missing Values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Course"] = df["Course"].fillna("Unknown")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter Handling Missing Values:")
print(df)

# Clean Text
df["Name"] = df["Name"].str.strip().str.title()
df["Course"] = df["Course"].str.strip()

# Display Final Dataset
print("\nCleaned Dataset:")
print(df)

# Verify Cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())