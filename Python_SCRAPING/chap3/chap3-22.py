import pandas as pd
import openpyxl
import os

# 実行ファイルの絶対パスを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# 相対パスを指定して、絶対パスを取得
df_path = "TEST.csv"
absolute_path = os.path.join(script_dir, df_path)

# ===CSVをExcelで表示===

# CSVファイルを読み込む
df = pd.read_csv(absolute_path)
print(df)

# ソート(国語の点数が高い順)
kokugo = df.sort_values("国語",ascending=False)

# Excelファイルに出力
# index = Falae 先頭のindex値を非表示
with pd.ExcelWriter("csv_to_excel3.xlsx") as writer:
    df.to_excel(writer, index=False, sheet_name="元のデータ")
    kokugo.to_excel(writer,index=False,sheet_name="国語でソート")