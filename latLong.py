# from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import pandas as pd
import config
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
geolocator = GoogleV3(api_key=config.api_key)
port_cityList = ['Port Massawa', 'Port Assab', 'Port Tadjoura', 'Port Djibouti']
# tigray = ['Himora','Shire', 'Aksum']
tigray = ['Himora','Shire', 'Aksum', 'Adwa', 'Adigrat', 'Negash'
		 'Mekele', 'Ambalage', 'Korem', 'Alamta']
region = [tigray]
###############################
# for state in region:
# 	for city in state:		Basic Template for accessing cities from region
# 		print(city)
##############################

# for state_Name in region:
# 	for city in state_Name: # Destination city
# 		city = city + ", Ethiopia" # Make sure towns are in Ethiopia
# 		for port_city in port_cityList:
# 			location = geolocator.geocode(port_city)
# 			port = location.latitude, location.longitude
# 			location = geolocator.geocode(city)
# 			destination = location.latitude, location.longitude
# 			print(city,'---->', port_city, geodesic(port,destination).miles)

all_data = {
	'city_name' : [],
	'massawa' : [],
	'assab': [],
	'tadjoura': [],
	'djibouti': [],
	'latitude': [],
	'longitude': [],

}

# for state_Name in region:
# 	for city in state_Name:
# 		all_data['city_name'].append(city) # Add city as dict key to city_name

# 		city_address = geolocator.geocode(dest_city)
# 		latitude = city_address.latitude
# 		all_data['latitude'].append(latitude)
# 		longitude = city_address.longitude
# 		all_data['longitude'].append(longitude)

for port_city in port_cityList:
	data_port = []
	for state_Name in region:
		for city in state_Name:
			dest_city = city + ", Ethiopia" # Make sure towns are in Ethiopia
			location = geolocator.geocode(port_city)
			port = location.latitude, location.longitude
			location = geolocator.geocode(dest_city)
			destination = location.latitude, location.longitude
			distance = geodesic(port,destination).miles
			data_port.append(distance)

			if port_city == 'Port Massawa': # To Append all city names, and lat/long info to dict key once only
				all_data['city_name'].append(city)
				latitude = location.latitude
				all_data['latitude'].append(latitude)
				longitude = location.longitude
				all_data['longitude'].append(longitude)

			print(city,'---->', port_city, geodesic(port,destination).miles)
	for item in data_port:
		if port_city == 'Port Massawa':
			all_data['massawa'].append(item)
		if port_city == 'Port Assab':
			all_data['assab'].append(item)
		if port_city == 'Port Tadjoura':
			all_data['tadjoura'].append(item)
		if port_city == 'Port Djibouti':
			all_data['djibouti'].append(item)
df = pd.DataFrame(all_data)
print(df)