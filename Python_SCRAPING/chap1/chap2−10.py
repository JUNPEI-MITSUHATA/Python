import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib


# 保存用のフォルダを作る
out_folder = Path("./MY_PYTHON/Python_スクレイピング/download")
out_folder.mkdir(exist_ok=True)

# ウェブページを取得して解析する
load_url = "https://www.y-mori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# ファイルを書き込みモードで開く
filename = "./MY_PYTHON/Python_スクレイピング/linklist.txt"
with open(filename, "w") as f:
    # すべてのaタグを検索し、リンクを絶対URLで書き出す
    for element in soup.find_all("a"):
        url = element.get("href")
        link_url = urllib.parse.urljoin(load_url, url)
        f.write(element.text + "\n")  # リンクのテキストを書き込む
        f.write(link_url + "\n")      # 絶対URLを書き込む
        f.write("\n")
