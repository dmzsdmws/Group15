# 以下を「app.py」に書き込み
import io
import os
import fitz
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import numpy as np
import pandas as pd
st.title("   "  + "GROUP15 -IROFUDE-")
st.set_page_config(
        page_title= "Multipage App",
        page_icon="📁")
st.markdown('<style>div[class="css-6qob1r e1fqkh3o3"] { background: url("https://media2.giphy.com/media/46hpy8xB3MiHfruixn/giphy.gif");background-repeat: no-repeat;background-size:350%;border:1px solid #36454F; border-top:none;} </style>', unsafe_allow_html=True)
st.title(" ")
moji = st.text_input("検索したい文字",key="moji",value = "irofude")
if st.session_state.moji is not None:
   search = moji 
image = Image.open(search +".jpg")
st.image(image,width = 200)
st.markdown(":blue[低学年]")
moji1 = Image.open('images/iro1.jpg')
st.image(moji1,width = 50)
st.markdown(":blue[中学年]")
moji2 = Image.open('images/iro2.jpg')
st.image(moji2,width = 50)
st.markdown(":blue[高学年]")
st.write(' ')
moji3 = Image.open('images/iro3.jpg')
st.image(moji3,width = 50)

# ---------- テキスト入力 ----------
search = "white"
