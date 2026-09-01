# Day 48 - Handling Missing Data in Pandas

Today I learned how to identify, count, remove, and replace missing values in a Pandas DataFrame.

Missing values are common when working with real-world datasets. In Pandas, missing numerical values can be represented using `NaN`.

## Topics Covered

* `np.nan`
* `isna()`
* Counting missing values
* `dropna()`
* `fillna()`
* Filling missing values with a specific value
* Filling missing values in a specific column
* Filling missing values using the average
* `copy()`

## What I Learned

### 1. Creating Missing Values

I created a DataFrame containing missing values using:

```python
np.nan
```

This allowed me to practice different methods for handling incomplete data.

### 2. Detecting Missing Values

I used:

```python
df.isna()
```

to check which values in the DataFrame were missing.

The method returns:

* `True` for missing values
* `False` for available values

### 3. Counting Missing Values

I used:

```python
df.isna().sum()
```

to count the number of missing values in each column.

The DataFrame contained:

* Age → 2 missing values
* Marks → 2 missing values
* City → 1 missing value

### 4. Removing Missing Values

I used:

```python
df.dropna()
```

to remove rows containing missing values.

Only rows without any missing values remained in the resulting DataFrame.

### 5. Filling Missing Values

I used:

```python
df.fillna("Not Available")
```

to replace all missing values with a specific value.

### 6. Filling Missing Values in a Specific Column

I filled the missing values in the `Marks` column with `0`.

```python
marks_filled_df["Marks"] = marks_filled_df["Marks"].fillna(0)
```

### 7. Filling Missing Ages with the Average

I calculated the average of the available age values and used it to fill the missing values.

```python
average_age_df["Age"] = average_age_df["Age"].fillna(
    average_age_df["Age"].mean()
)
```

The average age was `20`, so the missing age values were replaced with `20.0`.

### 8. Using `copy()`

I used:

```python
df.copy()
```

before making changes to a DataFrame.

This allowed me to create a separate copy and perform modifications without changing the original DataFrame.

## Important Functions

| Function       | Purpose                                           |
| -------------- | ------------------------------------------------- |
| `isna()`       | Detects missing values                            |
| `isna().sum()` | Counts missing values                             |
| `dropna()`     | Removes rows or columns containing missing values |
| `fillna()`     | Replaces missing values                           |
| `mean()`       | Calculates the average value                      |
| `copy()`       | Creates a copy of a DataFrame                     |

## Practical Work

Today I performed the following operations:

* Created a DataFrame containing missing values
* Detected missing values
* Counted missing values in each column
* Removed rows containing missing values
* Filled all missing values with `"Not Available"`
* Filled missing marks with `0`
* Filled missing ages with the average age
* Used `.copy()` to preserve the original DataFrame

## Key Takeaway

Today I learned that missing data can be handled in different ways depending on the situation.

I can:

* Detect missing values using `isna()`
* Count missing values using `isna().sum()`
* Remove missing data using `dropna()`
* Replace missing values using `fillna()`

I also learned that numerical missing values can be replaced using calculated values such as the column average.