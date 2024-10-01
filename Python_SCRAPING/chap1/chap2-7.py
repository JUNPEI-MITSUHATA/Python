import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する。
url ="https://www.yahoo.co.jp/"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")


# IDで検索して、その中のすべてのliタグを検索して表示
news = soup.find(id="tabpanelTopics1")
for element in news.find_all("a"):
    print(element.text)