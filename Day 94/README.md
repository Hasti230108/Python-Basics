# Day 94 — Temperature Converter

## About the Project

The **Temperature Converter** is a simple interactive web application built using Python and Streamlit. It converts temperatures from Celsius to Fahrenheit and from Fahrenheit to Celsius based on the unit selected by the user.

## Features

- Accepts a temperature through a numeric input field.
- Allows the user to select Celsius or Fahrenheit.
- Converts the temperature when the user clicks the **Convert Temperature** button.
- Displays the converted result.
- Supports conversion in both directions.

## Technologies Used

- Python
- Streamlit

## Concepts Practiced

- Streamlit input widgets: `st.number_input()` and `st.selectbox()`
- Variables and user input
- Conditional statements using `if` and `else`
- Arithmetic operations
- Temperature conversion formulas
- Button handling using `st.button()`

## Conversion Formulas

**Celsius to Fahrenheit**

```python
fahrenheit = (temperature * 9 / 5) + 32
```

**Fahrenheit to Celsius**

```python
celsius = (temperature - 32) * 5 / 9
```

---

Built a basic temperature conversion app while practising Python conditional logic, arithmetic operations, and interactive Streamlit widgets.

---

*Keep learning, one small project at a time!* 