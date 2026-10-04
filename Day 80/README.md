# Day 80 — Demographic Data Analysis

Today I moved from DSA and matrix problems into **Data Analysis using Pandas and Matplotlib**.

I created a sample demographic dataset and practiced analyzing categorical and numerical data.

## Topics Covered

* Creating a DataFrame using Pandas
* `value_counts()`
* `describe()`
* Categorical data analysis
* Numerical data statistics
* Data visualization
* Bar charts using Matplotlib
* Basic dataset exploration

## 1. Creating the Dataset

A sample dataset was created containing:

* Gender
* Age
* Race

```python
df = pd.DataFrame(data)
```

## 2. Gender Distribution

I used `value_counts()` to count the number of people in each gender category.

```python
df["Gender"].value_counts()
```

## 3. Race Distribution

I also used `value_counts()` to analyze the distribution of race categories.

```python
df["Race"].value_counts()
```

## 4. Age Statistics

The `describe()` function was used to generate basic statistical information about the age column.

```python
df["Age"].describe()
```

It provides values such as:

* Count
* Mean
* Standard deviation
* Minimum
* Maximum
* Quartiles

## 5. Data Visualization

The race distribution was visualized using a bar chart:

```python
df["Race"].value_counts().plot(kind="bar")
```

Matplotlib was then used to add the chart title and axis labels.

## Key Takeaways

> `value_counts()` is useful for counting categorical values.

> `describe()` provides statistical information about numerical data.

> Pandas makes basic data analysis easier.

> Matplotlib can be used to visualize data.

> Data visualization makes patterns in datasets easier to understand.

## Libraries Used

```text
Pandas
Matplotlib
```
