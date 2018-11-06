import pandas as pd
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import googlemaps
from datetime import datetime
import config
import json


geolocator = GoogleV3(api_key=config.api_key)
gmaps = googlemaps.Client(key=config.maps_api_key)

port_cityList = ['Massawa Port Authority', 'Assab Port']
tigray = ['Himora','Shire']
amhara = ['Weldiya', 'Mersa']
region = [tigray, amhara]

port_geocord = []
destination_geocord = []
elevation = []
straight_distance = []
city_name_list = []
data_road_distance = []
data_road_duration = []




def func_port_geocord():
	for port_city in port_cityList:
		if port_city == 'Port de Doraleh, Djibouti': 
			start = '11.578054, 43.094573'
			port_geocord.append(start)
		else:
			port = geolocator.geocode(port_city)
			start = str(port.latitude)+','+str(port.longitude)
			port_geocord.append(start)
			print('raw',start)
	print(port_geocord)
	return port_geocord

def append_city_name():
	for state_Name in region:
		for city in state_Name:
			city_name_list.append(city)
	return city_name_list

# def elevation():
# 	ELEVATION_BASE_URL = 'http://maps.googleapis.com/maps/api/elevation/json?'
# 	URL_PARAMS = "locations=%s,%s&sensor=%s" % (lati, lngi, "false")
# 	url=ELEVATION_BASE_URL + URL_PARAMS
# 	with urllib.request.urlopen(url) as f:
# 		response = json.loads(f.read().decode())    
# 		status = response["status"]
# 		result = response["results"][0]
# 	height = str(result["elevation"] * 3.28084)
# 	elevation.append(height)

def func_destination_geocord():
	for city in city_name_list:
		dest_city = city + ", Ethiopia"
		destination = geolocator.geocode(dest_city)
		end = str(destination.latitude)+','+str(destination.longitude)
		destination_geocord.append(end)
		print(city,end)
	return destination_geocord



def straight_distance_calculator(port_geocord, destination_geocord):
    for dest_cord in destination_geocord:
    	end = dest_cord
    	for port_cord in port_geocord:
    		start = port_cord # Get cord for ports
    		distance = geodesic(start,end).miles # calculate distance
    		straight_distance.append(distance)
    		print(dest_cord,'---->', port_cord,distance)
    return straight_distance




def driving_distance_calculator(port_geocord, destination_geocord):
	for dest_cord in destination_geocord:
		end = dest_cord
		now = datetime.now()
		for port_cord in port_geocord:
			start = port_cord
			print(start,end,type(start),type(end))
			directions_result = gmaps.distance_matrix(start,
                        		end,
                        		mode="driving",
                                departure_time=now,
                                units='imperial')
			print(directions_result)
			road_distance = directions_result['rows'][0]['elements'][0]['distance']['text']
			data_road_distance.append(road_distance)
			road_duration = directions_result['rows'][0]['elements'][0]['duration']['value']
			data_road_duration.append(road_duration)
	print(start,'--->','end',road_distance,road_duration)
	return road_distance,road_duration

# def test():
# 	for port_city in port_cityList:
# 		port = geolocator.geocode(port_city)
# 		start = str(port.latitude)+','+str(port.longitude) 
# 		print(start,type(start))
# 		break


def main():
	# test()
	func_port_geocord()
	append_city_name()
	func_destination_geocord()
	# # # straight_distance_calculator(port_geocord,destination_geocord)
	driving_distance_calculator(port_geocord,destination_geocord)


main()
