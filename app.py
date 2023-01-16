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
    background: url('https://wallpapercave.com/uwp/uwp3212117.png');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
}
.stApp > header {
    background-color: transparent;
}

'''

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title("   "  + "GROUP15 -IROFUDE-")
st.title(" ")
moji = st.text_input("検索したい文字",key="moji",value = "irofude")
if st.session_state.moji is not None:
   search = moji 
image = Image.open(search +".jpg")
st.image(image,width = 200)
st.write("低学年")
moji1 = Image.open('images/iro1.jpg')
st.image(moji1,width = 50)
st.write("中学年")
moji2 = Image.open('images/iro2.jpg')
st.image(moji2,width = 50)
st.write("高学年")
st.write(' ')
moji3 = Image.open('images/iro3.jpg')
st.image(moji3,width = 50)

# ---------- テキスト入力 ----------
search = "white"
