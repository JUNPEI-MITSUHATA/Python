import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
import os

# matplotlib_fontja.japanize()

# 実行ファイルの絶対パスを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# 相対パスを指定して、絶対パスを取得
df_path = "TEST.csv"
absolute_path = os.path.join(script_dir, df_path)
png_path = os.path.join(script_dir, "bargraph.png")

# ===データからグラフの作成===

# CSVファイルを読み込む
df = pd.read_csv(absolute_path,index_col=0)
print(df)

# グラフを作って表示する(変化を見たい時)
df.plot()
plt.show()
# 棒グラフを作って表示(値の代償を見たい時)
df.plot.bar()
plt.legend(loc="lower right")
plt.show()
# 棒グラフ(水平)を作って表示
df.plot.barh()
plt.legend(loc="lower left")
plt.show()
# 積み上げ棒グラフ(変化の要因を見たい時)
df.plot.bar(stacked=True)
plt.legend(loc="lower right")
plt.show()
# 箱ひげグラフ(データの散らばりを見たい時)
df.plot.box()
plt.show()
# 面グラフ(変化の大きさを強調したい時)
df.plot.area()
plt.legend(loc="lower right")
plt.show() 

# 国語の棒グラフ
df["国語"].plot.barh()
plt.legend(loc="lower left")
plt.show()
# 国語と数学の棒グラフ
df[["国語","数学"]].plot.barh()
plt.legend(loc="lower left")
plt.show()
# C子の棒グラフ
df.loc["C子"].plot.barh()
plt.legend(loc="lower left")
plt.show()
# C子の円グラフ
df.loc["C子"].plot.pie(labeldistance=0.6)
plt.legend(loc="lower left")
plt.show()

# 行と列の表示を入れ替える(列ごとのグラフ作成)
df.T.plot.bar()
plt.legend(loc="lower right")
plt.show()

# 棒グラフのカラー選択、画像で出力
colorlist = ["skyblue","steelblue","tomato","cadetblue","orange","sienna"]
df.T.plot.bar(color=colorlist)
plt.legend(loc="lower right")
plt.savefig(png_path)