# Day 69 — DSA: Searching

Today I started DSA again and learned the basics of searching algorithms in Python.

## Topics Covered

- Linear Search
- Binary Search
- Searching using loops
- Sorted arrays/lists
- `left`, `right`, and `middle` pointers
- Found and not-found conditions
- Basic time complexity understanding

## 1. Linear Search

Linear Search checks each element one by one until the target is found.

```python
for num in range(length):
    if target == numbers[num]:
        print("Found at index:", num)
        break
````

It works even when the list is not sorted.

## 2. Binary Search

Binary Search repeatedly divides a **sorted list** into smaller sections.

```python
middle = (left + right) // 2
```

If the target is smaller than the middle element, the right side is reduced.

If the target is larger, the left side is increased.

```python
right = middle - 1
left = middle + 1
```

## Practical Work

* Took numbers from the user
* Searched for a target using Linear Search
* Sorted the list using NumPy
* Searched the sorted list using Binary Search
* Displayed the sorted index and position
* Handled the case when the number was not found

## Key Takeaways

* Linear Search checks elements one by one.
* Binary Search requires a sorted list.
* Binary Search is generally more efficient for large sorted datasets.
* `left`, `right`, and `middle` control the search range.