# Day 76 — Matrix Adjoint

Today I extended my matrix program to calculate the **adjoint of 2×2 and 3×3 matrices using NumPy**.

## Topics Covered

* Matrix input using NumPy
* 2×2 matrix adjoint
* 3×3 matrix minors
* Cofactor calculation
* Cofactor matrix
* Matrix transpose
* Adjoint of a matrix
* Conditional handling using `if` and `elif`

## 2×2 Matrix

For:

```text
[a  b]
[c  d]
```

The adjoint is:

```text
[d  -b]
[-c  a]
```

## 3×3 Matrix

For a 3×3 matrix, the program:

```text
Matrix
  ↓
Find Minors
  ↓
Calculate Cofactors
  ↓
Cofactor Matrix
  ↓
Transpose
  ↓
Adjoint Matrix
```
