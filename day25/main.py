# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

# import csv

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas as pd

data = pd.read_csv("./day25/weather_data.csv")
# print(data["temp"], "\n")

# data_dict = data.to_dict()
# print(data_dict, "\n")

# temp_list = data["temp"].to_list()
# print(temp_list, "\n")


# print(round(data['temp'].mean(),2),'\n')
# print(data['temp'].max(),'\n')

# print(data[data.day == 'Monday'],'\n')

# print(data[data.temp == data.temp.max()])

# print(data[data.day == 'Monday'].temp)

# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

# data = pd.DataFrame(data_dict)

# data.to_csv('students_data.csv')