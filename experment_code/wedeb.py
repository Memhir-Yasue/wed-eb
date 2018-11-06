

def main():
	port_city_list = ['Massawa','Assab','Djibouti'

	]
	region_list = {

		'Tigray':[ {'Aksum':[]}, {'Adwa':[]}, {'Mekelle':[]}

		],

	   	'Amhara':[ {'Bahir Dar':[]}, {'Gonder':[]}, {'Desse':[]}

	   	],

	   	'Oromia':[{'Negelle':[]}, {'Sashemene':[]}, {'Nazreth':[]}

	   	]

	   	}
	state_names = []
	city_names = []
	get_city_state_names(port_city_list, region_list,state_names,city_names)
	append_latlong(port_city_list, region_list, state_names,city_names)

####################################################
def get_city_state_names(port_city_list, region_list,state_names, city_names):
	for state in region_list.items():
		state_name = state[0]
		for city in region_list[state_name]:
			for item in city.items():
				city_name = item[0]
				state_names.append(state_name)
				city_names.append(city_name)
	return state_names, city_names

def append_latlong(port_city_list, region_list,state_names,city_names):
	for state in set(state_names):
		print(state,'---------')
		for city_name in city_names:
			if state == 'Tigray':
				

	

main()