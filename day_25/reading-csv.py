import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for lists in list(data)[1:]:
#         temp.append(int(lists[1]))
#     print(temp)


# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(f"Avg temp = {round(sum(temp_list)/len(temp_list), 2)}")
# print(data[data.temp == data["temp"].max()])

squirrels = pandas.read_csv("squirrels_data.csv")
fur_list = squirrels["Primary Fur Color"].to_list()

fur_dic = {}
for colors in fur_list:
    if isinstance(colors, str):
        if colors not in fur_dic.keys():
            fur_dic[colors] = 1
        else:
            fur_dic[colors] += 1

print(fur_dic)