import streamlit as st
import random as rd

st.set_page_config(page_title="Guess the Number")

st.title("Guess the Number Game")

if "secret_number" not in st.session_state:
    secret_number = rd.randint(1, 20)
    st.session_state.secret_number = secret_number
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    if "best_score" not in st.session_state:
        st.session_state.best_score = None

guess = st.number_input("Guess a number between 1 and 20", min_value=1, max_value=20, key="guess")
st.write("Attempts:", st.session_state.attempts)
st.write("Best Score:", st.session_state.best_score if st.session_state.best_score is not None else "N/A")

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.write("Too low! Try again.")
    elif guess > st.session_state.secret_number:
        st.write("Too high! Try again.")
    else:
        st.success("Correct! You guessed the number!")
        if (
            st.session_state.best_score is None
            or st.session_state.attempts < st.session_state.best_score
        ):
            st.session_state.best_score = st.session_state.attempts
            st.balloons()
            st.write("New best score!")

if st.button("Play Again"):
    st.session_state.secret_number = rd.randint(1, 20)
    st.session_state.attempts = 0
    st.rerun()