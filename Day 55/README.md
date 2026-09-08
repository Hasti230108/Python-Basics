# Day 55 — Pandas Revision

Today I continued revising important **Pandas concepts** from the previous days.

The goal of Day 55 was to practice the concepts again and maintain consistency without starting a new topic.

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
* Aggregation using `mean()`, `sum()`, and `size()`
* Sorting using `sort_values()`
* Ranking using `rank()`
* Top-N analysis using `nlargest()`
* Bottom-N analysis using `nsmallest()`

## 1. DataFrame Creation

I created a Pandas DataFrame containing names, ages, and cities.

```python
df = pd.DataFrame({
    'Name': ['Hasti', 'Tinker', 'Himanshi', 'Rahul'],
    'Age': [18, 21, 20, 21],
    'City': ['Mumbai', 'Dadar', 'Dadar', 'Mumbai']
})
```

## 2. Filtering

I revised filtering rows using conditions.

```python
df[df['Age'] > 19]
```

```python
df[df['City'] == 'Dadar']
```

## 3. Indexing

I revised selecting specific columns and rows.

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

I practiced creating and handling missing values using `np.nan`.

```python
df_missing.loc[2, 'Age'] = np.nan
df_missing.loc[4, 'City'] = np.nan
```

I checked missing values using:

```python
df_missing.isnull().sum()
```

I also revised:

```python
df_missing.dropna()
```

and:

```python
df_missing.fillna(0)
```

## 5. Combining DataFrames

I revised combining DataFrames using `pd.concat()`.

```python
pd.concat([df1, df2], ignore_index=True)
```

## 6. Grouping and Aggregation

I revised grouping data by city and applying aggregation functions.

```python
df.groupby('City')['Age'].mean()
```

```python
df.groupby('City')['Age'].sum()
```

```python
df.groupby('City').size()
```

## 7. Sorting

I revised sorting a DataFrame by age.

```python
df.sort_values('Age')
```

For descending order:

```python
df.sort_values('Age', ascending=False)
```

## 8. Ranking

I revised ranking values using `rank()`.

```python
df['Age'].rank()
```

Tied values receive the average of their possible ranks.

## 9. Top-N Analysis

I revised finding the oldest and youngest people using:

```python
df.nlargest(3, 'Age')
```

```python
df.nsmallest(3, 'Age')
```

## Key Takeaways

> Revision helps strengthen previously learned concepts.

> Pandas provides useful functions for filtering, cleaning, combining, and analyzing data.

> `groupby()` and aggregation are useful for summarizing data.

> `sort_values()`, `rank()`, `nlargest()`, and `nsmallest()` are useful for ranking and comparison.