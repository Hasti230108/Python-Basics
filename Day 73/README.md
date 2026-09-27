# Day 73 — Two Pointer Technique

Today I learned and practiced the **Two Pointer Technique** in Python.

## Topic Covered

- Two Pointer Technique
- Pair Sum Problem
- Sorting a list
- Using `left` and `right` pointers
- Finding two numbers whose sum matches a target

## How It Works

First, the list is sorted.

- `left` starts from the beginning.
- `right` starts from the end.
- If the sum is smaller than the target, move `left` forward.
- If the sum is larger than the target, move `right` backward.
- If the sum matches the target, the pair is found.

## Key Takeaway

The Two Pointer Technique can solve pair-based problems efficiently after sorting instead of checking every possible pair.