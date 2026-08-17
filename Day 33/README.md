# Day 33 - NumPy Matrix Operations

## Topics Covered

- Matrix Operations
- Element-wise Addition
- Element-wise Subtraction
- Element-wise Multiplication
- Dot Product
- Matrix Multiplication
- `np.matmul()`
- `@` Operator
- Matrix Transpose
- Diagonal Elements
- Matrix Trace

## Matrix Operations

NumPy arrays can be used to perform mathematical operations on matrices.

```python
matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])
```

## Element-wise Operations

Element-wise operations perform calculations between corresponding elements of two arrays.

### Addition
```python
matrix_a + matrix_b
```
Output:
```python
[[ 6  8]
 [10 12]]
```

### Subtraction
```python
matrix_a - matrix_b
```

### Multiplication
```python
matrix_a * matrix_b
```
Element-wise multiplication multiplies corresponding positions.

### Dot Product

The `np.dot()` function performs a dot product and can perform matrix multiplication for 2D arrays.
```python
np.dot(matrix_a, matrix_b)
```
Output:
```python
[[19 22]
 [43 50]]
```

### Matrix Multiplication

NumPy provides `np.matmul()` for matrix multiplication.
```python
np.matmul(matrix_a, matrix_b)
```
The `@` operator can also be used for matrix multiplication.
```python
matrix_a @ matrix_b
```
Both produce:
```python
[[19 22]
 [43 50]]
```
#### Important Difference
```python
matrix_a * matrix_b
```
→ Element-wise multiplication

```python
matrix_a @ matrix_b
```
→ Matrix multiplication

### Matrix Transpose

Transpose changes the rows of a matrix into columns and columns into rows. 
```python
matrix_a.T
```
Example:
```python
[[1 2]
 [3 4]]
```
becomes:
```python
[[1 3]
 [2 4]]
```

### Diagonal
`np.diag() ` is used to access the main diagonal of a matrix.```python
```python
np.diag(matrix_a)   
```
Output:
```
[1 4]
```

### Trace
The trace of a square matrix is the sum of its main diagonal elements. NumPy provides `np.trace()` for this operation. 
```python
np.trace(matrix_a)
```
For:
```
[[1 2]
 [3 4]]
```
the trace is:
```
1 + 4 = 5
```

## Practice
```python
print(f"Element-wise addition:\n{matrix_a + matrix_b}")
print(f"Element-wise subtraction:\n{matrix_a - matrix_b}")
print(f"Element-wise multiplication:\n{matrix_a * matrix_b}")

print(f"Dot Product:\n{np.dot(matrix_a, matrix_b)}")
print(f"Matrix Multiplication:\n{matrix_a @ matrix_b}")

print(f"Transpose:\n{matrix_a.T}")
print(f"Diagonal: {np.diag(matrix_a)}")
print(f"Trace: {np.trace(matrix_a)}")
```

## Skills Gained
- Matrix Operations
- Element-wise Operations
- Dot Product
- Matrix Multiplication
- Transpose
- Diagonal Extraction
- Matrix Trace

## Outcome
Today I learned how to perform basic matrix operations using NumPy. I practiced element-wise operations, dot product, matrix multiplication, transpose, diagonal extraction, and trace. These operations provide a foundation for understanding linear algebra concepts used in Data Science and AI/ML.