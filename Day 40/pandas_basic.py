import pandas as pd

marks = pd.Series([72, 85, 91, 64, 78], index=["Maths", "Physics", "Biology", "Chemistry", "English"])

print(marks)

df = pd.DataFrame({
    "Name": ["Hasti", "Elia", "Tahseen", "Twinkle"],
    "Age": [19, 18, 21, 20],
    "Marks": [85, 92, 76, 88],
    "City": ["Mumbai", "Wadala", "Andheri", "Vile Parle"]
})

print("\n", df)

print(f"\nFirst 2 rows: \n{df.head(2)}")

print(f"\nLast 2 rows: \n{df.tail(2)}")

print(f"\nShape: {df.shape}")

print(f"\nColumn Names: {df.columns}")

print(f"\nData Types: \n{df.dtypes}")

print("\n", df["Name"])

print("\n", df["Marks"])

print("\n", df[["Name", "Marks"]])

print(f"\nStudents with marks ≥ 80: \n{df[df["Marks"] >= 80]}")

print(f"\nStudents younger than 20: \n{df[df["Age"] < 20]}")

print(f"\nStudents from Mumbai: \n{df[df["City"] == "Mumbai"]}")

print(f"\nStudents who scored between 80 and 90: \n{df[(df["Marks"] >= 80) & (df["Marks"] <= 90)]}")