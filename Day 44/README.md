# Day 44 - Pandas `groupby()` and Aggregation

## Topics Covered

* Grouping data using `groupby()`
* Calculating average using `mean()`
* Calculating total using `sum()`
* Finding highest values using `max()`
* Finding lowest values using `min()`
* Counting values using `count()`
* Applying multiple aggregations using `agg()`
* Grouping data using multiple columns
* Using `as_index=False`
* Creating custom column names using named aggregation

## What I Learned

### 1. Grouping by a Single Column

I grouped students based on their `City` and performed different operations on the `Marks` column.

I calculated:

* Average marks
* Total marks
* Highest marks
* Lowest marks
* Number of students

### 2. Multiple Aggregations

Instead of performing each calculation separately, I used `agg()` to apply multiple operations at once.

The operations included:

* `mean`
* `sum`
* `max`
* `min`
* `count`

### 3. Grouping by Multiple Columns

I added a `Course` column and grouped the data using both:

* `City`
* `Course`

This created separate groups for each unique combination of City and Course.

### 4. Using `as_index=False`

I learned that by default, the grouping column becomes the index of the result.

Using `as_index=False` keeps the grouping column as a normal column and returns a more DataFrame-like result.

### 5. Named Aggregation

I used named aggregation to create meaningful output column names such as:

* `Average_Marks`
* `Highest_Marks`
* `Total_Students`

## Key Takeaway

Today I learned how to group data and calculate statistics for each group using Pandas. I also learned how to group by multiple columns and use `agg()` to perform multiple calculations at once.

The main idea of `groupby()` is:

**Group the data → Apply an operation → Get the combined result**