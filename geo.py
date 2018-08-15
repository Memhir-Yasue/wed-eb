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




def func_port_geocord(port_geocord):
	for port_city in port_cityList:
		if port_city == 'Port de Doraleh, Djibouti': 
			start = '11.578054, 43.094573'
			port_geocord.append(start)
		else:
			port = geolocator.geocode(port_city)
			start = port.latitude, port.longitude
			port_geocord.append(start)
	return port_geocord


def func_destination_geocord(destination_geocord):
	for state_Name in region:
		for city in state_Name:
			dest_city = city + ", Ethiopia"
			destination = geolocator.geocode(dest_city)
			end = destination.latitude, destination.longitude
			destination_geocord.append(end)
			print(city,destination_geocord)
	return destination_geocord



def straight_distance_calculator(port_geocord, destination_geocord,straight_distance):
	# for state_Name in region:
	# 	dest_index = 0
	# 	for city in state_Name:
	# 		end = destination_geocord[dest_index]
	# 		dest_index+=1
	# 		port_geocord_index = 0
    for dest_cord in destination_geocord:
    	end = dest_cord
    	for port_city in port_geocord:
    		start = port_city # Get cord for ports
    		distance = geodesic(start,end).miles # calculate distance
    		straight_distance.append(distance)
    		print('---->', port_city,distance) 
    return straight_distance

def elevation(elevation):
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
	port_geocord = []
	destination_geocord = []
	straight_distance = []
	elevation = []
	func_port_geocord(port_geocord)
	func_destination_geocord(destination_geocord)
	straight_distance_calculator(port_geocord,destination_geocord,straight_distance)

main()