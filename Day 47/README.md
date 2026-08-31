# Day 47 - Pandas Pivot Tables

Today I learned how to create and use **Pivot Tables in Pandas** using the `pd.pivot_table()` function.

Pivot tables are useful for summarizing and analyzing data by grouping values based on one or more categories.

## Topics Covered

* `pd.pivot_table()`
* Using `values`
* Using `index`
* Using `columns`
* Using `aggfunc`
* Using multiple aggregation functions
* Using `fill_value`

## What I Learned

### 1. Creating a Basic Pivot Table

I created a pivot table to calculate the average marks of students based on their city.

```python
pd.pivot_table(
    df,
    values="Marks",
    index="City",
    aggfunc="mean"
)
```

This grouped the students by city and calculated the average marks for each city.

### 2. Pivot Table by Course

I created another pivot table to calculate the average marks for each course.

The courses included:

* AI & ML
* Data Science

### 3. Pivot Table Using Rows and Columns

I used both `index` and `columns` to create a table showing the average marks based on both City and Course.

This made it easier to compare data across multiple categories.

### 4. Multiple Aggregation Functions

I used multiple aggregation functions in a single pivot table:

* `mean`
* `sum`
* `max`
* `min`

This allowed me to view multiple statistics for each city in one table.

### 5. Counting Students

I created a pivot table to count the number of students in each combination of City and Course.

I used:

```python
aggfunc="count"
```

to count the students.

### 6. Using `fill_value`

I used:

```python
fill_value=0
```

This can replace missing values in a pivot table with `0`.

## Important Parameters

| Parameter    | Purpose                                        |
| ------------ | ---------------------------------------------- |
| `values`     | Specifies the column to calculate or summarize |
| `index`      | Specifies the rows of the pivot table          |
| `columns`    | Specifies the columns of the pivot table       |
| `aggfunc`    | Specifies the aggregation function             |
| `fill_value` | Replaces missing values with a specified value |

## Practical Work

Today I created pivot tables to:

* Calculate average marks by City
* Calculate average marks by Course
* Calculate average marks by City and Course
* Calculate multiple statistics by City
* Count students by City and Course

## Key Takeaway

Today I learned that `pd.pivot_table()` is used to create spreadsheet-style summary tables from a DataFrame. It can group data using rows and columns and apply aggregation functions such as `mean`, `sum`, `max`, `min`, and `count`.

Pivot tables are useful for quickly summarizing and comparing data across different categories.
