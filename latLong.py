# from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import googlemaps
from datetime import datetime
import pandas as pd
import config
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
geolocator = GoogleV3(api_key=config.api_key)
gmaps = googlemaps.Client(key=config.maps_api_key)

port_cityList = ['Port Massawa', 'Port Assab', 'Port Tadjoura', 'Port de Doraleh, Djibouti',
'Port of Mogadishu','Berbera Port', 'Mokowe, Kenya'
]

tigray = ['Himora','Shire', 'Aksum', 'Adwa', 'Adigrat', 'Negash',
		 'Mekele', 'Ambalage', 'Korem', 'Alamta']

amhara = ['Weldiya', 'Mersa', 'Dessie', 'Kombolcha',
'Senbete', 'Molale', 'Ankober', 'Debre Birhan',
'Rema', 'Merkane Selam', 'Mertule Maryam',
'Felege Birhan', 'Zebich', 'Dejen', 'Debre Markos', 'Dembecha',
'Bure','Injibara', 'Dangla', 'Durbete', 'Mer Awi', 'Bahir Dar',
'Addis Zemen', 'Gondar', 'Amba Giorgis', 'Dabat', 'Debark',
'Chew Ber', 'Amdework', 'Sekota', 'Lalibela', 'Gashena', 'Wegel Tena',
'Tenta', 'Akesta', 'Metema', 'Shawira'
]

afar = [
'Berhale', 'Eli Dar', 'Semera', 'Gewana', 'Awash'
]

gambella = [
'Gambela', 'Abobo'
]

federal = [
'Addis Ababa', 'Harar', 'Dire Dawa'
]

somali = [
'Jijiga', 'kebri beyah', 'Degeh Bur', 'Bircot','Shekosh','Kebri Dehar',
'Shilabo','Kelafo','Mustahil','Danan','Imi',
'Melka Chireti','Bogol','Fiq'
]

debub = [
'Butajira','Agena','Hosaena','Alba Kulito','Areka',
'Tarcha','Sodo','Yirga Alem','Dilla','Arba Minch','konso',
'Masha','Gecha','Mizan Teferi','Bonga','Shishinda',
'Omorate','Turmi','Ganda','Welkite'
]


oromiya = [
'Gimbi','Dembi Dolo','Dongoro','Nekemte','Ambo',
'Bishoftu','Adama','Meiso','Karamile','Raaso',
'Delo','Dinsho','Assela','Tiya','Asasa',
'Sashamane','Finchawa','Hagere Maryam','Kibre Mengist',
'Wadera','Negele','Udet','Filtu','Moyala',
'Wachile','Mega','Yebelo','Addis Alem','Waliso','Jimma',
'Agaro','Ziway','Awassa','Fiche','Mendi'
]

benshangul = [
'Asosa','Menge','Guba','Debre Zeyit'
]

region = [tigray, amhara, afar, gambella, oromiya, federal, somali, benshangul, debub]
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

	'massawa_straight_distance' : [],
	'assab_straight_distance': [],
	'tadjoura_straight_distance': [],
	'djibouti_straight_distance': [],
	'mogadishu_straight_distance': [],
	'berbera_straight_distance': [],
	'lamu_straight_distance': [],

	'massawa_road_distance' : [],
	'assab_road_distance': [],
	'tadjoura_road_distance': [],
	'djibouti_road_distance': [],
	'mogadishu_road_distance': [],
	'berbera_road_distance': [],
	'lamu_road_distance': [],

	'massawa_road_duration' : [],
	'assab_road_duration': [],
	'tadjoura_road_duration': [],
	'djibouti_road_duration': [],
	'mogadishu_road_duration': [],
	'berbera_road_duration': [],
	'lamu_road_duration': [],

	'latitude': [],
	'longitude': [],

}

for port_city in port_cityList:
	data_straight_distance = []
	data_road_distance = []
	data_road_duration = []
	for state_Name in region:
		for city in state_Name:
			dest_city = city + ", Ethiopia" # Make sure towns are in Ethiopia
			port = geolocator.geocode(port_city)
			start = port.latitude, port.longitude
			destination = geolocator.geocode(dest_city)
			end = destination.latitude, destination.longitude
			straight_distance = geodesic(start,end).miles
			data_straight_distance.append(straight_distance)
			# Getting driving distance and duration
			now = datetime.now()
			if port_city == 'Port de Doraleh, Djibouti': # Getting around an error between himora and djibouti
				start = '11.578054, 43.094573'
				directions_result = gmaps.directions(start,
                                     end,
                                     mode="driving",
                                     departure_time=now)
				road_distance = directions_result[0]['legs'][0]['distance']['text']
				data_road_distance.append(road_distance)
				road_duration = directions_result[0]['legs'][0]['duration']['text']
				data_road_duration.append(road_duration)
				print('good!')
			else:
				directions_result = gmaps.directions(start,
                                     end,
                                     mode="driving",
                                     departure_time=now)
				road_distance = directions_result[0]['legs'][0]['distance']['text']
				data_road_distance.append(road_distance)
				road_duration = directions_result[0]['legs'][0]['duration']['text']
				data_road_duration.append(road_duration)

			if port_city == 'Port Massawa': # To Append all city names, and lat/long info to dict key once only
				all_data['city_name'].append(city)
				latitude = destination.latitude
				all_data['latitude'].append(latitude)
				longitude = destination.longitude
				all_data['longitude'].append(longitude)
			print(city,'---->', port_city, geodesic(start,end).miles,'-----', road_distance, road_duration)

	for item in data_straight_distance:
		if port_city == 'Port Massawa':
			all_data['massawa_straight_distance'].append(item)
			all_data['massawa_road_distance'].append(item)
			all_data['massawa_road_duration'].append(item)
		if port_city == 'Port Assab':
			all_data['assab_straight_distance'].append(item)
			all_data['assab_road_distance'].append(item)
			all_data['assab_road_duration'].append(item)
		if port_city == 'Port Tadjoura':
			all_data['tadjoura_straight_distance'].append(item)
			all_data['tadjoura_road_distance'].append(item)
			all_data['tadjoura_road_duration'].append(item)
		if port_city == 'Port de Doraleh, Djibouti':
			all_data['djibouti_straight_distance'].append(item)
			all_data['djibouti_road_distance'].append(item)
			all_data['djibouti_road_duration'].append(item)
		if port_city == 'Port of Mogadishu':
			all_data['mogadishu_straight_distance'].append(item)
			all_data['mogadishu_road_distance'].append(item)
			all_data['mogadishu_road_duration'].append(item)
		if port_city == 'Berbera Port':
			all_data['berbera_straight_distance'].append(item)
			all_data['berbera_road_distance'].append(item)
			all_data['berbera_road_duration'].append(item)
		if port_city == 'Mokowe, Kenya':
			all_data['lamu_straight_distance'].append(item)
			all_data['lamu_road_distance'].append(item)
			all_data['lamu_road_duration'].append(item)
df = pd.DataFrame(all_data)
df.to_csv('WedEb_with_gps.csv')
print(df)