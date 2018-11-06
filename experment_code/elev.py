import urllib.request
import json
lati = 9.019630
lngi =  38.755647
# url_params completes the base url with the given latitude and longitude values
ELEVATION_BASE_URL = 'http://maps.googleapis.com/maps/api/elevation/json?'
URL_PARAMS = "locations=%s,%s&sensor=%s" % (lati, lngi, "false")
url=ELEVATION_BASE_URL + URL_PARAMS
with urllib.request.urlopen(url) as f:
	response = json.loads(f.read().decode())    
	status = response["status"]
	# result = response["results"][0]

# height = str(result["elevation"] * 3.28084)


print(status)
