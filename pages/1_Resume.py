import requests
import streamlit as st
st.title("Resume")
# image ID
# file_id = "13lKo6cb5pVEuC7OxE2di_dMIhfRt2wmQ"
#
# # URL
# url = f"https://drive.google.com/uc?export=view&id={file_id}"
#
# response = requests.get(url)
# st.image(response.content)
resume = st.file_uploader("../pdf/Rahul_resume.pdf", type="pdf")
if resume is not None:
    st.pdf(resume)

