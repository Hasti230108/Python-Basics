# Day 71 — Selection Sort

Today I practiced **Selection Sort** in Python.

Selection Sort repeatedly finds the smallest or largest element from the unsorted part of the list and places it in the correct position.

## Topics Covered

* Selection Sort
* Finding the minimum element
* Finding the maximum element
* Swapping elements
* Ascending order sorting
* Descending order sorting
* Nested loops
* In-place sorting

## Ascending Order

For ascending order, the smallest element is selected and placed at the beginning of the unsorted portion.

```python
if numbers[j] < numbers[min_index]:
    min_index = j
```

## Descending Order

For descending order, the largest element is selected and placed at the beginning of the unsorted portion.

```python
if numbers[j] > numbers[min_index]:
    min_index = j
```

## Key Takeaway

> Selection Sort finds the required element and swaps it into its correct position.

## Complexity

* Time Complexity: **O(n²)**
* Space Complexity: **O(1)**