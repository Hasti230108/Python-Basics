# Day 72 — Insertion Sort

Today I learned and practiced **Insertion Sort** in Python.

## Topics Covered

* Insertion Sort
* Sorting elements using `key`
* Using `while` loop for shifting elements
* Ascending order sorting
* Descending order sorting
* Understanding how elements are inserted into their correct position

## Insertion Sort

Insertion Sort builds the sorted list one element at a time.

For ascending order:

```python
for i in range(1, length):
    key = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j = j - 1

    numbers[j + 1] = key
```

For descending order, the comparison is reversed:

```python
while j >= 0 and numbers[j] < key:
```

genui{"learning_viz":{"type_id":"INSERTION_SORT"}}

## Practical Work

* Took numbers as input from the user
* Displayed the original list
* Sorted the list in ascending order
* Sorted the list in descending order
* Practiced shifting elements using a `while` loop

## Key Takeaway

> Insertion Sort takes one element at a time and inserts it into its correct position in the already sorted portion of the list.