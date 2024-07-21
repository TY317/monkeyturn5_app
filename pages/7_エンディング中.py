import streamlit as st
import pandas as pd
from PIL import Image

##### ページの内容 #####
# エンディング中のセリフの示唆内容を参考表示

st.subheader("エンディング中セリフでの示唆")
st.caption("・エンディング中のレア役成立時にサブ液晶タッチで示唆ボイス")
st.caption("・ボイス時にランプ色も変化")

im = Image.open("./image/ending_image.bmp")
st.image(im)