import streamlit as st
import pandas as pd

# Streamlitアプリの作成
st.title('財務分析')

# CSVファイルのアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

if uploaded_file is not None:
    # CSVファイルからデータフレームに変換
    df = pd.read_csv(uploaded_file)

    # 表示する列を選択
    columns = df.columns.tolist()
    selected_columns = st.multiselect("表示する列を選択してください", columns, default=columns)

    # 選択された列のみを表示
    st.write('## 財務諸表データ')
    st.dataframe(df[selected_columns])

    # 財務指標の計算
    if '総資産' in df.columns and '純資産' in df.columns and '利益剰余金' in df.columns and '株主資本' in df.columns:
        df['負債総額'] = df['総資産'] - df['純資産']
        df['ROE'] = (df['利益剰余金'] / df['株主資本']) * 100
        df['ROA'] = (df['利益剰余金'] / df['総資産']) * 100

        # 財務指標の表示
        st.write('## 財務指標')
        st.write(f"負債総額: {df['負債総額'][0]:,.0f} 円")
        st.write(f"ROE (自己資本利益率): {df['ROE'][0]:.2f} %")
        st.write(f"ROA (総資産利益率): {df['ROA'][0]:.2f} %")
    else:
        st.warning("必要な列（総資産, 純資産, 利益剰余金, 株主資本）がCSVに含まれていません。")
else:
    st.info("CSVファイルをアップロードしてください。")
