import streamlit as st
import pandas as pd
from PIL import Image

##### ページの内容 #####
# 舟券での示唆内容を参考表示


st.subheader("舟券での示唆")
st.caption("・ライバルモードと設定を示唆。詳細は下表参照")

im = Image.open("./image/funaken_image.bmp")
st.image(im)