# Day 41 – Pandas Indexing & Data Manipulation

## Overview

Today I continued learning **Pandas** and worked with a DataFrame using `.loc`, `.iloc`, conditional filtering, updating values, and creating new columns.

A useful part of today's learning was combining **Pandas and NumPy**. Pandas was used for working with the DataFrame, while NumPy was used for condition-based operations such as creating `Result` and `Grade` columns.

## Topics Covered

### 1. `.loc[]` – Label-Based Indexing

`.loc[]` is used to access rows and columns using their **labels**.

```python
df.loc[0]
df.loc[0:2]
df.loc[0:2, ["Name", "Marks"]]
df.loc[3, "City"]
```

### 2. `.iloc[]` – Position-Based Indexing

`.iloc[]` accesses data using its **integer position**, starting from `0`.

```python
df.iloc[0]
df.iloc[0:2]
df.iloc[0:2, [0, 2]]
df.iloc[3, 3]
```

**Remember:**

* `.loc` → labels
* `.iloc` → positions

### 3. Conditional Filtering

I learned how to filter rows based on conditions.

```python
df[df["Marks"] > 80]
df[df["Age"] < 20]
df[df["City"] == "Mumbai"]
```

For multiple conditions:

```python
df[(df["Marks"] >= 80) & (df["Marks"] <= 90)]
```

`&` is used for **AND** conditions.

### 4. Updating Data Using `.loc`

`.loc` can also be used to modify specific values.

```python
df.loc[0, "Marks"] = 90
df.loc[1, "City"] = "Mumbai"
```

It can also update multiple rows conditionally:

```python
df.loc[df["Marks"] < 80, "Marks"] = df["Marks"] + 5
```

### 5. Creating a New Column with NumPy

I used NumPy together with Pandas to create a `Result` column.

```python
df["Result"] = np.where(
    df["Marks"] >= 50,
    "PASS",
    "FAIL"
)
```

This showed how **NumPy can handle the condition while Pandas stores the result in the DataFrame**.

### 6. Creating Multiple Categories with `np.select()`

I also used multiple conditions to create a `Grade` column.

```python
conditions = [
    df["Marks"] >= 90,
    df["Marks"] >= 80,
    df["Marks"] >= 70,
    df["Marks"] >= 60
]

choices = ["O", "A", "B", "C"]

df["Grade"] = np.select(
    conditions,
    choices,
    default="D"
)
```

`np.select()` checks the conditions in order and assigns the corresponding choice.

## Key Learning

Today's important takeaway was seeing **NumPy and Pandas working together**:

> **Pandas → manages and manipulates the DataFrame**
> **NumPy → helps perform efficient conditional operations**

This combination is especially useful for **data analysis and later Machine Learning preprocessing**.

**Pandas:** `.loc`, `.iloc`, filtering, updating values, creating columns
**NumPy:** `np.where()`, `np.select()`
**Main Skill:** Combining NumPy + Pandas for DataFrame manipulation.