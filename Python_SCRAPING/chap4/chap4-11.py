import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja



# 実行ファイルの絶対パスを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# 相対パスを指定して、絶対パスを取得
file_names = ["平均気温.csv", "最高気温.csv", "最低気温.csv"]
absolute_paths = [os.path.join(script_dir, file_name) for file_name in file_names]
print (absolute_paths[0])
print (absolute_paths[1])
print (absolute_paths[2])


# ===キッズすたっとのオープンデータ_CSVを読み・グラフの作成===

# CSVファイルを読み込む
df1 = pd.read_csv(absolute_paths[0], index_col="時点")
df2 = pd.read_csv(absolute_paths[1], index_col="時点")
df3 = pd.read_csv(absolute_paths[2], index_col="時点")
print (df1.columns.values)
print (df2.columns.values)
print (df3.columns.values)

# 折れ線グラフで表示
df1["東京都"].plot()
df2["東京都"].plot()
df3["東京都"].plot()
plt.ylim(-5,35)
plt.show()
