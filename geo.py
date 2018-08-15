import pandas as pd
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import googlemaps
import config


geolocator = GoogleV3(api_key=config.api_key)
gmaps = googlemaps.Client(key=config.maps_api_key)

port_cityList = ['Massawa Port Authority', 'Assab Port']
tigray = ['Himora','Shire']
amhara = ['Weldiya', 'Mersa']
region = [tigray, amhara]

port_geocord = []
destination_geocord = []
straight_distance = []
elevation = []
city_name_list = []



def func_port_geocord():
	for port_city in port_cityList:
		if port_city == 'Port de Doraleh, Djibouti': 
			start = '11.578054, 43.094573'
			port_geocord.append(start)
		else:
			port = geolocator.geocode(port_city)
			start = port.latitude, port.longitude
			port_geocord.append(start)
	return port_geocord

def append_city_name():
	for state_Name in region:
		for city in state_Name:
			city_name_list.append(city)
	return city_name_list

def func_destination_geocord():
	for city in city_name_list:
		dest_city = city + ", Ethiopia"
		destination = geolocator.geocode(dest_city)
		end = destination.latitude, destination.longitude
		destination_geocord.append(end)
		print(city,destination_geocord)
	return destination_geocord



def straight_distance_calculator(port_geocord, destination_geocord,straight_distance):
    for dest_cord in destination_geocord:
    	end = dest_cord
    	for port_cord in port_geocord:
    		start = port_cord # Get cord for ports
    		distance = geodesic(start,end).miles # calculate distance
    		straight_distance.append(distance)
    		print(dest_cord,'---->', port_cord,distance) 
    return straight_distance

def elevation():
	ELEVATION_BASE_URL = 'http://maps.googleapis.com/maps/api/elevation/json?'
	URL_PARAMS = "locations=%s,%s&sensor=%s" % (lati, lngi, "false")
	url=ELEVATION_BASE_URL + URL_PARAMS
	with urllib.request.urlopen(url) as f:
		response = json.loads(f.read().decode())    
		status = response["status"]
		result = response["results"][0]
	height = str(result["elevation"] * 3.28084)
	elevation.append(height)


# def driving_distance_calculator

def main():
	# func_port_geocord()
	append_city_name()
	func_destination_geocord()
	# straight_distance_calculator(port_geocord,destination_geocord,straight_distance)

main()