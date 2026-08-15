# Day 31 - NumPy Random Numbers and Random Sampling

## Topics Covered

- NumPy Random Number Generator
- `np.random.default_rng()`
- Generating Random Integers
- Generating Multiple Random Integers
- Generating Random Floats
- Generating Random Matrices
- Random Selection using `choice()`
- Selecting Multiple Random Values
- Random Seeds
- Reproducible Random Numbers

## NumPy Random Number Generator

NumPy provides tools for generating pseudo-random numbers and random samples. The recommended approach in modern NumPy is to create a `Generator` using `np.random.default_rng()` and then use its methods to generate random data. :contentReference[oaicite:0]{index=0}

```python
import numpy as np

rng = np.random.default_rng()
```

The `rng` object can then be used to generate different types of random data.

## Generating a Random Integer

The `integers()` method generates random integer values.
```python
rng.integers(1, 101)
```
This generates one random integer from 1 to 100.

The lower limit is included and the upper limit is excluded by default.

Example:
```python
print(rng.integers(1, 101))
```
Output may be:
`76`

The output can be different each time because the number is randomly generated.

## Generating Multiple Random Integers

The `size` parameter can be used to generate multiple random values.

```python
rng.integers(1, 101, size=5)
```
Example output:
`[100 17 44 42 69]`

This generates 5 random integers between 1 and 100.

## Generating Random Floats

The random() method generates random floating-point numbers between 0 and 1.

```python
rng.random(5)
```
Example output:
`[0.46251676 0.33188754 0.04176639 0.09879988 0.05347082]`

The generated values are in the range `[0, 1),` meaning `0` can occur but `1` is not included.

## Generating a Random Matrix

The `size` parameter can also be used to create arrays with a specific shape.

```python
rng.integers(1, 101, size=(3, 3))
```
This creates a 3 × 3 NumPy array containing random integers.

Example:
```
[[49 16 52]
 [17 81 63]
 [25 52 91]]
 ```

## Random Choice

The `choice()` method randomly selects values from an existing array.

```python
marks = np.array([45, 78, 92, 47, 96, 87, 83, 79])

rng.choice(marks)
```
This randomly selects one value from the marks array.

Example:
`92`

## Selecting Multiple Random Values
Multiple values can also be selected using the size parameter.

```python
rng.choice(marks, size=3)
```
Example:
```
[45 96 87]
```
By default, `choice()` allows replacement, so the same value can appear more than once.

## Random Seed

A seed can be provided when creating a random number generator.

```python
rng1 = np.random.default_rng(42)
```
A fixed seed makes the generated pseudo-random sequence reproducible.

Example:
```python
rng1 = np.random.default_rng(42)

print(rng1.integers(1, 101, size=5))
```
Output:
`[ 9 78 66 44 44]`

Creating another generator with the same seed produces the same sequence:

```python
rng2 = np.random.default_rng(42)

print(rng2.integers(1, 101, size=5))
```
Output:
`[ 9 78 66 44 44]`

## Random Numbers Without a Seed

When no seed is provided:
```python
rng = np.random.default_rng()
```
NumPy initializes the generator using operating-system entropy, so the generated sequence normally changes between runs.

Difference Between Random and Reproducible Random Numbers
| Without Seed | With Seed |
|--------------|-----------|
| Output can change between runs | Same seed gives reproducible sequence |
| Uses fresh entropy | Starts from a specified initial state |
| Useful for general random generation | Useful for experiments and reproducible results |

## Important Syntax
### Random Integer
```python
rng.integers(1, 101)
```
### Multiple Random Integers
```python
rng.integers(1, 101, size=5)
```
### Random Floats
```python
rng.random(5)
```
### Random Matrix
```python
rng.integers(1, 101, size=(3, 3))
```
### Random Choice
```python
rng.choice(marks)
```
### Multiple Random Choices
```python
rng.choice(marks, size=3)
```
### Reproducible Random Numbers
```python
rng = np.random.default_rng(42)
```
## Practice
```python
marks = np.array([45, 78, 92, 47, 96, 87, 83, 79])

print(f"Random choice: {rng.choice(marks)}")
print(f"Three random marks: {rng.choice(marks, size=3)}")
```

## Skills Gained
- NumPy Random Number Generation
- Using default_rng()
- Generating Random Integers
- Generating Random Floats
- Creating Random Arrays
- Creating Random Matrices
- Random Selection
- Using choice()
- Understanding size
- Using Random Seeds
- Creating Reproducible Random Sequences

## Outcome
Today I learned how to generate and work with random data using NumPy's random number generator. I learned how to generate random integers, random floating-point values, random arrays and matrices, and randomly select values from an existing array. I also learned how random seeds make pseudo-random results reproducible, which is important when working with experiments, simulations, data analysis and machine learning.