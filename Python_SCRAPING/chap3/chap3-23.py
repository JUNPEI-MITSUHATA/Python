import pandas as pd
import openpyxl
import os

# 実行ファイルの絶対パスを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# 相対パスを指定して、絶対パスを取得
df_path = "TEST.csv"
absolute_path = os.path.join(script_dir, df_path)
# excel_path = os.path.join(script_dir, "csv_to_excel1.xlsx")

# ===Excelを読み込み表示===

# Excelファイルを読み込む
df = pd.read_excel("csv_to_excel3.xlsx")
print(df)
df = pd.read_excel("csv_to_excel3.xlsx", sheet_name="国語でソート")
print(df)