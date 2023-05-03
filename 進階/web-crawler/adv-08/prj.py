import requests
import os
import sys
import datetime

os.chdir(sys.path[0])
api_Key = "892da2f13edf3c7f382637760e72d224"
base_url = "https://api.openweathermap.org/data/2.5/onecall?"
lon = "121.5319"
lat = "25.0478"
exclude = "minutely,horuly"
units = "metric"
lang = "zh_tw"
send_url = base_url
send_url += "lat=" + lat
send_url += "&lon=" + lon
send_url += "&exclude=" + exclude
send_url += "&appid=" + api_Key
send_url += "&units=" + units
send_url += "&lang=" + lang
print(send_url)
response = requests.get(send_url)
info = response.json()

if "daily" in info.keys():
    for i in range(7):
        temp = info["daily"][i]["temp"]["day"]
        time = datetime.datetime.fromtimestamp(
            info["daily"][i]["dt"]).strftime("%m/%d")
        print(f"{time}={temp}")
else:
    print(" fail")

# print(info)
# print(info["main"]["temp"])
# print(info["name"])
# print(info["weather"][1]["description"])
# if "main" in info.keys():
#     icon_code = info["weather"][0]["icon"]
#     icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
#     response = requests.get(icon_url)
#     with open(f"{icon_code}.png", "wb") as icon_file:
#         icon_file.write(response.content)
# else:
#     print(" CZity Not Found")