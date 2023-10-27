import streamlit as st
import Send_email


st.title('Contact me :')
with st.form(key='mail_form'):
    email_addr = st.text_input("Your E-Mail address: ",
                               placeholder='xyz@abc.com', key='email')
    message = st.text_area('Message', height=250,
                           placeholder='Enter your message', key='msg')
    button = st.form_submit_button(label='Send')
    if button:
        Send_email.send(email_addr, message)
        st.text("mail sent!")
