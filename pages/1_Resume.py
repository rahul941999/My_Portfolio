import requests
import streamlit as st

# iamge ID
file_id = "13lKo6cb5pVEuC7OxE2di_dMIhfRt2wmQ"

# URL
url = f"https://drive.google.com/uc?export=view&id={file_id}"

response = requests.get(url)
st.image(response.content)

