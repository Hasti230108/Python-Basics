# Day 30 - NumPy Boolean Indexing and Filtering

## Topics Covered

- Boolean indexing
- Array filtering
- Conditional filtering
- `np.where()`
- Multiple conditions
- `np.logical_and()`
- `np.logical_or()`
- Filtering NumPy arrays

## Boolean Indexing

Boolean indexing is used to filter elements of a NumPy array based on a condition.

```python
marks[marks > 80]
```
This returns only the values that satisfy the condition.

Example
```python
marks = np.array([45, 78, 92, 47, 96, 87, 83, 79])
print(marks[marks > 80])
```
Output:
```python
[92 96 87 83]
```
## Filtering Values
Different conditions can be used to filter array elements.

### Values Above 80
```python
marks[marks > 80]
```
### Values Below 60
```python
marks[marks < 60]
```
### Passed Marks
```python
marks[marks >= 40]
```
### Failed Marks
```python
marks[marks < 40]
```
## np.where()

```np.where()``` is used to find the positions or indices where a condition is true.
```python
np.where(marks > 80)
```
Example output:
```python
(array([2, 4, 5, 6]),)
```
This means the values above 80 are present at indices:
2, 4, 5, 6

## Filtering Between Two Values

Multiple conditions can be combined using &.
```python
marks[(marks >= 60) & (marks <= 80)]
```
This selects values that are:
- Greater than or equal to 60
- Less than or equal to 80
Both conditions must be true.

## np.logical_and()

```np.logical_and()``` is another way to combine two conditions where both conditions must be true.

```python
marks[np.logical_and(marks >= 60, marks <= 80)]
```
Output:
[78 79]

## np.logical_or()

```np.logical_or()``` is used when at least one of the conditions must be true.
```python
marks[np.logical_or(marks < 50, marks > 90)]
```
Output:
[45 92 47 96]

This selects values that are either:
- Below 50
- OR above 90

## Difference Between logical_and and logical_or
| np.logical_and() | np.logical_or() |
|------------------|-----------------|
| Both conditions must be true | At least one condition must be true |
| Works like AND | Works like OR |
| More restrictive filtering | Less restrictive filtering|

## Important Syntax
Using `&`
```python
array[(condition1) & (condition2)]
```
Using |
```python
array[(condition1) | (condition2)]
```
Using np.logical_and()
```python
array[np.logical_and(condition1, condition2)]
```
Using np.logical_or()
```python
array[np.logical_or(condition1, condition2)]
```

## Practice
```python
print(f"Above 80: {marks[marks > 80]}")
print(f"Below 60: {marks[marks < 60]}")
print(f"Passed marks: {marks[marks >= 40]}")
print(f"Failed marks: {marks[marks < 40]}")
```

## Skills Gained
- Boolean Indexing
- NumPy Array Filtering
- Conditional Selection
- Finding Array Positions
- Using np.where()
- Combining Conditions
- Using np.logical_and()
- Using np.logical_or()

## Outcome 
Today I revised and learned how to filter NumPy arrays using conditions and Boolean indexing. I learned how to find specific values using conditions, locate their positions using np.where(), and combine multiple conditions using &, np.logical_and() and np.logical_or(). This helped me understand how NumPy can efficiently select and analyze data based on conditions.