import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Hasti", "Elia", "Tahseen"],
    "Marks": [86, 92, 75]
})

df2 = pd.DataFrame({
    "Name": ["Twinkle", "Rahul", "Ananya"],
    "Marks": [88, 90, 95]
})

print("First Dataframe:")
print(df1)

print("\nSecond Dataframe:")
print(df2)

combined_df = pd.concat([df1, df2])

print("\nCombined DataFrame:")
print(combined_df)

combined_ignore_index_df = pd.concat(
    [df1, df2],
    ignore_index=True
)
print("\nCombined DataFrame with Reset Index:")
print(combined_ignore_index_df)

df3 = pd.DataFrame({
    "City": ["Mumbai", "Mumbai", "Andheri", "Andheri", "Mumbai", "Andheri"],
    "Course": ["AI & ML", "AI & ML", "Data Science", "Data Science", "AI & ML", "Data Science"]
})

horizontal_df = pd.concat(
    [combined_ignore_index_df, df3],
    axis=1
)

print("\nDataFrames Combined Horizontally:")
print(horizontal_df)

df4 = pd.DataFrame({
    "Name": ["Daksh", "Tinker"],
    "Marks": [90, 94]
})

df5 = pd.DataFrame({
    "Name": ["Tejal", "Hassan"],
    "City": ["Vile Parle", "Mumbai"]
})

different_columns_df = pd.concat(
    [df4, df5],
    ignore_index=True
)

print("\nCombined DataFrames with Different Columns:")
print(different_columns_df)

keyed_df = pd.concat(
    [df1, df2],
    keys=["First_Group", "Second_Group"]
)

print("\nCombined DataFrame with Keys:")
print(keyed_df)