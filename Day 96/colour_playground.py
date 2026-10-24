import streamlit as st

st.set_page_config(page_title="Colour Playground")
st.title("My Colour Playground")

st.markdown(":red[This text is red]")
st.markdown(":blue[This text is blue]")
st.markdown(":green[This text is green]")
st.markdown(":violet[This text is violet]")
st.markdown(':color[This text is pink]{foreground="#FF69B4" background="#FCE4EC"}')
