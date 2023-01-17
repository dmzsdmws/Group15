# 以下を「app.py」に書き込み
import io
import os
import fitz
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import numpy as np
import pandas as pd

css = '''
.stApp {
    
    background: url('https://wallpapercave.com/uwp/uwp3212126.jpeg');
    background-size: 50%;
    background-repeat: no-repeat;
    background-position: center;
    background-color: #C2EEFF;
   
}
.stApp > header {
    background-color: #6699CC;
}


'''

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
st.title("  ")
st.markdown('_スマホの画面を横にしてください_')
search = "irofude"
moji = st.text_input("検索したい文字:",key="moji",value = "irofude",placeholder = "irofude" )
if st.session_state.moji is not None:
   search = moji 
else:
   st.write('Error')

image = Image.open(search +".jpg")
x = 200
col1, col2 = st.columns(2)
with col1:
    st.markdown('**検索結果:**')
with col2:
    if st.button('画像拡大'):
    　  x = 400
st.markdown('**検索結果:**')
st.image(image,width = x)
moji1 = Image.open('images/dai1.jpg')
moji2 = Image.open('images/iro1.jpg')
moji3 = Image.open('images/dan1.jpg')
moji4 = Image.open('images/ichi.jpg')
moji5 = Image.open('images/ni.jpg')
moji6 = Image.open('images/ao.jpg')
moji7 = Image.open('images/dai3.jpg')
moji8 = Image.open('images/dan3.jpg')
moji9 = Image.open('images/iro3.jpg')
st.title(" ")
st.markdown('**_中学年_**')
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.image(moji1,width = 60)
with col2:
    st.image(moji4,width = 60)
with col3:
    st.image(moji5,width = 60)
with col4:
    st.image(moji1,width = 60)
with col5:
    st.image(moji4,width = 60)
with col6:
    st.image(moji5,width = 60)

st.write('**_中学年_**')
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.image(moji6,width = 60)
with col2:
    st.image(moji2,width = 60)
with col3:
    st.image(moji6,width = 60)
with col4:
    st.image(moji2,width = 60)
with col5:
    st.image(moji6,width = 60)
with col6:
    st.image(moji2,width = 60)
st.write('**_高学年_**')
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.image(moji3,width = 60)
with col2:
    st.image(moji3,width = 60)
with col3:
    st.image(moji3,width = 60)
with col4:
    st.image(moji3,width = 60)
with col5:
    st.image(moji3,width = 60)
with col6:
    st.image(moji3,width = 60)

# ---------- テキスト入力 ----------
search = "white"
