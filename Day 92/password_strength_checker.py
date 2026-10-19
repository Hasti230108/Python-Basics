import streamlit as st

st.set_page_config(page_title="Password Strength Checker")

st.title("Password Strength Checker")
st.header("Check the strength of your password.")

input_password = st.text_input("Enter your password:", type="password")

length = len(input_password)
uppercase = any(char.isupper() for char in input_password)
lowercase = any(char.islower() for char in input_password)
digit = any(char.isdigit() for char in input_password)
special_characters = any(not char.isalnum() for char in input_password)

if st.button("Check Strength"):
    if length < 8:
        st.warning("Your password is too short. It should be at least 8 characters long.")
    elif not uppercase:
        st.warning("Your password should contain at least one uppercase letter.")
    elif not lowercase:
        st.warning("Your password should contain at least one lowercase letter.")
    elif not digit:
        st.warning("Your password should contain at least one digit.")
    elif not special_characters:
        st.warning("Your password should contain at least one special character.")
    else:
        st.success("Your password is strong!")

st.info("A strong password should be at least 8 characters long and contain uppercase letters, lowercase letters, digits, and special characters.")