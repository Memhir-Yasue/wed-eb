import pandas as pd
# for state in region:
# 	for city in state:		#Basic Template for accessing cities from region
# 		print(city)
port_cityList = ['Port Massawa', 'Port Assab', 'Port Tadjoura', 'Port de Doraleh, Djibouti',
'Port of Mogadishu','Berbera Port', 'Mokowe, Kenya'
]

tigray = ['Himora','Shire', 'Aksum']
amhara = ['Weldiya', 'Mersa', 'Dessie', 'Kombolcha']
region = [tigray, amhara]



port_data = {
    'city_name': [],
    'Massawa': [],
    'Asseb': [243,45,56,584,492,845,985],
    # 'Tadjoura': [126,24,560,584,192],
    # 'Djibouti': [88,25,56,284,952]
}

# Create a function to collect and store portCity geoinfo ONCE only

for state_name in region:
	for city_name in state_name:
		# Store city geocode
		#--------------------
		port_data['city_name'].append(city_name) #Append city name to df
		for port_name in port_cityList:
			port_data['Massawa'].

			
df = pd.DataFrame(port_data)
print(df)


