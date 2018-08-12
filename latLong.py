# from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
geolocator = GoogleV3()
# port_City = ["Port Massawa", "Port Tadjoura", "Port Assab", "Port Djibouti"]
location = geolocator.geocode(" Port Tadjoura")
port = location.latitude, location.longitude
location = geolocator.geocode("Mer Awi")
destination = location.latitude, location.longitude

print(geodesic(port,destinationf).miles)