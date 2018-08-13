# from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import pandas as pd
import config
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
geolocator = GoogleV3(api_key=config.api_key)
port_cityList = ['Port Massawa', 'Port Assab', 'Port Tadjoura', 'Port Djibouti',
'Port of Mogadishu','Berbera Port', 'Lamu, Kenya'
]
# tigray = ['Himora','Shire', 'Aksum']
tigray = ['Himora','Shire', 'Aksum', 'Adwa', 'Adigrat', 'Negash',
		 'Mekele', 'Ambalage', 'Korem', 'Alamta']

amhara = ['Weldiya', 'Mersa', 'Dessie', 'Kombolcha',
'Artuma', 'Senbete', 'Molale', 'Ankober', 'Debre Birhan',
'Degolo', 'Rema', 'Merkane Selam', 'Mertule Maryam',
'Felege Birhan', 'Zebich', 'Dejen', 'Debre Markos', 'Dembecha',
'Bure','Injibara', 'Dangla', 'Durbete', 'Mer Awi', 'Bahir Dar',
'Addis Zemen', 'Gondar', 'Amba Giorgis', 'Dabat', 'Debark',
'Chew Ber','Corissa', 'Amdework', 'Sekota', 'Lalibela', 'Gashena', 'Wegel Tena',
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
'Melka Chireti','Bogol','Fiq','Hamero'
]

debub = [
'Butajira','Agena','Hosaena','Alba Kulito','Areka',
'Tarcha','Sodo','Yirga Alem','Dilla','Arba Minch','konso',
'Machi','Masha','Gecha','Mizan Teferi','Bonga','Shishinda',
'Omorate','Turmi','Ganda','Gedeb','Welkite'
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
'Asosa','Menge','Dibate','Guba','Debre Zeyit'
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
	'massawa' : [],
	'assab': [],
	'tadjoura': [],
	'djibouti': [],
	'mogadishu': [],
	'berbera': [],
	'lamu': [],
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
		if port_city == 'Port of Mogadishu':
			all_data['mogadishu'].append(item)
		if port_city == 'Berbera Port':
			all_data['berbera'].append(item)
		if port_city == 'Lamu, Kenya':
			all_data['lamu'].append(item)
df = pd.DataFrame(all_data)
df.to_csv('amh_tig.csv')
print(df)