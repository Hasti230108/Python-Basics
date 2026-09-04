# Day 51 - Student Performance Analyzer 

This project combines **Object-Oriented Programming (OOP)**, **NumPy**, and **Pandas** to analyze student marks and performance.

## Concepts Used

* Classes and Objects
* `__init__()` constructor
* Instance variables
* NumPy arrays
* Pandas DataFrames
* `np.mean()`
* `np.max()`
* `np.min()`
* Nested `np.where()`
* Boolean indexing
* Loops

## Features

### 1. Display Student Data

The `show_students()` method creates and displays a Pandas DataFrame containing:

* Student Name
* Marks

### 2. Calculate Average Marks

The `average_marks()` method uses:

```python
np.mean()
```

to calculate the average marks of all students.

### 3. Find Highest Marks

The `highest_marks()` method uses:

```python
np.max()
```

to find the highest mark.

### 4. Find Lowest Marks

The `lowest_marks()` method uses:

```python
np.min()
```

to find the lowest mark.

### 5. Student Performance Classification

The `performance_level()` method uses nested `np.where()` to classify students based on their marks.

| Marks       | Performance Level |
| ----------- | ----------------- |
| 90 or above | Excellent         |
| 75 to 89    | Good              |
| Below 75    | Needs Improvement |

### 6. Find Above-Average Students

The `above_average_students()` method:

1. Calculates the class average.
2. Creates a Boolean condition using marks greater than the average.
3. Uses NumPy Boolean indexing to select students who scored above average.
4. Displays their names.

## Student Data Used

| Name    | Marks |
| ------- | ----: |
| Hasti   |    86 |
| Tinker  |    92 |
| Amisha  |    68 |
| Sahima  |    88 |
| Tanisha |    74 |
| Mridula |    96 |

## Results

* Average Marks: **84.0**
* Highest Marks: **96**
* Lowest Marks: **68**

### Students Above Average

* Hasti
* Tinker
* Sahima
* Mridula

## Key Learning

This project helped me understand how different Python libraries and concepts can work together:

* **OOP** organizes the program using classes and methods.
* **NumPy** performs numerical calculations and Boolean filtering.
* **Pandas** displays structured student data using DataFrames.