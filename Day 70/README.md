# Day 70 — Bubble Sort

Today I learned and practiced **Bubble Sort** in Python.

Bubble Sort repeatedly compares adjacent elements and swaps them when they are in the wrong order.

## Topics Covered

* Bubble Sort
* Nested loops
* Comparing adjacent elements
* Swapping elements
* Ascending order
* Descending order
* In-place sorting

## 1. Ascending Order

```python
if numbers[j] > numbers[j + 1]:
    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
```

This places smaller elements toward the beginning of the list.

## 2. Descending Order

```python
if numbers[j] < numbers[j + 1]:
    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
```

This places larger elements toward the beginning of the list.

## Practical Task

The program:

* Takes numbers from the user
* Displays the original list
* Sorts the list in ascending order
* Sorts the list in descending order

## Key Takeaway

Bubble Sort works by repeatedly comparing **adjacent elements** and swapping them when necessary.