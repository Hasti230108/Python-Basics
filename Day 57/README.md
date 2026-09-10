# Day 57 — NumPy and Pandas Revision

Today I revised **NumPy and Pandas** together using a student performance dataset.

The revision focused on DataFrame information, statistical operations, filtering, sorting, grouping, aggregation, ranking, NumPy arrays, and conditional operations.

## Topics Revised

* Pandas DataFrame
* `shape`
* `columns`
* `dtypes`
* `describe()`
* `mean()`
* `median()`
* `std()`
* `value_counts()`
* Missing data handling
* Data filtering
* `sort_values()`
* `nlargest()`
* `nsmallest()`
* `groupby()`
* `agg()`
* `rank()`
* `isin()`
* NumPy arrays
* NumPy statistical functions
* `np.where()`


## DataFrame Information

Practiced checking the structure and information of a DataFrame.

```python
df.shape

df.columns

df.dtypes

df.describe()
```

## Statistical Operations

Used Pandas to calculate different statistical values.

```python
df["Marks"].mean()

df["Marks"].median()

df["Marks"].std()

df["Marks"].value_counts()
```

## Handling Missing Data

Checked for missing values and replaced the missing marks with the average.

```python
df.isnull().sum()

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
```

## Filtering and Sorting

Filtered students whose marks were above the average and sorted students by marks.

```python
df[df["Marks"] > df["Marks"].mean()]

df.sort_values("Marks", ascending=False)
```

## Top and Bottom Students

Used `nlargest()` and `nsmallest()` to find the highest and lowest marks.

```python
df.nlargest(3, "Marks")

df.nsmallest(3, "Marks")
```

## GroupBy and Aggregation

Performed course-wise and city-wise analysis.

```python
df.groupby("Course")["Marks"].mean()

df.groupby("City")["Marks"].mean()

df.groupby("Course")["Marks"].agg(["mean", "max", "min", "count"])
```

## Grade Calculation

Used NumPy `where()` to create a Grade column based on marks.

```python
df["Grade"] = np.where(
    df["Marks"] >= 90, "A",
    np.where(
        df["Marks"] >= 80, "B",
        np.where(
            df["Marks"] >= 70, "C",
            np.where(df["Marks"] >= 60, "D", "F")
        )
    )
)
```

## Ranking

Created a ranking based on student marks.

```python
df["Rank"] = df["Marks"].rank(ascending=False)

df.sort_values("Rank")
```

## Filtering with `isin()`

Used `isin()` to filter students belonging to selected grades.

```python
df[df["Grade"].isin(["A", "B"])]
```

## NumPy Revision

Converted the Pandas marks column into a NumPy array.

```python
marks = np.array(df["Marks"])
```

Practiced NumPy statistical operations:

```python
np.mean(marks)

np.max(marks)

np.min(marks)

np.median(marks)
```

Also used `np.where()` to find positions of students scoring 80 or above.

```python
np.where(marks >= 80)
```

## Key Takeaways

> Pandas is useful for working with structured and tabular data.

> `groupby()` helps perform category-wise analysis.

> `agg()` allows multiple calculations at the same time.

> `rank()` can be used to rank records based on values.

> NumPy provides powerful numerical and statistical operations.

> `np.where()` is useful for conditional operations.

> Pandas and NumPy can be used together for data analysis.