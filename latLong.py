# from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
geolocator = GoogleV3()
port_CityList = ['Port Massawa', 'Port Tadjoura', 'Port Assab', 'Port Djibouti']
for port_City in port_CityList:
	location = geolocator.geocode(port_City)
	port = location.latitude, location.longitude
	location = geolocator.geocode("Mer Awi")
	destination = location.latitude, location.longitude
	print(port_City, geodesic(port,destination).miles)