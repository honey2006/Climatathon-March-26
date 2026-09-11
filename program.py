from Nasa_Data import get_temp_data

data=[]

days = 5
for i in range(days, 3, -1):
    data.append(get_temp_data(i))

print(data)