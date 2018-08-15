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




def port_geocord():
	port_geocode = []
	for port_city in port_cityList:
		port = geolocator.geocode(port_city)
		start = port.latitude, port.longitude
		port_geocode.append(start)
	return port_geocode


def destination_geocord():
	destination_geocord = []
	for state_Name in region:
		for city in state_Name:
			dest_city = city + ", Ethiopia"
			destination = geolocator.geocode(dest_city)
			end = destination.latitude, destination.longitude
			destination_geocord.append(end)
	return destination_geocord



def distance_calculator(port_geocode):
	straight_distance = []
	for state_Name in region:
	for city in state_Name:
		# dest_city = city + ", Ethiopia" 
		# destination = geolocator.geocode(dest_city)
		# end = destination.latitude, destination.longitude
		port_geocode_index = 0
		for port_city in port_cityList:
			start = port_geocode[port_geocode_index]
			port_geocode_index+=1
			distance = geodesic(start,end).miles
			straight_distance.append(distance)
			print(city,'---->', port_city,distance) 
	return straight_distance






def main():
	port_geocode()
	distance_calculator(port_geocode)


