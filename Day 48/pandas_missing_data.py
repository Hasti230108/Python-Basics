import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Hasti", "Elia", "Tahseen", "Twinkle", "Rahul"],
    "Age": [19, np.nan, 21, np.nan, 20],
    "Marks": [86, 92, np.nan, 88, np.nan],
    "City": ["Mumbai", "Mumbai", np.nan, "Andheri", "Mumbai"]
})

print("Original DataFrame:")
print(df)

# To check if there is missing value in dataframe
print("\nMissing Values:")
print(df.isna())

# To count missing values in each column
print("\nNumber of Missing Values in Each Column:")
print(df.isna().sum())

# To remove rows containing missing values
clean_df = df.dropna()
print("\nDataFrame After Removing Missing Values:")
print(clean_df)

# To fill missing values with a specific value
filled_df = df.fillna("Not Available")
print("\nDataFrame After Filling Missing Values:")
print(filled_df)

# To fill missing marks values with 0
marked_filled_df = df.copy()
marked_filled_df["Marks"] = marked_filled_df["Marks"].fillna(0)
print("\nDataFrame After Filling Missing Marks with 0:")
print(marked_filled_df)

# To fill missing age values with average age
average_age_df = df.copy()
average_age_df["Age"] = average_age_df["Age"].fillna(average_age_df["Age"].mean())
print("\nDataFrame After Filling Missing Ages with Average:")
print(average_age_df)