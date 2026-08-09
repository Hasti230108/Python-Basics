# Da 25 - NumPy Filtering

This file contains my practice with **Boolean Filtering and Conditional Selection in NumPy**.

## Topics Covered

* Boolean Conditions
* Boolean Indexing
* Filtering NumPy Arrays
* Multiple Conditions
* `np.where()`
* Conditional Value Modification
* Combining Filtering with NumPy Statistics

## Boolean Filtering

Boolean filtering allows us to select elements from a NumPy array based on a condition.

```python
marks[marks > 80]
```

The condition creates a Boolean mask, and NumPy returns the elements where the condition is `True`.

## Multiple Conditions

Multiple conditions can be combined using:

* `&` → AND
* `|` → OR

Example:

```python
marks[(marks >= 70) & (marks <= 90)]
```

This selects marks between 70 and 90.

## `np.where()`

`np.where()` selects values based on a condition. If the condition is `True`, it uses the first value; otherwise, it uses the second value.

Syntax:

```python
np.where(condition, value_if_true, value_if_false)
```

Example:

```python
result = np.where(marks >= 75, "Pass", "Needs Improvement")
```

## Practical Performed

### 1. Filtered marks above 80

```python
print(marks[marks > 80])
```

### 2. Filtered marks greater than or equal to 90

```python
print(marks[marks >= 90])
```

### 3. Filtered marks below 60

```python
print(marks[marks < 60])
```

### 4. Filtered marks between 70 and 90

```python
print(marks[(marks >= 70) & (marks <= 90)])
```

### 5. Checked for a specific mark

```python
print(marks[marks == 75])
```

### 6. Counted students scoring above 80

```python
above_80 = marks[marks > 80]
print(above_80.size)
```

### 7. Found the highest mark among students scoring above 80

```python
print(np.max(above_80))
```

### 8. Created Pass/Needs Improvement labels

```python
result = np.where(
    marks >= 75,
    "Pass",
    "Needs Improvement"
)
```

### 9. Added grace marks

Students scoring below 60 receive 5 additional marks.

```python
grace_marks = np.where(marks < 60, marks + 5, marks)
```

### 10. Filtered marks below 70

```python
below_70 = marks[marks < 70]
```

## Concepts Learned

* Boolean masks
* Conditional filtering
* Multiple Boolean conditions
* `&` operator for AND conditions
* NumPy Boolean indexing
* `np.where()`
* Conditional modification of array values
* Combining filtering with `np.max()` and other NumPy functions

## Outcome
Today I learned how to filter NumPy arrays using Boolean conditions and how to use `np.where()` for conditional selection and modification. I also practiced combining filtering with NumPy statistical functions.