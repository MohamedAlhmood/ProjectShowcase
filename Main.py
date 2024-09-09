import streamlit as st

st.set_page_config(layout='wide')
col1,col2 = st.columns(2)

with col1:
    st.image('images/image.jpg')
with col2:
    st.title("Mohamed Alhmood")
    content = """Hello My names Mohamed! I am a student at the University Of Michigan And I'm a software engineering major. I am proficient in Python and C++ and this page is a website to showcase my projects that I have made so far in my journey of programming"""
    st.info(content)
content2 = """***Below are some of my projects. Feel free to contact me!***"""
st.write(content2)