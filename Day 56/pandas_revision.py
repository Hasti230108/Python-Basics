import pandas as pd
import numpy as np

data = {
    "Name": ["Hasti", "Rahul", "Ananya", "Himanshi", "Twinkle", "Aarav", "Elia", "Kartik"],
    "Course": ["AI & ML", "Data Science", "AI & ML", "Web Development", "Data Science", "IT", "AI & ML", "Web Development"],
    "Marks": [91, 76, 88, 89, 56, 83, 84, np.nan],
    "Age": [18, 21, 20, 18, 22, 19, 19, 20],
    "City": ["Mumbai", "Pune", "Delhi", "Mumbai", "Bangalore", "Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

print(df)

print("\n", df.head())
print("\n", df.tail())

print("\n", df[df["Marks"] > 80])
    
print("\n", df[["Name", "Marks"]])

print("\n", df.loc[0:3])

print("\n", df.iloc[0:4])

print("\n", df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\n", df)

print("\n", df.sort_values("Marks", ascending=False))

print("\n", df.nlargest(3, "Marks"))

print("\n", df.nsmallest(3, "Marks"))

print("\n", df["Marks"].mean())
print("\n", df["Marks"].max())
print("\n", df["Marks"].min())
print("\n", df["Marks"].sum())

print("\n", df.groupby("Course")["Marks"].mean())

print("\n", df.groupby("Course")["Marks"].max())

print("\n", df.groupby("Course").size())

df["rank"] = df["Marks"].rank(ascending=False)

print("\n", df.sort_values("rank"))

print("\n", df[df["Marks"] >= 80])

print("\n", df[df["City"] == "Mumbai"])

print("\n", df[df["Course"] == "AI & ML"])