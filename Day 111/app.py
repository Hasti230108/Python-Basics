import io

import streamlit as st
import csv
import io

st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

if "history" not in st.session_state:
    st.session_state.history = []

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
    st.session_state.history.append({
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result
    })

st.divider()
st.subheader("📜 Calculation History")

if st.session_state.history:
    for index, item in enumerate(reversed(st.session_state.history), start=1):
        st.write(
            f"{index}. {item['num1']:g} "
            f"{item['operation']} "
            f"{item['num2']:g} = {item['result']:g}"
        )
else:
    st.info("No calculations yet. Try calculating something!")

if st.session_state.history:
    output = io.StringIO()

    writer = csv.DictWriter(
        output,
        fieldnames=["num1", "operation", "num2", "result"]
    )

    writer.writeheader()
    writer.writerows(st.session_state.history)

    csv_data = output.getvalue()

    st.download_button(
        label="📥 Download Calculation History",
        data=csv_data,
        file_name="calculation_history.csv",
        mime="text/csv",
        use_container_width=True
    )

if st.session_state.history:
    if st.button("🗑️ Clear History"):
        st.session_state.history.clear()
        
st.divider()
st.caption("Built with Python & Streamlit | Day 109")
