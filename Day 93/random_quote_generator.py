import streamlit as st
import random

st.set_page_config(page_title="Random Quote Generator")

st.title("Random Quote Generator")
st.header("A little inspiration for your day!")

quotes = [
    "Believe in yourself and keep going.",
    "Small steps lead to big changes.",
    "Every day is a new beginning.",
    "Your efforts today shape your tomorrow.",
    "Progress is better than perfection.",
    "Never stop learning and growing.",
    "Difficult roads can lead to beautiful destinations.",
    "You are capable of more than you think."
]

st.write("Click the button to discover a random quote!")

if st.button("Generate Quote"):
    quote = random.choice(quotes)
    st.success(quote)

st.info("Take a deep breath, trust your journey, and keep moving forward.")
