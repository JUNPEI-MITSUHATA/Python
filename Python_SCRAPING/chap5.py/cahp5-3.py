import requests
import json
from pprint import pprint

# test2.jsonから情報を表示
""" 
with open("test2.json", mode="r") as f:
    jsondata = json.loads(f.read())
    print("１つ目のオブジェクト＝　",jsondata[0])
    print("都市名＝　",jsondata[0]["name"])
    print("緯度　＝　",jsondata[0]["coord"]["lat"])
    print("経度　＝　",jsondata[0]["coord"]["lon"])
"""

# 現在の天気を取得する：東京
url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Tokyo,JP", key="833710dc5c910a0d03fe31bdcaa4ef6c")
jsondata = requests.get(url).json()
print("日付　＝　",jsondata["list"][0]["dt_txt"])
print("都市名＝　",jsondata["city"]["name"])
print("気温　＝　",jsondata["list"][0]["main"]["temp"])
print("天気　＝　",jsondata["list"][0]["weather"][0]["description"])

# 郵便番号から現在の天気を取得する：東京
url2 = "http://api.openweathermap.org/data/2.5/forecast?zip={zipcode}&appid={key}&lang=ja&units=metric"
url2 = url2.format(zipcode="160-0006,JP", key="833710dc5c910a0d03fe31bdcaa4ef6c")
jsondata2 = requests.get(url2).json()
pprint(jsondata2)
print("日付　＝　",jsondata2["list"][0]["dt_txt"])
print("都市名＝　",jsondata2["city"]["name"])
print("気温　＝　",jsondata2["list"][0]["main"]["temp"])
print("天気　＝　",jsondata2["list"][0]["weather"][0]["description"])