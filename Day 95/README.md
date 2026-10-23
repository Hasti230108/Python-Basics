# 🎮Day 95 — Guess the Number Game

Today, I built a **Guess the Number Game** using Python and Streamlit. The computer generates a random number between 1 and 20, and the player tries to guess it.

The app also tracks the number of attempts and remembers the player's best score during the current session.

## Features

- 🎲 **Random Number Generation:** Generates a secret number between 1 and 20.
- 🔢 **Number Input:** Allows the player to enter a guess within the given range.
- ⬇️ **Too Low Message:** Displays a message when the guess is smaller than the secret number.
- ⬆️ **Too High Message:** Displays a message when the guess is greater than the secret number.
- 🎉 **Winning Message:** Displays a success message when the player guesses correctly.
- 🔁 **Attempt Counter:** Counts the number of guesses submitted.
- 🏆 **Best Score:** Tracks the fewest attempts taken to win during the current session.
- 🔄 **Play Again:** Starts a new round and resets the attempt counter.

## Technologies Used

- Python
- Streamlit
- Random module
- Streamlit Session State

## Concepts Practiced

- Importing modules
- Generating random numbers using `randint()`
- Conditional statements (`if`, `elif`, and `else`)
- Comparison operators
- Streamlit widgets such as `st.number_input()` and `st.button()`
- Displaying messages using `st.write()` and `st.success()`
- Managing session data using `st.session_state`
- Updating scores and resetting game values

## Key Learnings

This project helped me understand how to maintain values across Streamlit reruns using Session State. I also practiced conditional logic, random number generation, attempt tracking, and basic game state management.

---

Built a simple interactive number guessing game with an attempt counter, best score, and replay functionality.