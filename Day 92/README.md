# Day 92 — Password Strength Checker

## About the Project

The **Password Strength Checker** is a simple interactive web app built using Python and Streamlit. It checks whether a password meets basic requirements and displays feedback to the user.

## Features

- Accepts password input through a masked text field.
- Checks whether the password contains at least 8 characters.
- Checks for uppercase letters and lowercase letters.
- Checks for at least one digit.
- Checks for at least one special character.
- Displays warnings when a requirement is missing.
- Shows a success message when all checks pass.

## Technologies Used

- Python
- Streamlit

## Concepts Practiced

- String methods: `isupper()`, `islower()`, `isdigit()` and `isalnum()`
- `len()` for checking password length
- `any()` with generator expressions
- Conditional statements: `if`, `elif` and `else`
- Streamlit UI components and user input handling

## Note

This project checks basic password characteristics. It does not guarantee that a password is secure or difficult to guess. Use fictional passwords for testing, not real passwords.

---

Built an interactive password-checking app while practising Python string methods, conditional logic, and Streamlit.