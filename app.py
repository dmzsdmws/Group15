# 以下を「app.py」に書き込み
import io
import os
import fitz
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import numpy as np
import pandas as pd
from st_on_hover_tabs import on_hover_tabs

css = '''
.stApp {
    
    background: url('https://wallpapercave.com/uwp/uwp3212126.jpeg');
    background-size: 75%;
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
   search = "irofude"

image = Image.open(search +".jpg")

x = 200
a = 80
b = 80
c = 80

col1, col2 ,col3 = st.columns(3)
with col1:
    st.markdown('**検索結果:**')
with col2:
    if st.button('画像拡大'):
        x = 400
with col3:
    if st.button('復元'):
        x = 200

st.image(image,width = x)
moji1 = Image.open('images/dai1.jpg')
moji2 = Image.open('images/iro1.jpg')
moji3 = Image.open('images/dan1.jpg')
moji4 = Image.open('images/ichi.jpg')
moji5 = Image.open('images/ni.jpg')
moji6 = Image.open('images/ao.jpg')
moji7 = Image.open('images/ai.jpg')
moji8 = Image.open('images/san.jpg')
moji9 = Image.open('images/fude.jpg')
moji10 = Image.open('images/ki.jpg')
moji11 = Image.open('images/wara.jpg')
moji12 = Image.open('images/sou.jpg')

st.title(" 　")
st.write(" 　")

col1, col2 ,col3= st.columns(3)
with col1:
    st.write('**_低学年_**')
with col2:
    if st.button(' 画像拡大'):
        a = 160
with col3:
    if st.button(' 復元'):
        a = 80    

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image(moji1,width = a)
with col2:
    st.image(moji4,width = a)
with col3:
    st.image(moji5,width = a)
with col4:
    st.image(moji8,width = a)

col1, col2 ,col3= st.columns(3)
with col1:    
    st.write('**_中学年_**')
with col2:
    if st.button(' 画像拡大 '):
        b = 160
with col3:
    if st.button(' 復元 '):
        b = 80 
col1, col2, col3, col4= st.columns(4)
with col1:
    st.image(moji2,width = b)
with col2:
    st.image(moji11,width = b)
with col3:
    st.image(moji6,width = b)
with col4:
    st.image(moji10,width = b)
   
col1, col2 ,col3= st.columns(3)
with col1:    
     st.write('**_高学年_**')
with col2:
    if st.button('画像拡大 '):
        c = 160
with col3:
    if st.button('復元 '):
        c = 80    

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image(moji9,width = c)
with col2:
    st.image(moji3,width = c)
with col3:
    st.image(moji7,width = c)
with col4:
    st.image(moji12,width = c)


# ---------- テキスト入力 ----------
search = "irofude"
