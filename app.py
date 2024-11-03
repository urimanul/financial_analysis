import streamlit as st
import pandas as pd
import csv, os
import numpy as np

#対象のファイルのパス文字列を指定
file_path = os.path.join(".","fy-balance-sheet.csv")
print("file name:" + file_path)

#CSVファイルからdfへ変換
df = pd.read_csv(file_path)

#読み込んだデータの表示
df.head()

#df = pd.DataFrame(data)

# Streamlitアプリの作成
st.title('財務分析')

# データの表示
st.write('## 財務諸表データ')
st.dataframe(df)

# 財務指標の計算
df['負債総額'] = df['総資産'] - df['純資産']
df['ROE'] = (df['利益剰余金'] / df['株主資本']) * 100
df['ROA'] = (df['利益剰余金'] / df['総資産']) * 100

# 財務指標の表示
st.write('## 財務指標')
st.write(f"負債総額: {df['負債総額'][0]:,.0f} 円")
st.write(f"ROE (自己資本利益率): {df['ROE'][0]:.2f} %")
st.write(f"ROA (総資産利益率): {df['ROA'][0]:.2f} %")
