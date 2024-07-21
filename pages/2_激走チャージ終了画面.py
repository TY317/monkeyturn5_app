import streamlit as st
import pandas as pd
from Top import columns_gekiso, index_gekiso, path_gekiso
from CsvDfClass import CsvDf
from PIL import Image

##### ページの内容 #####
# 激走チャージ終了画面の情報表示
# 波多野A、Bの回数をカウント


########################################
##### マイナス、1行削除のための変数・関数定義
########################################

#マイナス、1行削除のチェック状態用の変数
if "minus_check" not in st.session_state:
    st.session_state["minus_check"] = False
    minus_check = st.session_state["minus_check"]

def toggle_minus_check():
    st.session_state["minus_check"] = not st.session_state["minus_check"]

#ボタンの表示文字列の設定
if st.session_state["minus_check"]:
    button_str = "マイナス"
    button_type = "primary"
else:
    button_str = "カウント"
    button_type = "secondary"


#############################
##### csvデータを読み込み
#############################
df = CsvDf(columns=columns_gekiso,
           index=index_gekiso,
           path=path_gekiso)


#######################################
##### 終了画面表の表示
#######################################
st.subheader("激走チャージ終了画面")
st.caption("・サブ液晶をタッチして確認。設定示唆とモード示唆")
st.caption("・示唆内容は下の表を参照")
st.caption("・デフォルトの波多野A、Bの振り分けに設定差あるため、この2つはカウント。設定5はこれでかなり見抜けるらしい")

#終了画面を読み込んで表示
im = Image.open("./image/gekiso_image.bmp")
st.image(im)


#######################################
##### 波多野A、Bのカウント
#######################################
st.subheader("波多野A、Bのカウント")

#波多野A、Bの回数カウント

###################
##### 波多野A
###################

#2列に画面分割
col1, col2 = st.columns(2)

##### 左画面
with col1:
    st.caption("波多野A回数カウント")

    #カウントボタン
    hatanoA_count_btn = st.button(button_str,key="hatanoA", type=button_type)

    #カウント処理
    if hatanoA_count_btn:
        df.SelectedCount(selected=columns_gekiso[0],minus_check=st.session_state["minus_check"])

##### 右画面
with col2:
    st.caption("波多野B回数カウント")

    #カウントボタン
    hatanoB_count_btn = st.button(button_str,key="hatanoB", type=button_type)

    #カウント処理
    if hatanoB_count_btn:
        df.SelectedCount(selected=columns_gekiso[1],minus_check=st.session_state["minus_check"])


##########################
##### 出現率の算出
##########################

#結果用データフレームの作成
df_result = df.df.copy()

#波多野Aの確率を算出
count_sum = df_result.loc[df.df.index[0]].sum()
# st.write(count_sum)
hatanoA_ratio = df_result.at[df_result.index[0], df_result.columns[0]] / count_sum
# st.write(hatanoA_ratio)

#波多野Bの確率を算出
hatanoB_ratio = 1 - hatanoA_ratio

#結果用データフレームに結果を追加
df_result.loc["出現確率"] = [f"{hatanoA_ratio*100:.1f}%", f"{hatanoB_ratio*100:.1f}%"]

#解析値用データフレームの作成
columns_list_theoretical = ["波多野A", "波多野B"]
index_list_theoretical = ["設定1", "設定2", "設定4", "設定5", "設定6"]
data_list_theoretical = [["50%", "50%"],
                        ["40%", "60%"],
                        ["40%", "60%"],
                        ["70%", "30%"],
                        ["40%", "60%"]]
df_theoretical = pd.DataFrame(data_list_theoretical, index=index_list_theoretical, columns=columns_list_theoretical)

##### 結果を表示
#2列に画面分割
col1, col2 = st.columns(2)
with col1:
    st.caption("現在値")
    st.dataframe(df_result)

with col2:
    st.caption("解析値")
    st.dataframe(df_theoretical)



##### マイナスのチェックボックス表示
st.checkbox("マイナスカウント、1行削除", value=st.session_state["minus_check"], on_change=toggle_minus_check)