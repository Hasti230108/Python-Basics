# Day 36 - NumPy Linear Algebra

## Topics Covered

- Determinant — `np.linalg.det()`
- Matrix inverse — `np.linalg.inv()`
- Matrix rank — `np.linalg.matrix_rank()`
- Solving linear equations — `np.linalg.solve()`
- Eigenvalues and eigenvectors — `np.linalg.eig()`

## Key Functions

```python
np.linalg.det(matrix)
np.linalg.inv(matrix)
np.linalg.matrix_rank(matrix)
np.linalg.solve(a, b)
np.linalg.eig(matrix)
```

NumPy's `numpy.linalg` module provides these standard linear-algebra operations.

## Practice

Used the matrix:
```python
matrix = np.array([
    [1, 2],
    [3, 4]
])
```

Also solved:
```text
x + 2y = 5
3x + 4y = 11
```

Result:

```text
x = 1
y = 2
```

## Outcome
Practiced basic NumPy linear algebra operations including matrix properties, solving equations, and finding eigenvalues and eigenvectors. `np.linalg.eig()` returns eigenvalues together with their corresponding right eigenvectors.