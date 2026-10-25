import streamlit as st

st.set_page_config(page_title="My Color Studio")
st.title("My Colour Studio")

color = st.color_picker(
    "Choose your favourite colour",
    "#FF69B4"
)

st.write("Selected HEX:", color )

hex_code = color.lstrip("#")

red = int(hex_code[0:2], 16)
green = int(hex_code[2:4], 16)
blue = int(hex_code[4:6], 16)

st.write("RGB:", red, green, blue)

st.subheader("Colour Preview")
st.markdown(
    f"""
    <div style="
        background-color: {color};
        height: 100px;
        border-radius: 12px;
        border: 1px solid #cccccc;
    "></div>
    """,
    unsafe_allow_html=True
)

st.subheader("Your Color Palette")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        ':color[Pink]{background="#FCE4EC"}'
    )

with col2:
    st.markdown(
        ':color[Lavender]{background="#E6E6FA"}'
    )

with col3:
    st.markdown(
        ':color[Mint]{background="#D1FAE5"}'
    )

with col4:
    st.markdown(
        ':color[Sky Blue]{background="#87CEEB"}'
    )

st.subheader("Your Selected Color Code")
st.code(color, language="text")

st.caption("Tip: Click and drag the colour picker to try different colours!")