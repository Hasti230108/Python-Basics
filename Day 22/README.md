# Day 22 - NumPy Basics

## Topics Covered

- Introduction to NumPy
- Importing NumPy
- Creating NumPy Arrays
- Difference between Python List and NumPy Array
- Array Properties
- Indexing
- Slicing
- Scalar Arithmetic
- Array Arithmetic
- Vectorized Operations

## What is NumPy?

NumPy (Numerical Python) is a Python library used for numerical computing. It provides fast and memory-efficient multidimensional arrays and mathematical operations.

## Why NumPy?

- Faster than Python Lists
- Uses Less Memory
- Supports Vectorized Operations
- Widely Used in AI, Machine Learning and Data Science

## Concepts Learned

### Importing NumPy

```python
import numpy as np
```

### Creating an Array

```python
numbers = [10, 20, 30, 40, 50]
array = np.array(numbers)
```

### Array Properties

- `ndim`
- `shape`
- `size`
- `dtype`

### Indexing

```python
array[0]
array[-1]
```

### Slicing

```python
array[0:5]
array[0:3]
```

### Scalar Arithmetic

```python
array + 10
array - 5
array * 2
array / 2
```

### Array Arithmetic

```python
array + array2
array - array2
array * array2
array / array2
```

## Difference Between Python List and NumPy Array

| Python List | NumPy Array |
|-------------|-------------|
| Slower | Faster |
| More Memory | Less Memory |
| General Purpose | Numerical Computing |
| No Vectorization | Supports Vectorization |

## Files

```
Day 22
│
├── numpy_intro.py
└── README.md
```

## Skills Gained

- NumPy Installation
- Importing Libraries
- Creating Arrays
- Array Properties
- Indexing
- Slicing
- Mathematical Operations
- Vectorized Computation

## Outcome
Today I started learning NumPy, the first Python library used in Artificial Intelligence and Machine Learning. I learned how to create NumPy arrays, inspect their properties, perform indexing and slicing, and execute mathematical operations using vectorization. This marks the beginning of my AI/ML library journey.