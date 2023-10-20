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
st.divider()
st.text('Below you can find some of the app that i have built '
        'in Python. Feel free to contact me!')
st.divider()
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
data = pd.read_csv("data.csv")

with col3:
    for index, row in data[::2].iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        print(f"images/{row['image']}")
        st.image(f"images/{row['image']}")
        col3_c1, col3_c2 = st.columns(2)
        with col3_c1:
            st.link_button(label='link to web app', url=f"{row['url']}")
        with col3_c2:
            st.write(f"[source code]({row['url']})")
        st.divider()
with col4:
    for index, row in data[1::2].iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        st.image("images/"+row['image'])
        col4_c1, col4_c2 = st.columns(2)
        with col4_c1:
            st.link_button(label='link to web app', url=f"{row['url']}")
        with col4_c2:
            st.write(f"[source code]({row['url']})")
        st.divider()
