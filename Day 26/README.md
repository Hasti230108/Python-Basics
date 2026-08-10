# Day 26 - NumPy Sorting and Searching

## Topics Covered

* Sorting NumPy arrays
* Ascending order
* Descending order
* Finding maximum and minimum values
* Finding the positions of maximum and minimum values
* Finding positions using `np.where()`
* Finding the second-highest value
* Sorting indices using `np.argsort()`

## Introduction

In Day 26, I continued working with NumPy arrays and learned how to **sort arrays and find the positions of specific values**.

I practiced using NumPy's sorting and searching functions to analyze marks and scores efficiently.

## Functions Learned

### 1. `np.sort()`

Sorts an array in ascending order and returns a sorted copy.

```python
np.sort(marks)
```

### 2. Descending Order

A sorted array can be reversed using slicing:

```python
np.sort(marks)[::-1]
```

### 3. `np.argmax()`

Returns the **index of the maximum value**.

```python
np.argmax(marks)
```

### 4. `np.argmin()`

Returns the **index of the minimum value**.

```python
np.argmin(marks)
```

### 5. `np.where()`

Finds the positions where a condition is true.

```python
np.where(marks > 80)
```

It can also be used to find a particular value:

```python
np.where(marks == 64)
```

### 6. `np.argsort()`

Returns the **indices that would sort an array**.

```python
scores = np.array([45, 88, 72, 95, 61, 79])

print(np.argsort(scores))
```

Output:

```text
[0 4 2 5 1 3]
```

This means the original elements should be taken in the order of indices `0, 4, 2, 5, 1, 3` to produce the sorted array.

## Practical Performed

### 1. Created a Marks Array

```python
marks = np.array([58, 98, 68, 64, 86, 92])
```

### 2. Sorted Marks in Ascending Order

```python
print(np.sort(marks))
```

### 3. Sorted Marks in Descending Order

```python
print(np.sort(marks)[::-1])
```

### 4. Found Highest and Lowest Marks

```python
print(np.max(marks))
print(np.min(marks))
```

### 5. Found Positions of Highest and Lowest Marks

```python
print(np.argmax(marks))
print(np.argmin(marks))
```

### 6. Found Positions Above 80

```python
print(np.where(marks > 80))
```

### 7. Found Position of 64

```python
print(np.where(marks == 64))
```

### 8. Found Position of 92

```python
print(np.where(marks == 92))
```

### 9. Found Positions Below 70

```python
print(np.where(marks < 70))
```

### 10. Found the Second-Highest Mark

```python
print(np.sort(marks)[-2])
```

### 11. Found Positions of Marks Greater Than or Equal to 90

```python
print(np.where(marks >= 90))
```

### 12. Created a Second Scores Array

```python
scores = np.array([45, 88, 72, 95, 61, 79])
```

### 13. Sorted the Scores

```python
print(np.sort(scores))
```

### 14. Found Sorting Indices

```python
print(np.argsort(scores))
```

## Important Difference

| Function       | Purpose                                   |
| -------------- | ----------------------------------------- |
| `np.max()`     | Returns maximum value                     |
| `np.min()`     | Returns minimum value                     |
| `np.argmax()`  | Returns index of maximum value            |
| `np.argmin()`  | Returns index of minimum value            |
| `np.sort()`    | Returns sorted values                     |
| `np.argsort()` | Returns indices that sort the array       |
| `np.where()`   | Finds positions where a condition is true |

## Concepts Learned

* Array sorting
* Array indexing
* Searching for values
* Searching using conditions
* Maximum and minimum positions
* Indirect sorting
* Using slicing for descending order

## Outcome
Today I learned how to sort NumPy arrays and search for values and their positions. I practiced `np.sort()`, `np.argmax()`, `np.argmin()`, `np.where()`, and `np.argsort()` using marks and scores. I also learned the important difference between sorting values and getting the indices that would sort an array.