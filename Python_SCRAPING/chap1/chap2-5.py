import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する。
url ="https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

# IDで検索して、そのタグの中身を表示
chap2 = soup.find(id="chap2")
print(chap2)

# IDで検索して、その中のすべてのliタグを検索して表示
chap2 = soup.find(id="chap2")
for element in chap2.find_all("li"):
    print(element.text)