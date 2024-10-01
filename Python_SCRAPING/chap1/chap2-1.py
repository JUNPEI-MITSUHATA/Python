import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する。
url ="https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

print(soup)
