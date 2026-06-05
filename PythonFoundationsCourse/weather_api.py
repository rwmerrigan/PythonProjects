# api key - b062659974cf443ba7d171322262705
# call - http://api.weatherapi.com/v1/current.json?key=b062659974cf443ba7d171322262705&q=Irvine&aqi=no

import requests

city = 'Irvine'
url = 'http://api.weatherapi.com/v1/current.json?key=b062659974cf443ba7d171322262705&q=' + city + '&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, "is", description, 'and', temp, 'degrees')
