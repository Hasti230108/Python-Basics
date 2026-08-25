import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Hasti", "Elia", "Tahseen", "Twinkle"],
    "Age": [19, 18, 21, 20],
    "Marks": [85, 92, 76, 88],
    "City": ["Mumbai", "Wadala", "Andheri", "Vile Parle"]
})

print(df)

print("\n", df.loc[0])

print("\n", df.loc[0:2])

print("\n", df.loc[0:2, ["Name", "Marks"]])

print("\n", df.loc[3, "City"])

print("\n", df.iloc[0])

print("\n", df.iloc[0:2])

print("\n", df.iloc[0:2, [0,2]])

print("\n", df.iloc[3, 3])

print("\n", df[df["Marks"] > 80])

print("\n", df[df["Age"] < 20])

print("\n", df[df["City"] == "Mumbai"])

print("\n", df[(df["Marks"] >= 80) & (df["Marks"] <= 90)])

df.loc[0, "Marks"] = 90

df.loc[1, "City"] = "Mumbai"

df.loc[df["Marks"] < 80, "Marks"] = df["Marks"] + 5

print("\n", df)

# df["Result"] = df["Marks"].apply(lambda x: "PASS" if x >= 50 else "FAIL")
df["Result"] = np.where(df["Marks"] >= 50, "PASS", "FAIL")

print("\n", df)

conditions = [
    df["Marks"] >= 90,
    df["Marks"] >= 80,
    df["Marks"] >= 70,
    df["Marks"] >= 60
]
choices = ["O", "A", "B", "C"]

df["Grade"] = np.select(conditions, choices, default="D")

print("\n", df)