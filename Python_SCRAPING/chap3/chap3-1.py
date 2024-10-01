import pandas as pd
import os

# 実行ファイルの絶対パスを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# 相対パスを指定して、絶対パスを取得
df_path = "TEST.csv"
absolute_path = os.path.join(script_dir, df_path)

# ===データの表示、列行の追加、削除===

# CSVファイルを読み込む
df = pd.read_csv(absolute_path)
print(df)

# データの情報を表示
print("データ件数=",len(df) )
print("項目名=", df.columns.values)
print("インデックス=", df.index.values)

# 1列データの取得
print("国語の列データ\n",df["国語"])
# 複数列データの取得
print("国語と数学の列データ\n",df[["国語","数学"]])

# 1行のデータを取得
print("C子のデータ\n",df.loc[2])
# 複数行のデータを取得
print("C子のとD郎のデータ\n",df.loc[[2,3]])
# 指定行の指定列のデータ
print("C子の国語データ\n",df.loc[2]["国語"])

# 1列データの追加
df["美術"] = [68,73,82,77,94,96] 
print("列データ(美術)を追加\n", df)
# 1行データの追加
df.loc[6] = ["G恵",90,92,94,96,92,98]
print("行データ(G恵)を追加\n",df)

# 「美術」列を削除
print("\n「美術」列を削除\n",df.drop("美術",axis=1))
# indexの6目(G恵)を削除
print("\n(G恵行)を削除\n",df.drop(6,axis=0))
