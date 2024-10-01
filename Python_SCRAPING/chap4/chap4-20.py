import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
import folium



# 実行ファイルの絶対パスを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# 相対パスを指定して、絶対パスを取得

df_path = "店舗.csv"
absolute_path = os.path.join(script_dir, df_path)

# ===データシティ鯖江のオープンデータ_CSVを読み・グラフの作成===

# CSVファイルを読み込む
df = pd.read_csv(absolute_path)
print (len(df))
print (df.columns.values)

# 店舗のある拠点（緯度,経度）をリスト化する
store = df[["緯度","経度","店舗名(日本語)"]].values
print(len(store))
print(store)

# 地図を作って書き出す
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)

for data in store:
    folium.Marker([data[0],data[1]],tooltip=data[2]).add_to(m)
m.save("store.html")

