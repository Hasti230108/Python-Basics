import streamlit as st

st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Simple Calculator")
st.caption("A basic calculator built with Python and Streamlit.")

st.divider()

num1 = st.number_input(
    "Enter first number",
    value=0.0
)

num2 = st.number_input(
    "Enter second number",
    value=0.0
)

operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate", use_container_width=True):
    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        if num2 == 0:
            st.error("Cannot divide by zero!")
            st.stop()

        result = num1 / num2

    st.success(f"Result: {result:g}")

st.divider()
st.caption("Built with Python & Streamlit | Day 109")
