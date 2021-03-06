# from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import googlemaps
from datetime import datetime
import pandas as pd
import urllib.request
import json
import config

# geolocator = Nominatim(user_agent="specify_your_app_name_here")
geolocator = GoogleV3(api_key=config.api_key)
gmaps = googlemaps.Client(key=config.maps_api_key)

port_cityList = ['Port Massawa', 'Port Assab', 'Port Tadjoura', 'Port de Doraleh, Djibouti',
'Port of Mogadishu','Berbera Port', 'Mokowe, Kenya'
]

tigray = ['Himora','Shire', 'Aksum', 'Adwa', 'Adigrat', 'Negash',
		 'Mekele', 'Ambalage', 'Korem', 'Alamta', 'Shiraro',
		 'Birkuta','Adi Ramets','May Tsemre','Inda Aba Guna'

]

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
'Berhale', 'Eli Dar', 'Semera', 'Gewana', 'Awash', 'Chifra', 'Abala'
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
'Melka Chireti','Bogol','Fiq','Erer', 'Dudub', 'Werder', 'Welwel',
'Danan'
]

debub = [
'Butajira','Agena','Hosaena','Alba Kulito','Areka',
'Tarcha','Sodo','Yirga Alem','Dilla','Arba Minch','konso',
'Masha','Gecha','Mizan Teferi','Bonga','Shishinda',
'Omorate','Turmi','Welkite', 'Gesuba', 'Sawla', 'Jinka',
'Omorate','Kemba','Bulki','Kossie','Gidole',
'Doyogena High school','Worabe','Sekoru'
]


oromiya = [
'Gimbi','Dembi Dolo','Dongoro','Nekemte','Ambo',
'Bishoftu','Adama','Meiso','Karamile','Raaso',
'Delo','Dinsho','Assela','Tiya','Asasa',
'Sashamane','Finchawa','Hagere Maryam','Kibre Mengist',
'Wadera','Negele','Udet','Filtu','Moyala',
'Wachile','Mega','Yebelo','Addis Alem','Waliso','Jimma',
'Agaro','Ziway','Awassa','Fiche','Mendi', 'Guliso','Baco','Kake','Gedo',
'Yayu','Bedele','Bichano','Nedjo','Metu','Gore'
]

benshangul = [
'Asosa','Menge','Guba'
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
	'elevation': [],

}

for port_city in port_cityList:
	data_straight_distance = []
	data_road_distance = []
	data_road_duration = []
	port = geolocator.geocode(port_city)
	start = port.latitude, port.longitude
	for state_Name in region:
		for city in state_Name:
			dest_city = city + ", Ethiopia" # Make sure towns are in Ethiopia
			destination = geolocator.geocode(dest_city)
			end = destination.latitude, destination.longitude
			straight_distance = geodesic(start,end).miles
			data_straight_distance.append(straight_distance)
			# Getting driving distance and duration
			now = datetime.now()
			if port_city == 'Port de Doraleh, Djibouti': # Getting around an error between himora and djibouti
				start = '11.578054, 43.094573'
				directions_result = gmaps.distance_matrix(start,
                                     end,
                                     mode="driving",
                                     departure_time=now,
                                     units='imperial')
				road_distance = directions_result['rows'][0]['elements'][0]['distance']['text']
				data_road_distance.append(road_distance)
				road_duration = directions_result['rows'][0]['elements'][0]['duration']['value']
				data_road_duration.append(road_duration)
			else:
				directions_result = gmaps.distance_matrix(start,
                                     end,
                                     mode="driving",
                                     departure_time=now,
                                     units='imperial')
				road_distance = directions_result['rows'][0]['elements'][0]['distance']['text']
				data_road_distance.append(road_distance)
				road_duration = directions_result['rows'][0]['elements'][0]['duration']['value']
				data_road_duration.append(road_duration)

			if port_city == 'Port Massawa': # To Append all city names, and lat/long info to dict key once only
				all_data['city_name'].append(city)
				latitude = destination.latitude
				all_data['latitude'].append(latitude)
				longitude = destination.longitude
				all_data['longitude'].append(longitude)
				#elevation calculation
				ELEVATION_BASE_URL = 'http://maps.googleapis.com/maps/api/elevation/json?'
				URL_PARAMS = "locations=%s,%s&sensor=%s" % (latitude, longitude, "false")
				url=ELEVATION_BASE_URL + URL_PARAMS
				with urllib.request.urlopen(url) as f:
					response = json.loads(f.read().decode())    
					status = response["status"]
					result = response["results"][0]
				feet = 3.28084
				elevation = str(result["elevation"] * feet )
				all_data['elevation'].append(elevation)
			print(city,'---->', port_city, geodesic(start,end).miles,'-----', road_distance, road_duration, elevation)

	for item in data_straight_distance:
		if port_city == 'Port Massawa':
			all_data['massawa_straight_distance'].append(item)
		if port_city == 'Port Assab':
			all_data['assab_straight_distance'].append(item)
		if port_city == 'Port Tadjoura':
			all_data['tadjoura_straight_distance'].append(item)
		if port_city == 'Port de Doraleh, Djibouti':
			all_data['djibouti_straight_distance'].append(item)
		if port_city == 'Port of Mogadishu':
			all_data['mogadishu_straight_distance'].append(item)
		if port_city == 'Berbera Port':
			all_data['berbera_straight_distance'].append(item)
		if port_city == 'Mokowe, Kenya':
			all_data['lamu_straight_distance'].append(item)

	for item in data_road_distance:
		if port_city == 'Port Massawa':
			all_data['massawa_road_distance'].append(item)
		if port_city == 'Port Assab':
			all_data['assab_road_distance'].append(item)
		if port_city == 'Port Tadjoura':
			all_data['tadjoura_road_distance'].append(item)
		if port_city == 'Port de Doraleh, Djibouti':
			all_data['djibouti_road_distance'].append(item)
		if port_city == 'Port of Mogadishu':
			all_data['mogadishu_road_distance'].append(item)
		if port_city == 'Berbera Port':
			all_data['berbera_road_distance'].append(item)
		if port_city == 'Mokowe, Kenya':
			all_data['lamu_road_distance'].append(item)

	for item in data_road_duration:
		if port_city == 'Port Massawa':
			all_data['massawa_road_duration'].append(item)
		if port_city == 'Port Assab':
			all_data['assab_road_duration'].append(item)
		if port_city == 'Port Tadjoura':
			all_data['tadjoura_road_duration'].append(item)
		if port_city == 'Port de Doraleh, Djibouti':
			all_data['djibouti_road_duration'].append(item)
		if port_city == 'Port of Mogadishu':
			all_data['mogadishu_road_duration'].append(item)
		if port_city == 'Berbera Port':
			all_data['berbera_road_duration'].append(item)
		if port_city == 'Mokowe, Kenya':
			all_data['lamu_road_duration'].append(item)

df = pd.DataFrame(all_data)
df.to_csv('WededV3.csv')
print(df)