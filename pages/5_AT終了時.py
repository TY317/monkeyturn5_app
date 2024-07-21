import streamlit as st
import pandas as pd
from PIL import Image
from Top import columns_medal, index_medal, path_medal
from Top import columns_shuki, index_shuki, path_shuki
from CsvDfClass import CsvDf


##### ページの内容 #####
# メダルの出現回数をカウント


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
df = CsvDf(columns=columns_medal,
           index=index_medal,
           path=path_medal)

#AT初当り回数をカウントするためのcsv読み込み
at_df = CsvDf(columns=columns_shuki,
           index=index_shuki,
           path=path_shuki)


#######################################
##### AT終了時のメダルカウント
#######################################
st.subheader("AT終了時のメダル")
st.caption("・黄色メダル以上は示唆としてかなり強いらしい")
st.caption("・メダルの出現回数をカウント")
st.caption("( ※AT当選回数は1ページ目の履歴データから取得しています )")

#3列に画面分割
col1, col2, col3 = st.columns(3)

##### 左画面
with col1:
    st.caption("青メダル")

    #カウントボタン
    blue_medal_count_btn = st.button(button_str,key="blue_medal", type=button_type)

    #カウント処理
    if blue_medal_count_btn:
        df.SelectedCount(selected=columns_medal[0],minus_check=st.session_state["minus_check"])

##### 中画面
with col2:
    st.caption("黄メダル")

    #カウントボタン
    yellow_medal_count_btn = st.button(button_str,key="yellow_medal", type=button_type)

    #カウント処理
    if yellow_medal_count_btn:
        df.SelectedCount(selected=columns_medal[1],minus_check=st.session_state["minus_check"])

##### 右画面
with col3:
    st.caption("黒メダル")

    #カウントボタン
    black_medal_count_btn = st.button(button_str,key="black_medal", type=button_type)

    #カウント処理
    if black_medal_count_btn:
        df.SelectedCount(selected=columns_medal[2],minus_check=st.session_state["minus_check"])


##########################
##### 出現率の算出
##########################

#ATの当選回数を取得
at_result_counts = at_df.df[at_df.df.columns[2]].value_counts()

#「当選」の回数を取得
at_times = at_result_counts.get("当選", 0)

#青メダルの出現率
blue_medal_ratio = df.df.at[df.df.index[0], df.df.columns[0]] / at_times
# st.write(gamou_ratio)
# st.dataframe(df.df)

#黄メダルの出現率
yellow_medal_ratio = df.df.at[df.df.index[0], df.df.columns[1]] / at_times

#黒メダルの出現率
black_medal_ratio = df.df.at[df.df.index[0], df.df.columns[2]] / at_times

#####結果用データフレームを作って表示
df_result = df.df.copy()

#出現率の結果を追加
df_result.loc["出現確率"] = [f"{blue_medal_ratio*100:.1f}%", f"{yellow_medal_ratio*100:.1f}%", f"{black_medal_ratio*100:.1f}%"]

##### 結果を表示
st.dataframe(df_result)

st.caption("黄メダル30%以上が欲しい")
st.caption("AT9回で青2回、黄2回で若干弱い  というくらいの感触らしい")


##########################
##### トロフィーの情報表示
##########################
st.subheader("トロフィーの示唆")

im = Image.open("./image/torofy_image.bmp")
st.image(im)


##### マイナスのチェックボックス表示
st.checkbox("マイナスカウント、1行削除", value=st.session_state["minus_check"], on_change=toggle_minus_check)