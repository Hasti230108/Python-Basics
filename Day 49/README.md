# Day 49 - OOP + NumPy + Pandas Integration

Today I combined concepts from **Object-Oriented Programming (OOP)**, **NumPy**, and **Pandas** to create a simple student marks analysis program.

## Concepts Covered

* Classes and Objects
* `__init__()` constructor
* Instance variables using `self`
* Class methods
* NumPy arrays using `np.array()`
* Numerical operations using NumPy
* Pandas DataFrames
* Data filtering
* Conditional values using `np.where()`

## What I Built

I created a class called `StudentAnalyzer` to analyze student marks.

The program stores student names and marks, converts the marks into a NumPy array, and uses Pandas to display and analyze the student data.

## Features

### 1. Display Student Data

The `show_data()` method creates and displays a Pandas DataFrame containing:

* Student Names
* Student Marks

### 2. Calculate Average Marks

Used NumPy's `np.mean()` to calculate the average marks of all students.

### 3. Find Highest Marks

Used `np.max()` to find the highest mark.

### 4. Find Lowest Marks

Used `np.min()` to find the lowest mark.

### 5. Find Students Above Average

The program calculates the average marks and uses Pandas filtering to display students who scored above the average.

### 6. Add Pass/Fail Result

Used `np.where()` to create a new `Result` column.

Students with marks greater than or equal to **80** are marked as **Pass**, while students below 80 are marked as **Fail**.

## Libraries Used

* NumPy
* Pandas

## Key Takeaway

Today I practiced combining **OOP, NumPy, and Pandas in a single program**.

This helped me understand how:

* OOP can organize a program using classes and methods.
* NumPy can perform numerical calculations efficiently.
* Pandas can store, display, and filter tabular data.
* `np.where()` can assign values based on conditions.

## Output Summary

The program successfully:

* Displayed student data.
* Calculated average, highest, and lowest marks.
* Identified students scoring above average.
* Added a Pass/Fail result column.