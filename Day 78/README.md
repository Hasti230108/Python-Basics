# Day 78 — Eigenvalues & Eigenvectors

Today I learned how to calculate **eigenvalues and eigenvectors of a matrix using NumPy**.

### Topics Covered

* Creating matrices using NumPy
* Eigenvalues
* Eigenvectors
* `np.linalg.eig()`
* Matrix-vector multiplication
* Verifying eigenvalues and eigenvectors

## Main Concept

For a matrix `A`, an eigenvector `v` and eigenvalue `λ` satisfy:

```text
A × v = λ × v
```

The program calculates the eigenvalues and eigenvectors using:

```python
np.linalg.eig(A)
```

It then verifies the result by comparing `A × v` with `λ × v`.

## Example

```text
Matrix A:
[[4 1]
 [2 3]]

Eigenvalues:
[5. 2.]
```

The program also displays the corresponding eigenvectors and their verification.
