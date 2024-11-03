#対象のファイルのパス文字列を指定
file_path = os.path.join(".","fy-balance-sheet.csv")
print("file name:" + file_path)

#CSVファイルからdfへ変換
df = pd.read_csv(file_path)

#読み込んだデータの表示
df.head()
