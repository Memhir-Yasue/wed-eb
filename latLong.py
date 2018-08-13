# from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
geolocator = GoogleV3()
port_CityList = ['Port Massawa', 'Port Assab', 'Port Tadjoura' , 'Port Djibouti']
tigray = ['Himora','Shire', 'Aksum', 'Adwa', 'Adigrat', 'Negash'
		 'Mekele', 'Ambalage', 'Korem', 'Alamta']
region = [tigray]
###############################
# for state in region:
# 	for city in state:		Basic Template for acessing cities from region
# 		print(city)
##############################
for state in region:
	for city in state: # Destination city
		for port_City in port_CityList:
			location = geolocator.geocode(port_City)
			port = location.latitude, location.longitude
			location = geolocator.geocode(city)
			destination = location.latitude, location.longitude
			print(city,'---->', port_City, geodesic(port,destination).miles)