# from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import config
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
geolocator = GoogleV3(api_key=config.api_key)
port_CityList = ['Port Massawa', 'Port Assab', 'Port Tadjoura' , 'Port Djibouti']
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
# 		dest_City = city + ", Ethiopia" # Make sure towns are in Ethiopia
# 		for port_City in port_CityList:
# 			location = geolocator.geocode(port_City)
# 			port = location.latitude, location.longitude
# 			location = geolocator.geocode(dest_City)
# 			destination = location.latitude, location.longitude
# 			print(city,'---->', port_City, geodesic(port,destination).miles)

for port_City in port_CityList:
	for state_Name in region:
		for city in state_Name:
			dest_City = city + ", Ethiopia" # Make sure towns are in Ethiopia
			location = geolocator.geocode(port_City)
			port = location.latitude, location.longitude
			location = geolocator.geocode(dest_City)
			destination = location.latitude, location.longitude
			print(city,'---->', port_City, geodesic(port,destination).miles)