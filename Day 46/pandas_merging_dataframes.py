import pandas as pd

# Students DataFrame containing Student ID and Name
students = pd.DataFrame({
    "Student ID": [101, 102, 103],
    "Name": ["Hasti", "Elia", "Tahseen"]
})

# Marks DataFrame containing Student ID and Marks
marks = pd.DataFrame({
    "Student ID": [101, 103, 104],
    "Marks": [86, 92, 75]
})

print("Students DataFrame:")
print(students)

print("Marks DataFrame:")
print(marks)

# Default Merge using the common Student ID column
merged_df = pd.merge(
    students,
    marks,
    on="Student ID"
)

print("\nMerged DataFrame:")
print(merged_df)

# Inner Merge using the common Student ID column
inner_merge_df = pd.merge(
    students,
    marks,
    on="Student ID",
    how="inner"
)

print("\nInner Merge DataFrame:")
print(inner_merge_df)

# Left Merge using the common Student ID column
left_merge_df = pd.merge(
    students,
    marks,
    on="Student ID",
    how="left"
)

print("\nLeft Merge DataFrame:")
print(left_merge_df)

# Right Merge using the common Student ID column
right_merge_df = pd.merge(
    students,
    marks,
    on="Student ID",
    how="right"
)

print("\nRight Merge DataFrame:")
print(right_merge_df)

# Outer Merge using the common Student ID column
outer_merge_df = pd.merge(
    students,
    marks,
    on="Student ID",
    how="outer"
)

print("\nOuter Merge DataFrame:")
print(outer_merge_df)

# Outer Merge with an indicator column
indicator_df = pd.merge(
    students,
    marks,
    on="Student ID",
    how="outer",
    indicator=True
)

print("\nOuter Merge with Indicator:")
print(indicator_df)