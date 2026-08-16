# Day 32 - NumPy Aggregation and Statistical Analysis

## Topics Covered
- NumPy Aggregation Functions
- `np.sum()`
- `np.mean()`
- `np.median()`
- `np.max()`
- `np.min()`
- Standard Deviation
- Variance
- Range
- Counting Array Elements
- `axis=0`
- `axis=1`
- Row-wise Operations
- Column-wise Operations
- `np.cumsum()`
- `np.cumprod()`

## Aggregation Functions
NumPy provides functions for calculating useful summary values from arrays.
```python
np.sum(marks)
np.mean(marks)
np.median(marks)
np.max(marks)
np.min(marks)
```
These functions can be used to analyze numerical data efficiently.

## Statistical Functions
### Mean
```python
np.mean(marks)
```
Calculates the average value of the array.
### Median
```python
np.median(marks)
```
Returns the middle value of the data after arranging the values in order.
### Standard Deviation
```python
np.std(marks)
```
Measures how spread out the values are from the mean.
### Variance
```python
np.var(marks)
```
Measures the squared variation of values from the mean.

## Range
The range represents the difference between the maximum and minimum values.
```python
np.max(marks) - np.min(marks)
```
## Counting Elements
The number of elements can be obtained using:
```python
marks.size
```
Conditional elements can be counted using:
```python
np.count_nonzero(marks >= 40)
```

## Axis Operations
NumPy allows aggregation operations to be performed along specific axes.
```python
np.sum(matrix, axis=1)
```
Performs the operation row-wise.
```python
np.sum(matrix, axis=0)
```
Performs the operation column-wise.
### Important
axis=0 → column-wise
axis=1 → row-wise

### Row-wise Operations
```python
np.sum(matrix, axis=1)
np.mean(matrix, axis=1)
np.max(matrix, axis=1)
np.min(matrix, axis=1)
```
### Column-wise Operations
```python
np.sum(matrix, axis=0)
np.mean(matrix, axis=0)
np.max(matrix, axis=0)
np.min(matrix, axis=0)
```

## Cumulative Sum
`np.cumsum()` calculates the cumulative sum of array elements. Each value contains the total accumulated up to that position.
```python
np.cumsum(marks)
```

## Cumulative Product
`np.cumprod()` calculates the cumulative product of array elements.
```python
np.cumprod(marks)
```
Each value is the product of all previous values up to that position.

## Practice
```python
print(f"Sum: {np.sum(marks)}")
print(f"Mean: {np.mean(marks)}")
print(f"Median: {np.median(marks)}")
print(f"Maximum: {np.max(marks)}")
print(f"Minimum: {np.min(marks)}")

print(f"Row totals: {np.sum(matrix, axis=1)}")
print(f"Column totals: {np.sum(matrix, axis=0)}")

print(f"Cumulative sum: {np.cumsum(marks)}")
print(f"Cumulative product: {np.cumprod(marks)}")
```

## Skills Gained
- NumPy Aggregation
- Statistical Analysis
- Mean and Median
- Standard Deviation and Variance
- Min, Max and Range
- Axis-based Operations
- Row and Column Analysis
- Cumulative Sum
- Cumulative Product

## Outcome
Today I practiced NumPy aggregation and statistical analysis. I learned how to calculate summary statistics, perform row-wise and column-wise operations using axes, and work with cumulative sum and cumulative product. This helped me understand how NumPy can be used to analyze numerical datasets efficiently.