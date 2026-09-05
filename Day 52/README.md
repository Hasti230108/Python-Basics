# Day 52 – Pandas GroupBy & Data Analysis

## Topic

Pandas `groupby()`, aggregation, multi-column grouping, `agg()`, and `idxmax()`

## What I Learned

Today I practiced using Pandas to analyze a realistic sales dataset instead of just working with basic DataFrame operations.

### 1. `groupby()`

Used `groupby()` to divide data into groups based on a column and perform calculations on each group.

```python
df.groupby("City")["Amount"].sum()
```

### 2. Aggregation Functions

Practiced:

* `sum()` – total sales
* `mean()` – average sales
* `max()` – highest sale
* `count()` – number of non-missing values
* `size()` – number of rows/orders

### 3. `agg()`

Used multiple aggregation functions together to create a city-wise sales report.

```python
city_report = df.groupby("City").agg({
    "Amount": ["sum", "mean", "count"]
})
```

This produced a report containing:

* Total sales
* Average sale
* Number of orders

### 4. Grouping by Multiple Columns

Grouped the data using both `City` and `Item`:

```python
sales = df.groupby(["City", "Item"])["Amount"].sum()
```

This helped calculate the total sales for each item within each city.

### 5. `idxmax()`

Used `idxmax()` to find the highest-selling item for each city.

```python
best_selling = sales.groupby(level=0).idxmax()
```

Results:

* Mumbai → Coffee
* Navi Mumbai → Pizza
* Thane → Pizza

## Mini Data Analyst Challenge

Worked with a café sales dataset containing:

* Customer
* City
* Item
* Amount

Used Pandas to answer practical questions such as:

* Which city generated the most sales?
* What is the average spending in each city?
* What is the highest individual sale in each city?
* How many orders were placed for each item?
* Which item sold the most in each city?

## Key Takeaway

`groupby()` is useful for turning raw data into meaningful summaries.

The general pattern I practiced was:

```text
Group → Calculate → Compare → Find Insights
```

## Summary

Today I learned how to use Pandas for practical data analysis with:

* `groupby()`
* `sum()`
* `mean()`
* `max()`
* `count()`
* `size()`
* `agg()`
* Multi-column grouping
* MultiIndex
* `idxmax()`