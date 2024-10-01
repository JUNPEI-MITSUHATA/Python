import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib


# 保存用のフォルダを作る
out_folder = Path("./download")
out_folder.mkdir(exist_ok=True)

# ウェブページを取得して解析する
load_url = "https://www.y-mori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# ファイルを書き込みモードで開く
filename = "./Download/img_url.txt"
with open(filename, "w") as f:
    # すべてのaタグを検索し、リンクを絶対URLで書き出す
    for element in soup.find_all("img"):
        src = element.get("src")
        # 絶対パスを取得
        image_url = urllib.parse.urljoin(load_url, src)
        f.write(element.text + "\n")  # リンクのテキストを書き込む
        f.write(image_url + "\n")      # 絶対URLを書き込む
        f.write("\n")