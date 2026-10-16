import streamlit as st

st.title("Student Profile Creator.")

name = st.text_input("Enter your name:")

course = st.selectbox(
    "choose your course",
    ["AI & ML", "Data Science",  "Cyber Security", "Other"]
)

age = st.slider("Select your age", 16, 30, 25)

if st.button("Create Profile"):
    if name.strip():
        st.subheader("Your Profile")
        st.write("Name:", name)
        st.write("Course:", course)
        st.write("Age:", age)
        st.success("Profile created successfully!")
    else:
        st.warning("Please enter your name.")