import streamlit as st
from PIL import Image
from io import BytesIO

import pandas
from pathlib import Path
import requests

st.set_page_config(layout='wide')
col1,col2 = st.columns(2)
csvData = pandas.read_csv('static/data.csv',sep=';')


url_icon = "https://raw.githubusercontent.com/MohamedAlhmood/ProjectShowcase/refs/heads/master/image.jpg"
response = requests.get(url_icon)
img = Image.open(BytesIO(response.content))


with col1:
    st.image(img)
with col2:
    st.title("Mohamed Alhmood")
    content = """Hello My names Mohamed! I am a student at the University Of Michigan And I'm a software engineering major. I am proficient in Python and C++ and this page is a website to showcase my projects that I have made so far in my journey of programming"""
    st.info(content)
content2 = """***Below are some of my projects. Feel free to contact me!***"""
st.write(content2)

col3 ,col4, col5 = st.columns([1.5,0.5,1.5])
with col3:
    for index,row in csvData[:2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        url_icon = row['image']
        response = requests.get(url_icon)
        img = Image.open(BytesIO(response.content))
        st.image(img)
        st.write("[Source Code]("+row['url']+')')
with col5:
    for index,row in csvData[2:4].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        url_icon = row['image']
        response = requests.get(url_icon)
        img = Image.open(BytesIO(response.content))
        st.image(img)
        st.write("[Source Code](" + row['url'] + ')')


#with col5:
#    for index,row in csvData[10:].iterrows():
#        st.header(row['title'])
#        st.write(row['description'])
#        st.image(f"images/{row['image']}")
#        #st.write("[Source Code...(]"+row['url']+')')
#        st.write('[Source Code]('+row['url']+')')
