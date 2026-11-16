# Day 112 — Advanced Calculator Operations

Today, I continued upgrading my Streamlit Simple Calculator by adding advanced arithmetic operations and improving how calculation results are displayed.

The calculator now supports six operations, handles additional mathematical edge cases, and displays small decimal values in ordinary decimal notation.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Modulus — calculates the remainder
- Power — calculates exponentiation
- Handles division by zero
- Handles modulus by zero
- Handles zero raised to a negative power
- Handles unsupported fractional powers of negative numbers
- Maintains calculation history
- Clear History button
- Download calculation history as a CSV file
- Displays small decimal values in ordinary notation

## Concepts Learned

- Using the modulus operator `%`
- Using the exponentiation operator `**`
- Handling mathematical edge cases with conditional statements
- Checking whether a number is an integer using `.is_integer()`
- Formatting floating-point numbers
- Using f-string precision with `.15f`
- Removing unnecessary trailing zeros using `.rstrip()`
- Reusing code through a custom function
- Updating calculation history with formatted results

## Number Formatting

I created a custom function to display numbers with up to 15 decimal places while removing unnecessary trailing zeros.

```python
def format_number(value):
    return f"{value:.15f}".rstrip("0").rstrip(".")
```

For example:

| Original display | Formatted display |
|---|---|
| `1.31687e-06` | `0.00000131687` |
| `2.500000` | `2.5` |
| `8.000000` | `8` |

*Note: The formatter rounds values to a maximum of 15 decimal places.*

## Test Cases

| Calculation | Expected result |
|---|---:|
| 10 % 3 | 1 |
| 2 ** 3 | 8 |
| 15 ** -5 | 0.00000131687 |
| 10 / 4 | 2.5 |
| 0 ** -1 | Error message |

## Technologies Used

- Python
- Streamlit
- CSV
- IO

## Key Takeaways

I learned how to extend a basic calculator with additional mathematical operations and handle special cases using conditional statements.

I also learned how to create reusable formatting functions to make numerical results easier to read.

This project helped me practice Python functions, operators, error handling, Streamlit widgets, Session State, and CSV file generation.

---

Successfully upgraded the Simple Calculator with Modulus, Power, improved decimal formatting, and additional error handling.