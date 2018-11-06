import googlemaps
import config

gmaps = googlemaps.Client(key=config.maps_api_key)
result = gmaps.geocode('Nefas, Ethiopia')

state = result[0]['address_components'][2]['long_name']

zone = result[0]['address_components'][1]['long_name']
print(zone,state)