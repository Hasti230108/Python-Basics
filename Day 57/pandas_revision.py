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

print("\n", df.shape)

print("\n", df.columns)

print("\n", df.dtypes)

print("\n", df.describe())

print("\n", df["Marks"].mean())

print("\n", df["Marks"].median())

print("\n", df["Marks"].std())

print("\n", df["Marks"].value_counts())

print("\n", df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\n", df)

print("\n", df[df["Marks"] > df["Marks"].mean()])

print("\n", df.sort_values("Marks", ascending=False))

print("\n", df.nlargest(3, "Marks"))

print("\n", df.nsmallest(3, "Marks"))

print("\n", df.groupby("Course")["Marks"].mean())

print("\n", df.groupby("City")["Marks"].mean())

print("\n", df.groupby("Course")["Marks"].agg(["mean", "max", "min", "count"]))

df["Grade"] = np.where(
    df["Marks"] >= 90, "A",
    np.where(
        df["Marks"] >= 80, "B",
        np.where(
            df["Marks"] >= 70, "C",
            np.where(df["Marks"] >= 60, "D", "F")
        )
    )
)

print("\n", df)

df["Rank"] = df["Marks"].rank(ascending=False)

print("\n", df.sort_values("Rank"))

print("\n", df[df["Grade"].isin(["A", "B"])])

print("\n", df["Marks"].to_numpy())

marks = np.array(df["Marks"])

print("\n", marks)

print("\n", np.mean(marks))

print("\n", np.max(marks))

print("\n", np.min(marks))

print("\n", np.median(marks))

print("\n", np.where(marks >= 80))