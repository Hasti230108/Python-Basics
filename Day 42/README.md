# Day 42 — Pandas Missing Data Handling

## Overview

Today I learned how to **detect, count, fill, and remove missing values** in a Pandas DataFrame. Missing data is common in real-world datasets, so handling it properly is an important part of data cleaning. Pandas provides functions such as `isna()`, `fillna()`, and `dropna()` for this purpose.

## Topics Covered

### 1. Detecting Missing Values — `isna()`

```python
df.isna()
```

Returns `True` where a value is missing and `False` where a value exists.

### 2. Counting Missing Values

```python
df.isna().sum()
```

`isna()` identifies missing values, while `sum()` counts them column-wise.

### 3. Filling Missing Values — `fillna()`

```python
df["Age"] = df["Age"].fillna(20)
```

Replaces missing values with the specified value.

It can also be used on the complete DataFrame:

```python
df.fillna("Unknown")
```

### 4. Filling with the Mean

```python
average_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(average_marks)
```

Instead of using an arbitrary value, the missing mark was replaced with the column's average.

### 5. Removing Missing Data — `dropna()`

```python
df.dropna()
```

Removes rows containing missing values.

## Key Learning

The basic workflow for missing data is:

```text
Detect → Count → Fill/Replace → Remove if necessary
```

### Important Functions

* `isna()` → Detect missing values
* `isna().sum()` → Count missing values
* `fillna()` → Fill missing values
* `mean()` → Calculate average for numerical data
* `dropna()` → Remove rows/columns containing missing values