import pandas as pd
import os

# 実行ファイルの絶対パスを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# 相対パスを指定して、絶対パスを取得
df_path = "TEST.csv"
absolute_path = os.path.join(script_dir, df_path)

# ===データの摘出、集計==

# CSVファイルを読み込む
df = pd.read_csv(absolute_path)
print(df)

# 条件に合うデータを抽出する
data_s = df[df["国語"] >= 90]
data_c = df[df["数学"] < 70]
print("国語が90点以上 \n",data_s)
print("数学が70点未満 \n",data_c)

# 集計（最大値、最小値、平均値、中央値、合計、、）
print("数学の最高点 = ",df["数学"].max())
print("数学の最低点 = ",df["数学"].min())
print("数学の平均点 = ",df["数学"].mean())
print("数学の中央値 = ",df["数学"].median())
print("数学の合計 = ",df["数学"].sum())