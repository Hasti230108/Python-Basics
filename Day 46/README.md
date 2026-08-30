# Day 46 - Merging DataFrames using Pandas

Today I learned how to combine DataFrames using the `merge()` function in Pandas. Merging DataFrames is similar to performing joins in SQL, where two tables are combined using a common column.

## Topics Covered

* `pd.merge()`
* Inner Merge
* Left Merge
* Right Merge
* Outer Merge
* `indicator=True`

## What I Learned

### 1. Basic Merge

I used `pd.merge()` to combine the `students` and `marks` DataFrames using the common `Student ID` column.

```python
pd.merge(students, marks, on="Student ID")
```

By default, Pandas performs an **inner merge**, meaning only the matching Student IDs from both DataFrames are included.

### 2. Inner Merge

An inner merge returns only the records where the `Student ID` exists in both DataFrames.

```python
pd.merge(students, marks, on="Student ID", how="inner")
```

In my example, Student IDs `101` and `103` existed in both DataFrames.

### 3. Left Merge

A left merge keeps all records from the left DataFrame.

```python
pd.merge(students, marks, on="Student ID", how="left")
```

If a matching Student ID does not exist in the right DataFrame, the missing values are displayed as `NaN`.

### 4. Right Merge

A right merge keeps all records from the right DataFrame.

```python
pd.merge(students, marks, on="Student ID", how="right")
```

If a matching Student ID does not exist in the left DataFrame, the missing values are displayed as `NaN`.

### 5. Outer Merge

An outer merge keeps all Student IDs from both DataFrames.

```python
pd.merge(students, marks, on="Student ID", how="outer")
```

Missing values are represented using `NaN`.

### 6. Merge Indicator

I also used `indicator=True` to identify where each row came from.

```python
pd.merge(
    students,
    marks,
    on="Student ID",
    how="outer",
    indicator=True
)
```

The `_merge` column shows:

* `both` → Student ID exists in both DataFrames
* `left_only` → Student ID exists only in the left DataFrame
* `right_only` → Student ID exists only in the right DataFrame

## Practical Work

I created two DataFrames:

* `students` containing Student ID and Name
* `marks` containing Student ID and Marks

I intentionally used different Student IDs in both DataFrames to understand the difference between different types of merges.

### Student IDs

**Students DataFrame:**

* 101
* 102
* 103

**Marks DataFrame:**

* 101
* 103
* 104

This helped me clearly understand how each merge type handles matching and non-matching records.

## Key Takeaway

Today I learned that Pandas `merge()` combines DataFrames using a common column, similar to SQL joins.

The main difference between the merge types is:

* **Inner Merge** → Only matching records
* **Left Merge** → All records from the left DataFrame
* **Right Merge** → All records from the right DataFrame
* **Outer Merge** → All records from both DataFrames

I also learned how `indicator=True` helps identify whether a record came from the left DataFrame, right DataFrame, or both.