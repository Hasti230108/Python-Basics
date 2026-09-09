# Day 56 — Pandas Revision

Today I revised **Pandas** by working with a student performance dataset.

The revision focused on creating DataFrames, filtering data, handling missing values, sorting, ranking, aggregation, and grouping data.

## Topics Revised

* Pandas DataFrame
* DataFrame creation
* `head()` and `tail()`
* Filtering Data
* Selecting Columns
* `loc[]`
* `iloc[]`
* Missing Data
* `isnull()`
* `fillna()`
* `sort_values()`
* `nlargest()`
* `nsmallest()`
* Mean, Maximum, Minimum and Sum
* `groupby()`
* Aggregation
* Ranking using `rank()`

## DataFrame Creation

Created a student performance DataFrame containing:

* Name
* Course
* Marks
* Age
* City

```python
df = pd.DataFrame(data)
```

## Data Filtering

Filtered students based on their marks, city and course.

```python
df[df["Marks"] > 80]

df[df["Marks"] >= 80]

df[df["City"] == "Mumbai"]

df[df["Course"] == "AI & ML"]
```

## Selecting Data

Practiced selecting specific columns and rows.

```python
df[["Name", "Marks"]]

df.loc[0:3]

df.iloc[0:4]
```

## Handling Missing Data

Checked for missing values and replaced the missing marks with the average marks.

```python
df.isnull().sum()

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
```

## Sorting and Top/Bottom Students

Sorted students according to their marks.

```python
df.sort_values("Marks", ascending=False)

df.nlargest(3, "Marks")

df.nsmallest(3, "Marks")
```

The top 3 students were:

1. Hasti — 91
2. Himanshi — 89
3. Ananya — 88

## Statistical Operations

Practiced basic statistical operations on the marks column.

```python
df["Marks"].mean()

df["Marks"].max()

df["Marks"].min()

df["Marks"].sum()
```

Results:

* Mean: `81.0`
* Maximum: `91.0`
* Minimum: `56.0`
* Sum: `648.0`

## GroupBy and Aggregation

Calculated course-wise average marks, maximum marks and student count.

```python
df.groupby("Course")["Marks"].mean()

df.groupby("Course")["Marks"].max()

df.groupby("Course").size()
```

## Ranking

Created a rank column based on student marks.

```python
df["rank"] = df["Marks"].rank(ascending=False)

df.sort_values("rank")
```

Hasti secured **Rank 1** with 91 marks.

## Key Takeaways

> Pandas makes it easier to work with structured data.

> `loc[]` and `iloc[]` are used for selecting rows and data.

> `fillna()` can be used to handle missing values.

> `groupby()` is useful for analyzing data category-wise.

> `sort_values()` helps arrange data in ascending or descending order.

> `nlargest()` and `nsmallest()` are useful for finding top and bottom records.

> `rank()` can be used to rank values in a DataFrame.