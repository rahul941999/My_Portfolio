import streamlit as st


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/Rahul(Photo).jpg",width=200)
with col2:
    content = """
    Hello, My name is Rahul Sharma.
    I am a Computer Science graduate looking for an entry level 
    position as a python developer.
    """
    st.info(content)
