import streamlit as st
import pandas as pd
from PIL import Image
from Top import columns_aoshima, index_aoshima, path_aoshima
# from Top import columns_shuki, index_shuki, path_shuki
from CsvDfClass import CsvDf


##### ページの内容 #####
# 青島SG中のラウンド開始画面
# 青島SG中のSPフリーズの情報表示


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
    button_str = "登録"
    button_type = "secondary"


#############################
##### csvデータを読み込み
#############################
df = CsvDf(columns=columns_aoshima,
           index=index_aoshima,
           path=path_aoshima)


#################################
##### 青島SPフリーズの情報
#################################
st.subheader("SPフリーズ")
st.caption("・SPフリーズの発生に設定差があるのは間違いないらしい(解析数値はなし)")
st.caption("・1回でも確認できれば高設定期待度アップか")
st.caption("・1ラウンド目からの発生は無さそう。2ラウンド目から期待")


#################################
##### ラウンド開始画面のカウント
#################################
st.subheader("ラウンド開始画面")
st.caption("・ラウンド開始画面で設定を示唆(解析値はなし)")
st.write("・フリーズ後は設定関係なく青島＆波多野出てくるので、カウントから除外！！")

#画面の選択肢をセッション管理するための変数設定
if "pic_select" not in st.session_state:
    st.session_state.pic_select = ""

#セレクトボックスを作成
st.session_state.pic_select = st.selectbox("終了画面", df.columns_list)

#選択肢に合わせて画像を表示
im_path = f"./image/aoshima_{st.session_state.pic_select}.jpg"
im = Image.open(im_path)
st.image(im, width=300)

#登録ボタン
submit_btn = st.button(button_str, type=button_type)

#カウント処理
if submit_btn:
    df.SelectedCount(selected=st.session_state.pic_select,
                  minus_check=st.session_state["minus_check"])

#結果の表示
remarks_list = ["デフォルト", "偶数設定示唆", "高設定示唆", "設定5以上"]
df.CountAndProbabilityResultShow(remarks_list=remarks_list)

##### マイナスのチェックボックス表示
st.checkbox("マイナスカウント、1行削除", value=st.session_state["minus_check"], on_change=toggle_minus_check)