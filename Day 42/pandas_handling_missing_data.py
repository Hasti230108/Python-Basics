import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Hasti", "Elia", "Tahseen", "Twinkle"],
    "Age": [19, np.nan, 21, 20],
    "Marks": [85, 92, np.nan, 88],
    "City": ["Mumbai", "Wadala", None, "Vile Parle"]
})

print(df)

print("\n", df.isna())

print("\n", df.isna().sum())

df["Age"] = df["Age"].fillna(20)

print("\n", df)

print("\n", df.fillna("Unknown"))

average_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(average_marks)

print("\n", df)

print("\n", df.dropna())