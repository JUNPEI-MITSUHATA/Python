# ライブラリのインストール
""" 
■ folium(フォリウム)
  地図を扱うライブラリ
>pip3 install folium
"""
# Path操作に使用_基本ライブラリ
import os
# deta処理用の外部ライブラリ
import pandas as pd
# pandasライブラリのグラフ作成用ライブラリ
import matplotlib.pyplot as plt
# グラフなどの出力結果の日本語を文字化け防止_外部ライブラリ
import matplotlib_fontja
# 地図を扱うライブラリー
import folium



# 実行ファイルの絶対パスを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# 相対パスを指定して、絶対パスを取得
df_path = "人口動態.csv"
absolute_path = os.path.join(script_dir, df_path)

# ===e-statのオープンデータ_CSVを読み・グラフの作成・処理===

# CSVファイルを読み込む
df = pd.read_csv(absolute_path,index_col="全国・都道府県", encoding="shift_jis")
print (df['2022年'])
print (df['2023年'])

# ,を””に置換
df['2023年'] = pd.to_numeric(df['2023年'].str.replace(",",""))
df['2022年'] = pd.to_numeric(df['2022年'].str.replace(",",""))

# 全国を削除
df = df.drop("全国", axis=0)
# 2023-2022で差を求める
df["人口増減"] = df['2023年'] - df['2022年']
# 人口の昇順
df = df.sort_values('人口増減', ascending=False)
# figsize=(w,h) ウィンドウの大きさ
df['人口増減'].plot.bar(figsize=(10,6))
# 縦軸のスケールの調整
plt.ylim(-60, 60)

plt.show()


# === pandas x folium ===
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