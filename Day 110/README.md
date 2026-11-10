# Day 110 — Simple Calculator with Calculation History

Today, I upgraded my Day 109 Simple Calculator by adding a **Calculation History** feature using Streamlit's Session State.

The app now stores previous calculations, displays them in reverse chronological order, and allows users to clear the history.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Handles division by zero
- Stores previous calculations
- Displays the newest calculation first
- Provides a Clear History button
- Uses a custom dark aubergine and orchid theme

## Concepts Learned

- Understanding `st.session_state`
- Initializing session variables
- Storing calculations in a Python list
- Using dictionaries to organize calculation details
- Adding records with `.append()`
- Removing records with `.clear()`
- Using `enumerate()` to number history entries
- Using `reversed()` to display recent calculations first
- Understanding Streamlit app reruns

## How Calculation History Works

Streamlit reruns the application when users interact with widgets. Ordinary Python variables are reset during these reruns.

I used `st.session_state` to preserve the calculation history during the current session.

Each calculation is stored as a dictionary containing:

- First number
- Second number
- Selected operation
- Result

The history is displayed with the latest calculation at the top.

**Note:** Session State is temporary. History is not permanently saved and can be lost when the browser session is reset or the app restarts.

## Technologies Used

- Python
- Streamlit
- TOML configuration

## Key Takeaways

I learned how Streamlit Session State helps preserve information across application reruns.

I also practiced managing data using Python lists and dictionaries and displaying dynamic information in a Streamlit interface.
