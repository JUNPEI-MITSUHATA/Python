import pandas as pd
import os

# 実行ファイルの絶対パスを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# 相対パスを指定して、絶対パスを取得
df_path = "13TOKYO.CSV"
absolute_path = os.path.join(script_dir, df_path)

# ===郵便局のオープンデータ_CSVを読み・操作===

# CSVファイルを読み込む
df = pd.read_csv(absolute_path,header=None, encoding="shift_jis")
print(len(df))
print(df.columns.values)

# 「2」の列が「1600006」の住所を抽出して表示
results = df[df[2] == 1600006]
print(results[[2,6,7,8]])

# 「8」の列が「四谷」の住所を抽出して表示
results = df[df[8] == "四谷"]
print(results[[2,6,7,8]])
# 「8」の列が「四谷」を含む住所を抽出して表示
results = df[df[8].str.contains("四谷")]
print(results[[2,6,7,8]])