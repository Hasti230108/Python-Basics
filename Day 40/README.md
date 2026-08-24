# Day 40 — Pandas Basics 

## Topic

**Pandas Basics — Series, DataFrames, Data Inspection, Column Selection & Filtering**

## Objective

The goal of Day 40 was to begin learning **Pandas**, a Python library used for working with structured and tabular data.

Pandas is especially useful for data analysis and data preprocessing, and its `DataFrame` structure is similar to a table in a spreadsheet or database.

## Topics Covered

### 1. Importing Pandas

```python
import pandas as pd
```

`pd` is the commonly used alias for Pandas.

### 2. Pandas Series

A **Series** represents a one-dimensional labeled collection of data.

Example:

```python
marks = pd.Series(
    [72, 85, 91, 64, 78],
    index=["Maths", "Physics", "Biology", "Chemistry", "English"]
)
```

Custom indexes can be assigned to Series values.

### 3. Pandas DataFrame

A **DataFrame** is a two-dimensional table containing rows and columns.

Example:

```python
df = pd.DataFrame({
    "Name": ["Hasti", "Elia", "Tahseen", "Twinkle"],
    "Age": [19, 18, 21, 20],
    "Marks": [85, 92, 76, 88],
    "City": ["Mumbai", "Wadala", "Andheri", "Vile Parle"]
})
```

The DataFrame automatically creates the default row indexes:

```text
0
1
2
3
```

### 4. Exploring a DataFrame

#### First rows

```python
df.head(2)
```

Displays the first 2 rows.

#### Last rows

```python
df.tail(2)
```

Displays the last 2 rows.

#### Shape

```python
df.shape
```

Returns:

```text
(rows, columns)
```

For this DataFrame:

```text
(4, 4)
```

#### Column names

```python
df.columns
```

#### Data types

```python
df.dtypes
```

`head()` and `tail()` are methods, while `shape`, `columns`, and `dtypes` are attributes.

### 5. Selecting Columns

#### Single column

```python
df["Name"]
```

```python
df["Marks"]
```

Selecting one column returns a Series.

#### Multiple columns

```python
df[["Name", "Marks"]]
```

Selecting multiple columns returns a DataFrame.

### 6. Filtering Rows

Pandas allows rows to be selected using conditions.

#### Marks ≥ 80

```python
df[df["Marks"] >= 80]
```

#### Age < 20

```python
df[df["Age"] < 20]
```

#### City is Mumbai

```python
df[df["City"] == "Mumbai"]
```

#### Marks between 80 and 90

```python
df[(df["Marks"] >= 80) & (df["Marks"] <= 90)]
```

Important operators learned:

| Operator | Meaning               |    |
| -------- | --------------------- | -- |
| `>`      | Greater than          |    |
| `<`      | Less than             |    |
| `>=`     | Greater than or equal |    |
| `<=`     | Less than or equal    |    |
| `==`     | Equal                 |    |
| `!=`     | Not equal             |    |
| `&`      | AND                   |    |
| `        | `                     | OR |

When combining Pandas conditions, each condition should be placed inside parentheses.

## Key Learning

Day 40 introduced the basic Pandas workflow:

```text
Create data
    ↓
Create Series/DataFrame
    ↓
Inspect the data
    ↓
Select columns
    ↓
Filter rows
    ↓
Analyze the required data
```

These operations form the foundation for later Pandas work involving **data cleaning, preprocessing, statistics, grouping, sorting, and eventually machine learning datasets**. Pandas is specifically designed for exploring, cleaning, and processing tabular data.