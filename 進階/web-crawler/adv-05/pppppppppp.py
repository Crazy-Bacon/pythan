import requests

api_Key = "892da2f13edf3c7f382637760e72d224"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name :")
units = "metric"
lang = "zh_tw"
send_url = base_url
send_url += "appid=" + api_Key
send_url += "&q=" + city_name
send_url += "&untis=" + units
send_url += "&lang=" + lang
print(send_url)