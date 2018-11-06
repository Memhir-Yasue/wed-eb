# port_city_list = ['Massawa','Assab','Djibouti'

# ]

# # region_list = {
# # 		'Tigray':['Aksum','Adwa','Mekelle'

# # 		],	
# # 	   	'Amhara':['Bahir Dar','Gonder','Desse'

# # 	   	],
# # 	   	'Oromia':['Negelle', 'Sashemene','Nazreth'

# # 	   	]
# # }

# # print(region_list['Tigray'][0])


# # for port_city in port_city_list:
# # 	# Get a port city
# # 	for state_name in region_list:
# # 		# Get a province
		
# # 		for city in region_list[state_name]:
# # 			# Get a city 
# # 			print(port_city, state_name,city)

# # How to iterate over a list
# # print(region_list['Tigray'])
# # for item in region_list['Tigray']:
# # 	print(item)

# #####################################################################
# #						NESTED DICTIONARY

# region_list = {
# 		'Tigray':[ {'Aksum':[9.434,11.33]}, {'Adwa':[]}, {'Mekelle':[]}

# 		],	
# 	   	'Amhara':['Bahir Dar','Gonder','Desse'

# 	   	],
# 	   	'Oromia':['Negelle', 'Sashemene','Nazreth'

# 	   	]
# }

# print(region_list['Tigray'])
# # print(region_list['Tigray'][0]['Aksum'][0]) 

# # region_list['Tigray'][1]['Adwa'].append(9.998)
# # region_list['Tigray'][1]['Adwa'].append(11.887)

# # # print(region_list['Tigray'])
# # i = 0
# # for item in region_list.items():
# # 	state_name = item[0]
# # 	print(item[1][0])

# ####################################################################
# 							# NESTED II
# # region_list = {
# # 		'Tigray':[ {'Aksum':[]}, {'Adwa':[]}, {'Mekelle':[]}

# # 		],	
# # 	   	'Amhara':[ {'Bahir Dar':[]}, {'Gonder':[]}, {'Desse':[]}

# # 	   	],
# # 	   	'Oromia':[{'Negelle':[]}, {'Sashemene':[]}, {'Nazreth':[]}

# # 	   	]
# # }
# # state_names = []
# # city_names = []
# # def get_city_state_names(state_names, city_names):
	
# # 	for state in region_list.items():
# # 		state_name = state[0]
# # 		for city in region_list[state_name]:
# # 			for item in city.items():
# # 				city_name = item[0]
# # 				state_names.append(state_name)
# # 				city_names.append(city_names)
# # 	return state_names, city_names
# # # run function

# # def post_city_state_names(state_names,city_names):
# # 	print(state_names)



# # def main():
# # 	get_city_state_names(state_names,city_names)
# # 	post_city_state_names(state_names,city_names)

# # main()





# 		