# Day 28 - NumPy Array Manipulation

## Topics Covered

* `shape`
* `ndim`
* `size`
* `reshape()`
* `ravel()`
* `flatten()`
* Transpose using `.T`
* `axis=0`
* `axis=1`
* Row-wise calculations
* Column-wise calculations

## 1. Array Properties

NumPy arrays provide useful properties to understand their structure.

### `shape`

Returns the dimensions of the array.

```python
numbers.shape
```

For a 1D array:

```text
(6,)
```

For a 2D array with 2 rows and 3 columns:

```text
(2, 3)
```

### `ndim`

Returns the number of dimensions.

```python
numbers.ndim
```

### `size`

Returns the total number of elements.

```python
numbers.size
```

## 2. Reshape

`reshape()` changes the shape of an array without changing its data.

```python
matrix = numbers.reshape(2, 3)
```

Example:

```text
[10 20 30 40 50 60]

        ↓

[[10 20 30]
 [40 50 60]]
```

## 3. Ravel

`ravel()` converts an array into a flattened 1D array.

```python
matrix.ravel()
```

Output:

```text
[10 20 30 40 50 60]
```

## 4. Flatten

`flatten()` also converts an array into a 1D array.

```python
matrix.flatten()
```

Output:

```text
[10 20 30 40 50 60]
```

## 5. Transpose

The `.T` attribute transposes a 2D array.

Rows become columns and columns become rows.

```python
matrix.T
```

Example:

```text
[[10 20 30]
 [40 50 60]]
```

becomes:

```text
[[10 40]
 [20 50]
 [30 60]]
```

## 6. Axis

For a 2D array:

```text
axis=0 → column-wise operation
axis=1 → row-wise operation
```

### Row totals

```python
np.sum(marks, axis=1)
```

Output:

```text
[255 225 273]
```

### Column totals

```python
np.sum(marks, axis=0)
```

Output:

```text
[240 255 258]
```

### Row averages

```python
np.mean(marks, axis=1)
```

Output:

```text
[85. 75. 91.]
```

### Column averages

```python
np.mean(marks, axis=0)
```

Output:

```text
[80. 85. 86.]
```

## Important Difference

| Property / Function | Purpose                          |
| ------------------- | -------------------------------- |
| `shape`             | Returns array dimensions         |
| `ndim`              | Returns number of dimensions     |
| `size`              | Returns total number of elements |
| `reshape()`         | Changes array shape              |
| `ravel()`           | Flattens array into 1D           |
| `flatten()`         | Flattens array into 1D           |
| `.T`                | Transposes the array             |
| `axis=0`            | Performs operation column-wise   |
| `axis=1`            | Performs operation row-wise      |

## Practice Completed

* Checked array shape
* Checked number of dimensions
* Checked number of elements
* Reshaped a 1D array into a 2D array
* Flattened a 2D array using `ravel()`
* Flattened a 2D array using `flatten()`
* Transposed a 2D array
* Calculated row totals
* Calculated column totals
* Calculated row averages
* Calculated column averages
* Practiced `axis=0` and `axis=1`

## Key Takeaway

Array properties help understand the structure of NumPy arrays, while functions such as `reshape()`, `ravel()`, `flatten()`, and `.T` allow the array structure to be changed or viewed differently.

The most important concept from this day is understanding how `axis` affects calculations:

```text
axis=0 → columns
axis=1 → rows
```

## Outcome
Completed the basics of **NumPy array manipulation, reshaping, flattening, transposing, and axis-based calculations**.