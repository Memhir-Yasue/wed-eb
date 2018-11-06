import pandas as pd
data_massawa = [270,245,56,84,92]
city_name = ['Adi kemey','Mesqel','Langano','Jijiga','Hosana']
# df = pd.DataFrame(columns=['City Name','Massawa','Asseb'])
# for i in city_name:
# 	df = df.append({'City Name': i}, ignore_index=True)
# i = 0
# for i in data_massawa:
# 	df = df.append({'Massawa': i}, ignore_index=True)
# print(df)

weather_data = {
    'city_name': [],
    'Massawa': [],
    'Asseb': [243,45,56,584,492],
    # 'Tadjoura': [126,24,560,584,192],
    # 'Djibouti': [88,25,56,284,952]
}

# df = pd.DataFrame(weather_data)
# print(weather_data)

for i in city_name:
	weather_data['city_name'].append(i)

for i in data_massawa:
	weather_data['Massawa'].append(i)
# print(weather_data)

df = pd.DataFrame(weather_data)
# print(df)

weather_data['numbers'] = []
for i in range(5):
	weather_data['numbers'].append(i)

# print(weather_data)
df = pd.DataFrame(weather_data)
print(df)