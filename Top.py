import streamlit as st
import pandas as pd
from GeneralDef import TodayUseCheck

st.title("モンキーターンⅤ")

################################################
##### データフレームの定義 #######################
################################################

# 周期・ポイント用
columns_shuki = ["周期", "規定Pt or 契機", "SGラッシュ"]
index_shuki = []
data_shuki = []
path_shuki = "./pages/shuki_df.csv"

#激走チャージ画面用
columns_gekiso = ["波多野A","波多野B"]
index_gekiso = ["出現回数"]
data_gekiso = [[0,0]]
path_gekiso = "./pages/gekiso_image_count_df.csv"

#ライバルモード用
columns_rival = ["蒲生","浜岡","榎木"]
index_rival = ["推定回数"]
data_rival = [[0,0,0]]
path_rival = "./pages/rival_count_df.csv"

#AT終了時のメダルカウント用
columns_medal = ["青メダル", "黄メダル", "黒メダル"]
index_medal = ["出現回数"]
data_medal = [[0, 0, 0]]
path_medal = "./pages/medal_count_df.csv"

#青島SGのラウンド開始画面用
columns_aoshima = ["私服", "レース服", "ドレス", "青島＆波多野"]
index_aoshima = ["出現回数"]
data_aoshima = [[0, 0, 0, 0]]
path_aoshima = "./pages/aoshima_count_df.csv"

##################################################
##### 新規作成ボタンを押すとデータをすべてリセットする
##################################################

#フォームの作成
with st.form(key='new_play'):

    #説明書き
    st.caption("※ 新規作成ボタンを押すとデータがすべて0リセットされます!")
    st.caption("※ 同時に他の人が利用しているとその人のデータも0リセットされます!恨みっこなしです!")
    st.caption("※ データの最終更新が本日だと「本日使用中」表示になります")

    #データの最終更新日が本日かをチェック
    today_use_check_result = TodayUseCheck()
    # st.write(today_use_check_result)

    #チェック結果に応じて表示
    if today_use_check_result:
        st.markdown(":red-background[本日使用中]")
    else:
        st.markdown(":green-background[本日未使用]")

    #新規作成ボタンの設定
    start_btn = st.form_submit_button("新規作成")

    #ボタンが押されたらcsvファイルをリセットし保存
    if start_btn:

        #########################################
        ##### csvファイルの作成 ##################
        #########################################

        ##### 周期・ポイント用
        df = pd.DataFrame(data_shuki,
                          index=index_shuki,
                          columns=columns_shuki)
        df.to_csv(path_shuki)
        # st.dataframe(df)

        ##### 激走チャージ用
        df = pd.DataFrame(data_gekiso,
                          index=index_gekiso,
                          columns=columns_gekiso)
        df.to_csv(path_gekiso)
        

        ##### ライバルモード用
        df = pd.DataFrame(data_rival,
                          index=index_rival,
                          columns=columns_rival)
        df.to_csv(path_rival)
        

        ##### メダル用
        df = pd.DataFrame(data_medal,
                          index=index_medal,
                          columns=columns_medal)
        df.to_csv(path_medal)

        ##### 青島SG用
        df = pd.DataFrame(data_aoshima,
                          index=index_aoshima,
                          columns=columns_aoshima)
        df.to_csv(path_aoshima)


########################################
##### バージョン情報 ####################
########################################
st.caption("ver2.0.0")
st.caption("   ・新規作成")