import pandas as pd

df = pd.DataFrame({
    "Name": ["Hasti", "Elia", "Tahseen", "Twinkle", "Elia"],
    "Age": [19, 18, 21, 20, 18],
    "Marks": [85, 92, 76, 88, 92],
    "City": ["Mumbai", "Wadala", "Andheri", "Vile Parle", "Wadala"]
})

print(df, "\n")

clean_df = df.drop_duplicates()

print("\nData after removing duplicates:")
print(clean_df)

print("\nDuplicates based on Name:")
print(df.duplicated(subset="Name"))

name_clean_df = df.drop_duplicates(subset="Name")

print("\nData after removing duplicates based on Name:")
print(name_clean_df)

df["City"] = df["City"].replace("Wadala", "Mumbai")

print("\nData after replacing city:")
print(df)

print("\nStudents sorted by Marks:")
print(df.sort_values(by="Marks"))

print("\nStudents sorted by Marks (Highest to Lowest):")
print(df.sort_values(by="Marks", ascending=False))

print("\nStudents sorted by City and then Marks:")
print(df.sort_values(by=["City", "Marks"]))

print("\nStudents sorted by City (A-Z) and Marks (Highest to Lowest):")
print(df.sort_values(
    by=["City", "Marks"],
    ascending=[True, False]
))