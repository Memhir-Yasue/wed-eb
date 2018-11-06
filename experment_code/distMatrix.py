import googlemaps
from datetime import datetime
import config
import json

gmaps = googlemaps.Client(key=config.maps_api_key)

# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.distance_matrix("Himora, Ethiopia",
                                     "Port Djibouti",
                                     mode="driving",
                                     departure_time=now)


distance = directions_result['rows'][0]['elements'][0]['distance']['text']
duration = directions_result['rows'][0]['elements'][0]['duration']['value']
print(directions_result)


# distance = directions_result[0]['legs'][0]['distance']['text'] // From directions API
# duration = directions_result[0]['legs'][0]['duration']['text']
# print(duration)


                                     # ,departure_time=now)