# Day 50 - Personal Expense Analyzer 

A simple Python mini-project that analyzes personal expenses using **Object-Oriented Programming (OOP)**, **NumPy**, and **Pandas**.

## Topics Covered

* Python Classes and Objects
* Constructors (`__init__`)
* Instance Variables
* Class Methods
* NumPy Arrays
* `np.sum()`
* `np.mean()`
* `np.max()`
* Pandas DataFrames
* Pandas `groupby()`
* NumPy `np.where()`
* Loops
* `zip()`

## Project Features

The `ExpenseAnalyzer` class performs the following operations:

### 1. Show Expenses

Displays all expense categories along with their respective amounts.

### 2. Calculate Total Expense

Uses NumPy's `np.sum()` to calculate the total amount spent.

### 3. Calculate Average Expense

Uses `np.mean()` to calculate the average expense.

### 4. Find Highest Expense

Uses `np.max()` to find the highest individual expense.

### 5. Category-wise Analysis

Uses Pandas `groupby()` to calculate the total expense for each category.

### 6. Expense Level Classification

Uses `np.where()` to classify expenses as:

* **High** → Amount is greater than or equal to 1000
* **Normal** → Amount is less than 1000

## Technologies Used

* Python
* NumPy
* Pandas

## Key Learning

This project helped me combine multiple Python concepts into one practical program.

I learned how to use:

* **OOP** to organize the program using a class and methods.
* **NumPy** for numerical calculations.
* **Pandas** for grouping and analyzing expense data.
* **`zip()`** to iterate through categories and expenses together.
* **`np.where()`** to classify expenses based on a condition.