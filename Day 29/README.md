# Day 29 - NumPy Slicing, View and Copy

## Topics Covered

- Array slicing
- Negative indexing
- Step slicing
- Reversing arrays
- 2D array slicing
- Row and column selection
- View
- Copy

## Array Slicing

Slicing is used to select a part of an array.

```python
numbers[:3]
numbers[-3:]
numbers[2:5]
numbers[::2]
numbers[::-1]
```
Examples
```python
numbers[:3]
numbers[-3:]
numbers[2:5]
numbers[::2]
numbers[::-1]
```
- start - starting position
- stop - ending position
- step - number of positions to move

### Step Slicing
Step slicing allows elements to be selected at a particular interval.

```python
numbers[::2]
```
This selects every second element.

## Negative Indexing

Negative indexing is used to access elements from the end of an array.
```python
numbers[-3:]
```
This selects the last three elements.

### Reversing an Array
An array can be reversed using a negative step.
```python
numbers[::-1]
```

## 2D Array Indexing and Slicing

NumPy also allows rows, columns and individual elements to be accessed from a 2D array.

### Selecting a Row
```python
matrix[0]
```
### Selecting a Column
```python
matrix[:, 1]
```
### Selecting Multiple Rows
```python
matrix[:2]
```
### Selecting Multiple Columns
```python
matrix[:, 1:]
```
### Selecting a Specific Element
```python
matrix[1, 1]
```

## NumPy View
A view is a portion of an array that refers to the original array data.

```python
view = numbers[1:4]
view[0] = 999
```
Changing the view can also change the original array.

## NumPy Copy
The copy() method creates a separate copy of an array.
```python
copy = numbers[1:4].copy()
copy[0] = 111
```
Changing the copy does not change the original array.

## Difference Between View and Copy
| View	| Copy |
|-------|------|
| Refers to original data | Creates separate data |
| Changes can affect original array	| Changes do not affect original array |
| Created through slicing | Created using copy() |
| Uses less additional memory | Uses additional memory |

## Practice
```python
print(f"First four: {numbers[:4]}")
print(f"Odd positions: {numbers[::2]}")
print(f"Last column: {matrix[:, -1]}")
```

## Skills Gained
- NumPy Array Slicing
- Negative Indexing
- Step Slicing
- Array Reversing
- 2D Array Indexing
- Row and Column Selection
- Matrix Slicing
- NumPy Views
- NumPy Copies

## Outcome

Today I learned how to access and manipulate specific parts of NumPy arrays using slicing and indexing. I also learned how to work with rows and columns in 2D arrays and understood the difference between NumPy views and copies. This helped me understand how NumPy handles array data and memory when modifying sliced arrays.