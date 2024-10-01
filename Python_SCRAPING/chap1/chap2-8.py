import requests
from bs4 import BeautifulSoup

# 相対→絶対Path変更ライブラリー
import urllib

# Webページを取得して解析する。
url ="https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのaタグを検索して、リンクを表示
for element in soup.find_all("a"):
    print(element.text)
    a_url = element.get("href")
    print(a_url)

# 相対URLを絶対Pathで表示
link_url = urllib.parse.urljoin(url, a_url)
print(link_url)