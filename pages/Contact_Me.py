import streamlit as st
from sendEmail import sendMail
st.header("Contact Me")

with st.form(key='email'):
    userEmail = st.text_input('Your Email Address')
    message = st.text_area('Your Message')
    message = f"""\
Subject: New email from {userEmail}
{message}\n\nFrom: {userEmail}"""
    button = st.form_submit_button('Submit')
    if button:
        sendMail(message)
        st.info('Your email has been sent successfully!')