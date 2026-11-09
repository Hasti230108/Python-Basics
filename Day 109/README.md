# Day 109 — Simple Calculator using Streamlit

Today I built a **Simple Calculator** using Python and Streamlit.

The app takes two numbers, lets the user select an arithmetic operation, and displays the calculated result.

## Concepts Practiced

- Creating a Streamlit application
- Using `st.number_input()` to accept numeric input
- Using `st.selectbox()` to choose an operation
- Using `st.button()` to trigger calculations
- Using `if-elif-else` conditional statements
- Performing arithmetic operations
- Handling division by zero
- Displaying results with `st.success()` and errors with `st.error()`
- Customizing the app using Streamlit's `config.toml`

## Features

The calculator supports four operations:

| Operation | Function |
|---|---|
| Addition | Adds two numbers |
| Subtraction | Subtracts the second number from the first |
| Multiplication | Multiplies two numbers |
| Division | Divides the first number by the second |

It also handles division by zero by displaying an error message instead of attempting the calculation.

## Technologies Used

- **Python**
- **Streamlit**
- **TOML** for Streamlit theme configuration

## UI Design

The application uses a dark aubergine and orchid theme.

- Deep aubergine background
- Orchid-colored accents
- Dark surface backgrounds
- Centered calculator layout

## Key Takeaways

- Streamlit makes it possible to turn Python scripts into interactive web apps.
- Widgets collect input directly from users.
- Conditional statements help select which calculation to perform.
- Error handling makes an application safer and more user-friendly.

---

Built a working calculator with four arithmetic operations and a customized Streamlit interface.