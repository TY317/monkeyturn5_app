import streamlit as st
import pandas as pd
from Top import columns_shuki, index_shuki, path_shuki
from CsvDfClass import CsvDf

##### ページの内容 #####
# 周期と規定Pt、その他当選契機の履歴をメモ


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
    button_str = "1行削除"
    button_type = "primary"
else:
    button_str = "登録"
    button_type = "secondary"


#############################
##### csvデータを読み込み
#############################
df = CsvDf(columns=columns_shuki,
           index=index_shuki,
           path=path_shuki)


#######################################
##### 履歴のメモ
#######################################
st.subheader("周期での規定Pt、当選契機の履歴メモ")
st.caption("・高設定は3周期以上ハマりにくい。低設定は5,6周期に簡単にいく")
st.caption("・高設定ほど222ptが選ばれやすい。666ptが選ばれるとマイナスポイント")
st.caption("・弱レア役での直撃は設定4以上確定。直撃時は大体バイブなど、かなり強い演出が伴う")
st.caption("・モードB以上の示唆は300Gくらい回せば結構出る。出なければAの可能性高い")

#選択肢のリストを変数として設定
shuki_select_list= ["1周期", "2周期", "3周期", "4周期", "5周期", "6周期"]
pt_select_list = ["111pt", "222pt", "333pt", "444pt", "555pt", "666pt", "超抜", "直撃(強レア)", "直撃(弱レア)", "確定役", "天井"]
at_select_list = ["はずれ", "当選"]

##### 履歴データを入力し、登録するフォーム
with st.form(key='historical_data_input'):
    st.caption("周期・契機の結果入力")

    #3列のカラムを作成
    col1, col2, col3 = st.columns(3)

    #周期の入力
    with col1:
        shuki_result = st.selectbox(df.columns_list[0], shuki_select_list)

    #pt・契機の入力
    with col2:
        pt_result = st.selectbox(df.columns_list[1], pt_select_list)

    #当落結果の入力
    with col3:
        at_result = st.selectbox(df.columns_list[2], at_select_list)

    #登録ボタン
    submit_btn = st.form_submit_button(button_str, type=button_type)

    ##### 結果を保存
    #選択された結果をまとめたリストを定義
    selected_list = [shuki_result, pt_result, at_result]

    #結果の保存処理
    if submit_btn:
        df.BonusHistrical(add_result=selected_list,
                        minus_check=st.session_state["minus_check"])


#####################################
##### 結果の表示
#####################################

##### 履歴データの表示
st.caption("履歴データ")
st.dataframe(df.df)


##### マイナスのチェックボックス表示
st.checkbox("マイナスカウント、1行削除", value=st.session_state["minus_check"], on_change=toggle_minus_check)