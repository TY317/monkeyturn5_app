import streamlit as st
import pandas as pd
from PIL import Image
from Top import columns_rival, index_rival, path_rival
from Top import columns_shuki, index_shuki, path_shuki
from CsvDfClass import CsvDf

##### ページの内容 #####
# 設定差のあるライバルモードの回数をカウント

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
df = CsvDf(columns=columns_rival,
           index=index_rival,
           path=path_rival)

#AT初当り回数をカウントするためのcsv読み込み
at_df = CsvDf(columns=columns_shuki,
           index=index_shuki,
           path=path_shuki)


#######################################
##### ライバルモードのカウント
#######################################
st.subheader("ライバルモード")
st.caption("・蒲生、浜岡、榎木のライバルモードに設定差あり")
st.caption("・示唆が出ず見抜けないことも多いため、参考程度。あまり気にしなくてもいい")
st.caption("・各モードの特徴は下表を参照")
st.caption("( ※通常時モードの消化回数は1ページ目の履歴データから取得しています )")

#3列に画面分割
col1, col2, col3 = st.columns(3)

##### 左画面
with col1:
    st.caption("蒲生カウント")

    #カウントボタン
    gamou_count_btn = st.button(button_str,key="gamou", type=button_type)

    #カウント処理
    if gamou_count_btn:
        df.SelectedCount(selected=columns_rival[0],minus_check=st.session_state["minus_check"])

##### 中画面
with col2:
    st.caption("浜岡カウント")

    #カウントボタン
    hamaoka_count_btn = st.button(button_str,key="hamaoka", type=button_type)

    #カウント処理
    if hamaoka_count_btn:
        df.SelectedCount(selected=columns_rival[1],minus_check=st.session_state["minus_check"])

##### 右画面
with col3:
    st.caption("榎木カウント")

    #カウントボタン
    enoki_count_btn = st.button(button_str,key="enoki", type=button_type)

    #カウント処理
    if enoki_count_btn:
        df.SelectedCount(selected=columns_rival[2],minus_check=st.session_state["minus_check"])


##########################
##### 出現率の算出
##########################

#ATの当選回数を取得
at_result_counts = at_df.df[at_df.df.columns[2]].value_counts()

#「当選」の回数を取得
at_times = at_result_counts.get("当選", 0)

#蒲生の出現率
gamou_ratio = df.df.at[df.df.index[0], df.df.columns[0]] / (at_times + 1)
# st.write(gamou_ratio)
# st.dataframe(df.df)

#浜岡の出現率
hamaoka_ratio = df.df.at[df.df.index[0], df.df.columns[1]] / (at_times + 1)

#榎木の出現率
enoki_ratio = df.df.at[df.df.index[0], df.df.columns[2]] / (at_times + 1)

#####結果用データフレームを作って表示
df_result = df.df.copy()

#出現率の結果を追加
df_result.loc["出現確率"] = [f"{gamou_ratio*100:.1f}%", f"{hamaoka_ratio*100:.1f}%", f"{enoki_ratio*100:.1f}%"]

#解析値用データフレームの作成
columns_list_theoretical = ["蒲生", "浜岡", "榎木"]
index_list_theoretical = ["設定1", "設定2", "設定4", "設定5", "設定6"]
data_list_theoretical = [["7.8%", "7.8%", "7.8%"],
                        ["8.6%", "8.2%", "8.2%"],
                        ["10.9%", "9.4%", "9.4%"],
                        ["14.1%", "10.5%", "10.5%"],
                        ["15.6%", "10.9%", "10.9"]]
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


##########################
##### ライバルモードの説明
##########################
im = Image.open("./image/rival_image.bmp")
st.image(im)


##### マイナスのチェックボックス表示
st.checkbox("マイナスカウント、1行削除", value=st.session_state["minus_check"], on_change=toggle_minus_check)