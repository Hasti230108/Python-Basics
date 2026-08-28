import pandas as pd

df = pd.DataFrame({
    "Name": ["Hasti", "Elia", "Tahseen", "Twinkle", "Rahul", "Ananya"],
    "City": ["Mumbai", "Mumbai", "Andheri", "Andheri", "Mumbai", "Andheri"],
    "Marks": [86, 92, 75, 88, 90, 95]
})

print(df)

print(f"\nAverage marks by City: \n{df.groupby("City")["Marks"].mean()}")
print(f"\nTotal marks by City: \n{df.groupby("City")["Marks"].sum()}")
print(f"\nHighest marks by City: \n{df.groupby("City")["Marks"].max()}")
print(f"\nLowest marks by City: \n{df.groupby("City")["Marks"].min()}")
print(f"\nNumber of Students in each City: \n{df.groupby("City")["Marks"].count()}")
print("\nMultiple statistics by City:")
print(df.groupby("City")["Marks"].agg(
    ["mean", "sum", "max", "min", "count"]
))

df = pd.DataFrame({
    "Name": ["Hasti", "Elia", "Tahseen", "Twinkle", "Rahul", "Ananya"],
    "City": ["Mumbai", "Mumbai", "Andheri", "Andheri", "Mumbai", "Andheri"],
    "Course": ["AI & ML", "AI & ML", "AI & ML", "Data Science", "Data Science", "AI & ML"],
    "Marks": [86, 92, 75, 88, 90, 95]
})

print(df)
print(f"\nAverage Marks by City and Course: \n{df.groupby(["City", "Course"])["Marks"].mean()}")
print("\nMultiple Statistics by City and Course: ")
print(df.groupby(["City", "Course"])["Marks"].agg(
    ["mean", "sum", "max", "min", "count"]
))
print("\nAverage Marks by City as a DataFrame:")
city_average = df.groupby("City", as_index=False)["Marks"].mean()
print(city_average)
print("\nCity Statistics:")
city_statistics = df.groupby(
    "City", as_index=False
).agg(
    Average_Marks=("Marks", "mean"),
    Highest_Marks=("Marks", "max"),
    Total_Students=("Name", "count")
)
print(city_statistics)