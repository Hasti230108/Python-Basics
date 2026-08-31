import pandas as pd

df = pd.DataFrame({
    "Name": ["Hasti", "Elia", "Tahseen", "Twinkle", "Rahul", "Ananya"],
    "City": ["Mumbai", "Mumbai", "Andheri", "Andheri", "Mumbai", "Andheri"],
    "Course": ["AI & ML", "Data Science", "AI & ML", "Data Science", "AI & ML", "AI & ML"],
    "Marks": [86, 92, 75, 88, 90, 95]
})

print("Original DataFrame:")
print(df)

# To calculate average marks by city
city_pivot = pd.pivot_table(
    df,
    values="Marks",
    index="City",
    aggfunc="mean"
)

print("\nAverage Marks by City:")
print(city_pivot)

# To calculate average marks by course
course_pivot = pd.pivot_table(
    df, 
    values="Marks",
    index="Course",
    aggfunc="mean"
)

print("\nAverage Marks by Course:")
print(course_pivot)

# To calculate average marks by city and course
city_course_pivot = pd.pivot_table(
    df,
    values="Marks",
    index="City",
    columns="Course",
    aggfunc="mean"
)

print("\nAverage Marks by City and Course")
print(city_course_pivot)

# To calculate multiple Aggregate Functions Called Multiple Statistics
statistics_pivot = pd.pivot_table(
    df,
    values="Marks",
    index="City",
    aggfunc=["mean", "sum", "max", "min"]
)

print("\nMultiple Statistics by City:")
print(statistics_pivot)

# To count students by City and Course
count_pivot = pd.pivot_table(
    df,
    values="Name",
    index="City",
    columns="Course",
    aggfunc="count",
    fill_value=0
)

print("\nNumber of students by City and Course:")
print(count_pivot)