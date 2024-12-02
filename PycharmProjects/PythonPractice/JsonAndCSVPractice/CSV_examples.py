# """Read data from a CSV file"""
#
#
# import csv
#
# filename = "weather_by_cities.csv"
#
# fields = []
# rows = []
# fulldata = []
#
# with open(filename, 'r') as f:
#     csvreader = csv.reader(f)
#     for i in csvreader:
#         fulldata.append(i)
#     print(fulldata)
#
# for y in fulldata:
#     print(y)
#

# """Reading data from CSV and get output as a tabler form in output"""
#
# import csv
#
# filename = "weather_by_cities.csv"
#
# fields, rows = [], []
#
# with open(filename, "r") as a:
#     csvreader = csv.reader(a)
#
#     # fields = csvreader.__next__() #or
#      fields = next(csvreader) # gives the first line of the csv file and also removes that line from the csvreader variable
#     # print(fields)
#
#     for i in csvreader:
#         rows.append(i)
#
#     # print(rows)
#
#     for x in fields:
#         print("%10s" % x, end=" ")
#     print("\n")
#
#     for y in rows:
#         for col in y:
#             print("%10s" % col, end=" ")
#         print("\n")
#
#
# """Writing data to new CSV file"""
#
# with open("updated.csv", "w") as z:
#     writer = csv.writer(z)
#
#     # for i in rows:
#     #     i[1] = 'India'
#     #     break
#     # # for j in fields:
#     # fields[1] = "state"
#         # break
#     writer.writerow(fields)
#     writer.writerows(rows)

#
# """WRiting dictionay to a CSV file"""
#
import csv
#
mydict = [{'branch': 'COE', 'cgpa': '9.0',
           'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1',
           'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3',
           'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5',
           'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8',
           'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1',
           'name': 'Sahil', 'year': '2'}]
#
# with open("updated.csv", "w") as m:
#     writer = csv.DictWriter(m, fieldnames=mydict[0].keys())
#
#     writer.writeheader()
#     writer.writerows(mydict)

#
# """reading data using pandas and creating and writing to a csv file from dictionary"""
#
# import pandas as pd
# #
# # # with open("updated.csv", "r") as p:
# data = pd.read_csv("updated.csv")
# print(data) 
# print(data["name"])
# #
# # for i in data["name"]:
#
#
# # data["name"]['Nikhil'] = "Akhil"
#
# result = pd.DataFrame(mydict)
# result.to_csv("latest.csv")

