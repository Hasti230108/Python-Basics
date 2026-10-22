import streamlit as st

st.set_page_config(page_title="Temperature Converter")

st.title("Temperature Converter")
st.write("A simple temperature converter helps to convert temperature from Celsius to Fahrenheit and vice versa.")

temperature = st.number_input("Enter your temperature:")

unit = st.selectbox(
    "Convert from:",
    ["Celsius", "Fahrenheit"]
)

if st.button("Convert Temperature"):
    if unit == "Celsius":
        st.write((temperature * 9 / 5 ) + 32)
    else:
        st.write((temperature - 32) * 5 / 9)