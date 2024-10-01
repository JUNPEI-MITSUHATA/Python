import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
import folium



# 実行ファイルの絶対パスを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# 相対パスを指定して、絶対パスを取得

df_path = "消火栓.csv"
absolute_path = os.path.join(script_dir, df_path)

# ===データシティ鯖江のオープンデータ_CSVを読み・グラフの作成===

# CSVファイルを読み込む
df = pd.read_csv(absolute_path, encoding="shift_jis")
print (df.columns.values)

# 消火栓のある拠点（緯度,経度）をリスト化する
hydrant = df[["緯度","経度"]].values
print(len(hydrant))
print(hydrant)

# 地図を作って書き出す
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)

# 全ての消火栓にマークをつける
for data in hydrant:
    folium.Marker([data[0],data[1]]).add_to(m)
m.save("sabae.html")