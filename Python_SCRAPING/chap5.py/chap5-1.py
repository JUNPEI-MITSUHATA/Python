import requests
import json

# format構文
ans = "今日は{Key1}です。明日は{Key2}です。"
print(ans)

ans = ans.format(Key1 = "晴れ", Key2 = "曇り")
print(ans)

url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Kobe", key="833710dc5c910a0d03fe31bdcaa4ef6c")

jsondata = requests.get(url).json()
print(jsondata)