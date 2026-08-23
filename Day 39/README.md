# Day 39 – NumPy Final Student Analysis

## Overview

Day 39 is the final NumPy practice day of my Python learning journey.

In this project, I combined the NumPy concepts I learned throughout the previous days into one **student marks analysis program**.

The program works with a NumPy array of student marks and performs sorting, statistical analysis, searching, conditional filtering, counting, bonus calculations, and percentage calculations.

NumPy provides an `ndarray` for multidimensional numerical data and supports operations such as indexing, sorting, statistical calculations, and Boolean filtering.

## Topics Practiced

* NumPy arrays
* Array sorting with `np.sort()`
* Maximum and minimum values
* Mean and standard deviation
* `np.argmax()` and `np.argmin()`
* Boolean indexing
* Conditional filtering
* Counting conditions with `np.sum()`
* Adding arrays element-wise
* `np.minimum()` for capping values
* Percentage calculation
* Student marks analysis

## Important Functions

### `np.sort()`

Sorts the marks into ascending order.

### `np.max()` / `np.min()`

Find the highest and lowest marks.

### `np.mean()`

Calculates the average.

### `np.std()`

Calculates standard deviation.

### `np.argmax()` / `np.argmin()`

Return the **index/position** of the maximum and minimum values.

### Boolean Indexing

Example:

```python
marks[marks >= 50]
```

This selects only the elements satisfying the condition. Boolean indexing is a useful way to filter NumPy arrays.

### `np.minimum()`

Used to prevent marks from exceeding 100 after adding bonus marks.

## Final Results

* Total students: **10**
* Students passed: **9**
* Students failed: **1**
* Pass percentage: **90%**
* Highest marks: **96**
* Lowest marks: **43**
* Average marks: **73.8**
* Highest-mark index: **6**
* Lowest-mark index: **7**
* Students scoring above 80: **4**

## Learning Outcome

After completing Day 39, I have completed my planned **NumPy fundamentals**.

I can now work with NumPy arrays for numerical calculations, filtering, statistics, conditional operations, shape manipulation, broadcasting, random data, linear algebra, and basic data analysis.

This gives me the NumPy foundation needed before moving into **Pandas and data analysis**.