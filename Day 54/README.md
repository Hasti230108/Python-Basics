# Day 54 — Pandas Revision

Today I revised important **Pandas concepts** learned in the previous days.

Instead of learning a new topic, I practiced DataFrame creation, filtering, indexing, missing data handling, combining DataFrames, grouping, aggregation, ranking, and Top-N analysis.

## Topics Revised

* Creating DataFrames
* Filtering DataFrames
* Column and row indexing
* `head()` and `tail()`
* Handling missing values
* `isnull()`
* `dropna()`
* `fillna()`
* Combining DataFrames using `concat()`
* Grouping using `groupby()`
* Aggregation using `mean()` and `sum()`
* Counting groups using `size()`
* Ranking using `rank()`
* Top-N analysis using `nlargest()`
* Bottom-N analysis using `nsmallest()`

## 1. Creating a DataFrame

I created a Pandas DataFrame containing information about people such as their name, age, and city.

```python
df = pd.DataFrame({
    'Name': ['Hasti', 'Tinker', 'Himanshi', 'Rahul'],
    'Age': [18, 21, 20, 21],
    'City': ['Mumbai', 'Dadar', 'Dadar', 'Mumbai']
})
```

## 2. Filtering Data

I practiced filtering rows based on conditions.

```python
df[df['Age'] > 19]
```

I also filtered rows based on a specific city.

```python
df[df['City'] == 'Dadar']
```

## 3. Indexing

I practiced selecting specific columns and viewing specific portions of a DataFrame.

```python
df[['Name', 'Age']]
```

```python
df.head(3)
```

```python
df.tail(3)
```

## 4. Missing Data Handling

I created a copy of the DataFrame and introduced missing values using `np.nan`.

```python
df_with_missing.loc[2, 'Age'] = np.nan
df_with_missing.loc[4, 'City'] = np.nan
```

I then checked the number of missing values:

```python
df_with_missing.isnull().sum()
```

I also practiced removing missing rows:

```python
df_with_missing.dropna()
```

And filling missing values:

```python
df_with_missing.fillna(0)
```

## 5. Combining DataFrames

I practiced combining multiple DataFrames using `pd.concat()`.

```python
pd.concat([df1, df2], ignore_index=True)
```

This combines the rows of the two DataFrames into one DataFrame.

## 6. Grouping and Aggregation

I revised `groupby()` with different aggregation operations.

### Mean Age by City

```python
df.groupby('City')['Age'].mean()
```

### Total Age by City

```python
df.groupby('City')['Age'].sum()
```

### Number of Entries per City

```python
df.groupby('City').size()
```

## 7. Ranking

I revised the `rank()` function to assign rankings based on age.

```python
df['Age'].rank()
```

When multiple values are equal, Pandas assigns them the average of their possible ranks.

## 8. Top-N and Bottom-N Analysis

I practiced finding the oldest individuals:

```python
df.nlargest(3, 'Age')
```

And the youngest individuals:

```python
df.nsmallest(3, 'Age')
```

## Revision Practice Completed

* Created a DataFrame
* Filtered rows using conditions
* Selected specific columns
* Viewed first and last rows
* Created missing values
* Counted missing values
* Removed missing rows
* Filled missing values
* Combined DataFrames
* Grouped data by city
* Calculated averages and sums
* Counted grouped records
* Ranked values
* Found Top 3 values
* Found Bottom 3 values

## Key Takeaways

> Pandas DataFrames make structured data easier to work with.

> Filtering allows specific rows to be selected based on conditions.

> `isnull()`, `dropna()`, and `fillna()` are useful for handling missing data.

> `groupby()` helps analyze data based on categories.

> `rank()`, `nlargest()`, and `nsmallest()` are useful for ranking and Top-N analysis.