import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/Rahul(Photo).jpg", width=200)
with col2:
    st.title('Rahul Sharma')
    content = """
    Hello, My name is Rahul Sharma. 
    I graduated in 2022 with Bachelor of Technology
     in Computer Science from SGT University. I am 
     currently looking for an entry level position in 
     a reputed organisation as a python developer.
    """
    st.info(content)
st.text('Below you can find some of the app that i have built '
        'in Python. Feel free to contact me!')
col3, col4 = st.columns(2)
data = pd.read_csv("data.csv")

with col3:
    for index, row in data[::2].iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        print(f"images/{row['image']}")
        st.image(f"images/{row['image']}")
        st.link_button(label='link to web app', url=f"{row['url']}")
with col4:
    for index, row in data[1::2].iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.link_button(label='link', url=f"{row['url']}")
