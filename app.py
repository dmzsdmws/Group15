# 以下を「app.py」に書き込み
import streamlit as st
from pyngrok import ngrok
import os
import sys
import datetime
from PIL import Image
import cv2
import tkinter.filedialog as fd

st.title("GROUP15 -IROFUDE-")
st.title(" ")
st.write('低学年')
moji1 = Image.open('/content/images/iro1.jpg')
st.image(moji1,width = 50)
st.write('中学年')
moji2 = Image.open('/content/images/iro2.jpg')
st.image(moji2,width = 50)
st.write('高学年')
moji3 = Image.open('/content/images/iro3.jpg')
st.image(moji3,width = 50)

# ---------- テキスト入力 ----------
search = "white"
moji = st.text_input("検索したい文字",key="moji",value = "irofude")
if st.session_state.moji is not None:
   search = moji 
image = Image.open(search +".jpg")
st.image(image,width = 200)
