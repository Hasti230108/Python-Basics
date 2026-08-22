# Day 38 – NumPy Conditional Operations

## Topic

**NumPy Conditional Operations**
Today I learned how to use NumPy for making decisions and filtering data based on conditions. These operations are useful for working with datasets, especially when we need to select, count, replace, or limit values.

## Learned

### 1. `np.where()`

`np.where()` selects one value when a condition is `True` and another when it is `False`.

```python
result = np.where(marks >= 50, "Pass", "Fail")
```

Example:

```text
Marks: 86 94 73 46 84 61 55 84
Result: Pass Pass Pass Fail Pass Pass Pass Pass
```

### 2. Boolean Filtering

NumPy allows us to directly filter an array using a condition.

```python
marks[marks >= 80]
```

This returns:

```text
[86 94 84 84]
```

Multiple conditions can be combined using `&`:

```python
marks[(marks >= 50) & (marks <= 80)]
```

Result:

```text
[73 61 55]
```

### 3. `np.select()`

`np.select()` allows multiple conditions and corresponding choices. NumPy uses the **first matching condition** when multiple conditions are true.

```python
conditions = [
    marks >= 90,
    marks >= 70,
    marks >= 50,
    marks >= 40
]

choices = ["A", "B", "C", "D"]

grades = np.select(conditions, choices, default="F")
```

This can be used for assigning grades or categories.

### 4. `np.minimum()`

`np.minimum()` compares values element-by-element and is useful for setting an upper limit.

```python
np.minimum(marks + bonus, 100)
```

For example:

```text
101 → 100
```

So marks cannot exceed 100.

### 5. `np.clip()`

`np.clip()` keeps values inside a specified minimum and maximum range. Values below the minimum are raised to the minimum, while values above the maximum are reduced to the maximum.

```python
clipped_marks = np.clip(marks, 40, 90)
```

Example:

```text
94 → 90
```

### 6. Counting Values with `np.sum()`

A condition produces `True` and `False` values, which NumPy can use for counting.

```python
np.sum(marks >= 50)
```

Result:

```text
7
```

So, **7 students passed**.

### 7. `np.any()`

`np.any()` checks whether **at least one** element satisfies a condition.

```python
np.any(marks >= 90)
```

Result:

```text
True
```

Because at least one student scored 90 or above.

### 8. `np.all()`

`np.all()` checks whether **every** element satisfies a condition.

```python
np.all(marks >= 50)
```

Result:

```text
True
```

This means every mark is at least 50.


### 9. Conditional Replacement

We can modify only the elements that satisfy a condition.

```python
adjusted_marks = marks.copy()

adjusted_marks[adjusted_marks < 50] = 50
```

This changes every mark below 50 to 50.

Example:

```text
46 → 50
```

## 🧠 Important Concepts

| Function / Technique   | Purpose                                           |
| ---------------------- | ------------------------------------------------- |
| `np.where()`           | Choose between two results                        |
| Boolean filtering      | Select values based on conditions                 |
| `np.select()`          | Apply multiple conditions                         |
| `np.minimum()`         | Set an upper limit                                |
| `np.maximum()`         | Set a lower limit                                 |
| `np.clip()`            | Keep values within a range                        |
| `np.sum(condition)`    | Count values satisfying a condition               |
| `np.any()`             | Check if at least one value satisfies a condition |
| `np.all()`             | Check if every value satisfies a condition        |
| Conditional assignment | Replace values satisfying a condition             |

## Outcome
Today I learned how NumPy can be used not just for calculations, but also for **decision-making, filtering, counting, categorizing, and modifying array data**.

These operations will be especially useful later when working with **Pandas, data cleaning, preprocessing, and Machine Learning datasets**.