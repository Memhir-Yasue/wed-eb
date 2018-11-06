import urllib.request
import json
import config

# Your Bing Maps Key 
bingMapsKey = config.bing_api_key

# input information
start = 'Addis, Ababa'
destination = "Asmara, Eritrea"

encodedStart = urllib.parse.quote(start, safe='')
encodedDest = urllib.parse.quote(destination, safe='')

routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + encodedStart + "&wp.1=" + encodedDest + "&key=" + bingMapsKey


request = urllib.request.Request(routeUrl)
response = urllib.request.urlopen(request)

r = response.read().decode(encoding="utf-8")
result = json.loads(r)
print(result["resourceSets"][0]["resources"][0]['travelDistance'])
print(result["resourceSets"][0]["resources"][0]['travelDuration'])
# itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]

# for item in itineraryItems:
#     print(item["instruction"]["text"])