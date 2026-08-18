# Day 34 - NumPy Reshaping and Combining Arrays

## Topics Covered

- Array Shape
- `reshape()`
- `flatten()`
- `ravel()`
- Transpose
- `concatenate()`
- `vstack()`
- `hstack()`
- Combining Arrays using `axis`

## Array Shape

The `shape` property shows the size of an array along each axis.

```python
numbers.shape
````

For a 1D array containing 6 elements:

```text
(6,)
```

## Reshape

`reshape()` changes the shape of an array without changing its data. 

```python
reshaped = numbers.reshape(2, 3)
```

Example:

```text
[1 2 3 4 5 6]
```

becomes:

```text
[[1 2 3]
 [4 5 6]]
```

## Flatten

`flatten()` converts a multidimensional array into a one-dimensional array and returns a copy.

```python
reshaped.flatten()
```

Output:

```text
[1 2 3 4 5 6]
```

## Ravel

`ravel()` also returns a flattened 1D array. It may return a view instead of making a copy when possible.

```python
reshaped.ravel()
```

## Transpose

Transpose changes rows into columns and columns into rows.

```python
reshaped.T
```

Example:

```text
[[1 2 3]
 [4 5 6]]
```

becomes:

```text
[[1 4]
 [2 5]
 [3 6]]
```

## Concatenate

`np.concatenate()` joins arrays along an existing axis. 

```python
np.concatenate((a, b))
```

Output:

```text
[1 2 3 4 5 6]
```

For 2D arrays, the `axis` controls the direction of joining.

```python
np.concatenate((matrix_a, matrix_b), axis=0)
```

joins rows.

```python
np.concatenate((matrix_a, matrix_b), axis=1)
```

joins columns.

## Vertical Stack

`np.vstack()` stacks arrays vertically.

```python
np.vstack((matrix_a, matrix_b))
```

Output:

```text
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
```

## Horizontal Stack

`np.hstack()` stacks arrays horizontally.

```python
np.hstack((matrix_a, matrix_b))
```

Output:

```text
[[1 2 5 6]
 [3 4 7 8]]
```

## Axis

```text
axis=0 → combine along rows
axis=1 → combine along columns
```

## Difference Between Operations

| Operation       | Purpose                             |
| --------------- | ----------------------------------- |
| `reshape()`     | Changes array shape                 |
| `flatten()`     | Converts to 1D copy                 |
| `ravel()`       | Converts to 1D array                |
| `.T`            | Transposes array                    |
| `concatenate()` | Joins arrays along an existing axis |
| `vstack()`      | Stacks vertically                   |
| `hstack()`      | Stacks horizontally                 |

## Practice

```python
print(f"Reshaped:\n{numbers.reshape(2, 3)}")
print(f"Flattened: {reshaped.flatten()}")
print(f"Ravelled: {reshaped.ravel()}")
print(f"Transpose:\n{reshaped.T}")

print(f"Concatenate: {np.concatenate((a, b))}")
print(f"Vertical stack:\n{np.vstack((a, b))}")
print(f"Horizontal stack: {np.hstack((a, b))}")
```

## Skills Gained

- Understanding Array Shape
- Reshaping Arrays
- Flattening Arrays
- Raveling Arrays
- Transposing Arrays
- Concatenating Arrays
- Vertical and Horizontal Stacking
- Using Axes for Array Operations

## Outcome
Today I learned how to change the shape of NumPy arrays and combine multiple arrays. I practiced `reshape()`, `flatten()`, `ravel()`, transpose, `concatenate()`, `vstack()` and `hstack()`. This helped me understand how NumPy arrays can be reorganized and combined for numerical and data-processing tasks.