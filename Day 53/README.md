# Day 53 – Pandas Sorting, Ranking & Top-N Analysis

## Topic

Pandas `sort_values()`, `sort_index()`, ranking, `nlargest()`, `nsmallest()`, sorting by multiple columns, and Top-N analysis.

## What I Learned

Today I practiced sorting, ranking, and extracting top and bottom records from a Pandas DataFrame. I also combined these operations with `groupby()` to perform practical data analysis.

### 1. `sort_values()`

Used `sort_values()` to sort DataFrame rows based on column values.

```python
df.sort_values("Amount")
```

By default, the values are sorted in ascending order.

For descending order:

```python
df.sort_values("Amount", ascending=False)
```

### 2. Sorting by Multiple Columns

Used multiple columns for sorting:

```python
df.sort_values(["City", "Amount"], ascending=[True, False])
```

This sorts:

* `City` in ascending order
* `Amount` in descending order within each city

### 3. `sort_index()`

Used `sort_index()` to sort the DataFrame according to its index.

```python
df.sort_index()
```

For descending index order:

```python
df.sort_index(ascending=False)
```

### 4. `rank()`

Used `rank()` to assign rankings based on transaction amounts.

```python
df["Rank"] = df["Amount"].rank(ascending=False)
```

Using `ascending=False` gives the highest amount Rank 1.

Example:

```text
Amount    Rank
400        1
380        2
350        3
```

### 5. `nlargest()`

Used `nlargest()` to find the records with the highest values.

```python
df.nlargest(3, "Amount")
```

This returns the 3 highest transactions.

### 6. `nsmallest()`

Used `nsmallest()` to find the records with the lowest values.

```python
df.nsmallest(3, "Amount")
```

This returns the 3 lowest transactions.

### 7. Customer-wise Sales Analysis

Combined `groupby()` with sorting:

```python
customer_sales = df.groupby("Customer")["Amount"].sum()

customer_sales.sort_values(ascending=False)
```

This calculates the total spending of each customer and sorts the results from highest to lowest.

### 8. Top-N Customer Analysis

Used `nlargest()` after grouping:

```python
customer_sales.nlargest(3)
```

This finds the top 3 customers based on total spending.

### 9. City and Item Analysis

Grouped sales using multiple columns:

```python
sales = df.groupby(["City", "Item"])["Amount"].sum()
```

Then sorted the results:

```python
sales.sort_values(ascending=False)
```

This helped identify which city-item combinations generated the most sales.

## Mini Data Analyst Challenge

Worked with a café sales dataset containing:

* Customer
* City
* Item
* Amount

Used Pandas to answer practical questions such as:

* Which transactions have the highest amounts?
* Which transactions have the lowest amounts?
* Who are the top customers by total spending?
* What is the ranking of each transaction?
* Which city and item combination generated the most sales?
* How can grouped data be sorted to find useful insights?

## Key Takeaway

Sorting and ranking make it easier to turn calculated results into useful insights.

The general pattern I practiced was:

```text
Group → Calculate → Sort → Rank → Select Top/Bottom → Find Insights
```

## Summary

Today I learned how to use Pandas for practical data analysis with:

* `sort_values()`
* `sort_index()`
* `rank()`
* `nlargest()`
* `nsmallest()`
* Ascending and descending sorting
* Multiple-column sorting
* `groupby()` + sorting
* Top-N analysis
* City and item sales analysis