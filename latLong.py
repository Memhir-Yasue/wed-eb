# from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import pandas as pd
import config
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
geolocator = GoogleV3(api_key=config.api_key)
port_CityList = ['Port Massawa', 'Port Assab', 'Port Tadjoura', 'Port Djibouti']
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
# 		for port_City in port_CityList:
# 			location = geolocator.geocode(port_City)
# 			port = location.latitude, location.longitude
# 			location = geolocator.geocode(city)
# 			destination = location.latitude, location.longitude
# 			print(city,'---->', port_City, geodesic(port,destination).miles)

all_data = {
	'city_name' : [],
	'massawa' : [],
	'assab': [],
	'tadjoura': [],
	'djibouti': [],

}



for state_Name in region:
	for city in state_Name:
		all_data['city_name'].append(city)

for port_City in port_CityList:
	data_port = []
	for state_Name in region:
		for city in state_Name:
			dest_City = city + ", Ethiopia" # Make sure towns are in Ethiopia
			location = geolocator.geocode(port_City)
			port = location.latitude, location.longitude
			location = geolocator.geocode(dest_City)
			destination = location.latitude, location.longitude
			distance = geodesic(port,destination).miles
			data_port.append(distance)
			print(city,'---->', port_City, geodesic(port,destination).miles)
	for item in data_port:
		if port_City == 'Port Massawa':
			all_data['massawa'].append(item)
		if port_City == 'Port Assab':
			all_data['assab'].append(item)
		if port_City == 'Port Tadjoura':
			all_data['tadjoura'].append(item)
		if port_City == 'Port Djibouti':
			all_data['djibouti'].append(item)
print(all_data)
df = pd.DataFrame(all_data)
print(df)