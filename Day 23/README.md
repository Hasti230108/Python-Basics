# Day 23 - NumPy Arrays

## Topics Covered

* 2D NumPy Arrays
* Array Dimensions and Shape
* 2D Array Indexing
* `zeros()`
* `ones()`
* `full()`
* `arange()`
* `linspace()`
* `reshape()`

## Key Concepts

* `ndim` — number of dimensions
* `shape` — dimensions of an array
* `size` — total number of elements
* `arange()` — creates evenly spaced values using a step size
* `linspace()` — creates a specified number of evenly spaced values
* `reshape()` — changes the shape of an array without changing its data

## Examples

```python
import numpy as np

marks = np.array([
    [58, 98, 68],
    [64, 86, 92]
])

print(marks.ndim)
print(marks.shape)
print(marks.size)
print(marks[1][2])

zeros = np.zeros((2, 4))
ones = np.ones((2, 4))
full = np.full((2, 4), 9)

array = np.arange(1, 13)
new_array = array.reshape(3, 4)

print(new_array)
```

## Outcome
Learned how to create and work with 2D NumPy arrays and use common array-creation and reshaping functions.