# Day 35 - NumPy Broadcasting

## Topics Covered

- Broadcasting
- Scalar Broadcasting
- Array and Scalar Operations
- Row Broadcasting
- Column Broadcasting
- Broadcasting with Matrices
- Broadcasting with Real-World Data
- Using `np.minimum()`

## What is Broadcasting?

Broadcasting is a NumPy mechanism that allows operations between arrays with different but compatible shapes. NumPy automatically expands the smaller array conceptually so the operation can be performed element by element. 

## Scalar Broadcasting

A scalar value can be directly applied to every element of an array.

```python
numbers + 10
numbers - 5
numbers * 2
numbers / 10
````

Example:

```python
numbers = np.array([10, 20, 30, 40])

numbers + 10
```

Output:

```text
[20 30 40 50]
```

The value `10` is applied to every element.

## Broadcasting with a Matrix

A scalar can also be applied to every element of a 2D array.

```python
matrix + 10
```

Example:

```text
[[10 20 30]
 [40 50 60]
 [70 80 90]]
```

becomes:

```text
[[20 30 40]
 [50 60 70]
 [80 90 100]]
```

## Row Broadcasting

A 1D array can be added to every row of a matrix when their shapes are compatible.

```python
row = np.array([1, 2, 3])

matrix + row
```

Output:

```text
[[11 22 33]
 [41 52 63]
 [71 82 93]]
```

The row:

```text
[1 2 3]
```

is applied to each row of the matrix.

## Column Broadcasting

A column array can be applied to every column of a matrix.

```python
column = np.array([
    [1],
    [2],
    [3]
])

matrix + column
```

Output:

```text
[[11 21 31]
 [42 52 62]
 [73 83 93]]
```

Each value in the column is applied across its corresponding row.

## Broadcasting Rules

NumPy compares array dimensions starting from the rightmost dimension.

Two dimensions are compatible when:

* They are equal
* One of them is `1`

If the dimensions are not compatible, NumPy raises a `ValueError`.

Example:

```text
(3, 3) + (3,)
```

is compatible.

```text
(3, 3) + (2,)
```

is not compatible.

## Broadcasting with Marks

Broadcasting can be useful for real-world data processing.

```python
marks = np.array([
    [45, 60, 75],
    [68, 86, 73],
    [96, 84, 62]
])

bonus = np.array([5, 10, 5])

marks + bonus
```

The bonus is automatically applied to every row.

Output:

```text
[[ 50  70  80]
 [ 73  96  78]
 [101  94  67]]
```

## Limiting Values with np.minimum()

`np.minimum()` compares values element by element and returns the smaller value.

```python
np.minimum(marks + bonus, 100)
```

This can be used to make sure marks do not exceed 100.

Output:

```text
[[ 50  70  80]
 [ 73  96  78]
 [100  94  67]]
```

## Broadcasting Examples

```python
numbers + 10
```

```python
matrix + 10
```

```python
matrix + row
```

```python
matrix + column
```

```python
marks + bonus
```

## Difference Between Normal Operations and Broadcasting

| Normal Operation                                      | Broadcasting                                       |
| ----------------------------------------------------- | -------------------------------------------------- |
| Arrays usually need compatible shapes                 | Different compatible shapes can work               |
| Same-shaped arrays can operate element-wise           | Smaller arrays can be applied across larger arrays |
| Manual repetition may be required in other approaches | NumPy handles the expansion automatically          |

## Practice

```python
print(f"Add 10: {numbers + 10}")
print(f"Matrix + Row:\n{matrix + row}")
print(f"Matrix + Column:\n{matrix + column}")
print(f"Marks after bonus:\n{marks + bonus}")
print(f"Marks capped at 100:\n{np.minimum(marks + bonus, 100)}")
```

## Skills Gained

* Understanding NumPy Broadcasting
* Scalar Broadcasting
* Row Broadcasting
* Column Broadcasting
* Matrix Operations
* Working with Compatible Shapes
* Applying Operations to Data
* Using `np.minimum()`
* Vectorized Data Processing

## Outcome

Today I learned how NumPy broadcasting allows operations between arrays with compatible shapes without manually repeating data. I practiced scalar, row, and column broadcasting and applied broadcasting to a marks dataset. I also learned how `np.minimum()` can be used to limit values such as marks to a maximum of 100. This helped me understand how NumPy performs efficient vectorized operations on numerical data.