# Day 10 - Exception Handling in Python

## Topics Covered
- try
- except
- Multiple Exceptions
- ZeroDivisionError
- ValueError
- FileNotFoundError
- finally
- raise
- Custom Exceptions

## Programs

### 1. divide_by_zero.py
- Takes two numbers as input.
- Demonstrates how to handle `ZeroDivisionError` when dividing by zero.

### 2. multiple_exceptions.py
- Accepts user input.
- Handles:
  - `ValueError` for invalid input.
  - `ZeroDivisionError` for division by zero.

### 3. file_reading_example.py
- Reads data from a file.
- Handles `FileNotFoundError` if the file does not exist.
- Demonstrates the use of the `finally` block.

### 4. custom_exception.py
- Demonstrates how to create and raise a custom exception using `raise`.
- Checks eligibility based on age.

### 5. calculator.py
- Simple calculator using:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Handles invalid numbers and division by zero using exception handling.

### 6. student_marks.py
- Accepts student marks.
- Validates marks using exception handling.
- Displays grades based on marks.
- Demonstrates custom validation for valid mark range using `raise`.

## Concepts Learned

- Handling runtime errors using `try` and `except`.
- Handling multiple exceptions in a single program.
- Using the `finally` block to execute code regardless of exceptions.
- Raising custom exceptions using `raise`.
- Creating more robust and user-friendly Python programs.

## Outcome

Today I learned how Exception Handling makes Python programs safer by preventing unexpected crashes. I practiced handling different types of errors, creating custom exceptions, and writing programs that can respond gracefully to invalid user input. These concepts are essential for building reliable real-world Python applications.