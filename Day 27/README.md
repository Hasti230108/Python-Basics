# Day 27 - NumPy Joining & Splitting Arrays

## Topics Covered

* `np.concatenate()`
* `np.vstack()`
* `np.hstack()`
* `np.stack()`
* `np.split()`
* `np.vsplit()`
* `np.hsplit()`
* Joining 1D arrays
* Joining 2D arrays
* Splitting 1D arrays
* Splitting 2D arrays
* Using `axis` with `np.concatenate()`

## 1. Joining Arrays

Joining means combining two or more NumPy arrays into a larger array.

### `np.concatenate()`

`np.concatenate()` joins arrays along an existing axis. By default, it uses `axis=0`.

```python
np.concatenate((a, b))
```

For 1D arrays:

```text
[10 20 30] + [40 50 60]

[10 20 30 40 50 60]
```

For 2D arrays, `axis=0` joins rows:

```python
np.concatenate((marks_sem1, mark_sem2))
```

`axis=1` joins columns:

```python
np.concatenate((marks_sem1, mark_sem2), axis=1)
```

### `np.vstack()`

`vstack()` stacks arrays vertically, or row-wise.

```python
np.vstack((a, b))
```

Output:

```text
[[10 20 30]
 [40 50 60]]
```

### `np.hstack()`

`hstack()` stacks arrays horizontally, or column-wise for 2D arrays.

```python
np.hstack((a, b))
```

### `np.stack()`

`stack()` joins arrays along a **new axis**, unlike `concatenate()`, which joins along an existing axis.

```python
np.stack((a, b))
```

## 2. Splitting Arrays

Splitting means dividing one NumPy array into multiple smaller arrays.

### `np.split()`

Used to split an array into multiple equal-sized parts.

```python
numbers = np.array([10, 20, 30, 40, 50, 60])

np.split(numbers, 3)
```

Output:

```text
[array([10, 20]),
 array([30, 40]),
 array([50, 60])]
```

### `np.vsplit()`

`vsplit()` splits a 2D array vertically, meaning along rows.

```python
np.vsplit(marks, 2)
```

### `np.hsplit()`

`hsplit()` splits a 2D array horizontally, meaning along columns.

```python
np.hsplit(marks, 3)
```

## 3. Important Difference

| Function        | Purpose                             |
| --------------- | ----------------------------------- |
| `concatenate()` | Joins arrays along an existing axis |
| `vstack()`      | Joins arrays vertically             |
| `hstack()`      | Joins arrays horizontally           |
| `stack()`       | Joins arrays along a new axis       |
| `split()`       | Splits an array into equal parts    |
| `vsplit()`      | Splits vertically by rows           |
| `hsplit()`      | Splits horizontally by columns      |

## 4. Axis

For a 2D array:

```text
axis=0 → rows
axis=1 → columns
```

Example:

```python
np.concatenate((marks_sem1, mark_sem2), axis=0)
```

adds the rows.

```python
np.concatenate((marks_sem1, mark_sem2), axis=1)
```

adds the columns.

## 5. Practice Completed

During this day, I practiced:

* Creating 1D and 2D NumPy arrays
* Concatenating arrays
* Vertical stacking
* Horizontal stacking
* Stacking arrays using a new axis
* Splitting 1D arrays
* Splitting 2D arrays vertically
* Splitting 2D arrays horizontally
* Combining semester marks using `np.concatenate()`
* Using `axis=1` to concatenate 2D arrays column-wise

## Key Takeaway

`concatenate()` joins existing axes, while `stack()` creates a new axis.

For splitting:

```text
split   → general splitting
vsplit  → rows
hsplit  → columns
```

## Outcome
Completed the basics of **NumPy array joining and splitting** and gained more practical understanding of how NumPy arrays can be combined, stacked, divided, and manipulated using axes.