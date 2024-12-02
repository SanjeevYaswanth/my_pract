# # import csv
# #
# # # Data to write with headers
# # data = [
# #     {'Name': 'John', 'Age': 30, 'City': 'New York'},
# #     {'Name': 'Anna', 'Age': 22, 'City': 'London'},
# #     {'Name': 'Mike', 'Age': 32, 'City': 'San Francisco'}
# # ]
# #
# # # Path to the CSV file
# # file_path = 'data_with_headers.csv'
# #
# # # Write CSV data to the file with headers
# #
# # with open(file_path, "w") as f:
# #     fieldnames = data[0].keys()
# #     header = csv.DictWriter(f, fieldnames=fieldnames)
# #     header.writeheader()
# #     for i in data:
# #         header.writerow(i)

# import csv

# filename = "weather_by_cities.csv"

# fields = []
# rows = []
# fulldata = []

# with open(filename, 'r') as f:
#     csvreader = csv.reader(f)
#     for i in csvreader:
#         fulldata.append(i)
#     print(fulldata)

# for y in fulldata:
#     print(y)
#     # fields = next(csvreader) # extract the first row
#     # print(next(csvreader)) # extract the second row

#     # csv.DictReader(f, fieldnames=fields)
#     # csv.readheader()
#     # for row in csvreader:
#     #     rows.append(row)
#     # for field in fields:
#     #     print(field, end="\n")
#     # for row in rows:
#     #     for row in row:
#     #         print(row, end="\n")
#     # print(rows)
#     # for r in fields:
#     #     print("%10s" % r, end = " ")
#     # print("\n")
#     #
#     # for row in rows:
#     #     for col in row:
#     #         print("%10s" % col, end = " ")
#     #
#     #     print("\n")

# from time import sleep
# from threading import *
import threading, time

class hello():
    def run(self):
        for i in range(3):
            print("hello")
            time.sleep(1)


class hi():
    def run(self):
        for i in range(3):
            print("hi")
            time.sleep(1)


t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=hi)

t1.start()
# sleep(0.2)
t2.start()
t1.join()
t2.join()

# x = [1,2,3]
# # x+4
# print(x+[4])
# # x.append[123,]
# print(x)
x = 5


def fun():
    x = 10
    print(x)


# fun()
# print(x)


# import numpy as np
# a=np.array([1,2,3,4])
# b = a+2
# print(b)


# def listpalindrome(l):
#     revlist = []
#     for i in l:
#         revlist.insert(0, i)
#
#     print(revlist)
#
#
# # l=[1, 2, 3, 2, 1]
# l = [1, 'abc', 'abc', 1]
#
#
# # listpalindrome(l)
#
#
# def checkvalidephonenumber(num):
#     import re
#     # number = re.fullmatch("$[6-9]\d{9}", int(num))
#     # print(number)
#
#
# # checkvalidephonenumber(num=636115223)
#
# my_set = {9, 9.0}
#
# # Display the set
# print("Set contents:", my_set)
#
# for item in my_set:
#     print(f"Element: {item}, Type: {type(item)}")
#
#
# def numbers():
#     num = 0
#     while num < 11:
#         print(num)
#         num += 1
#
#
# # numbers()
# a = [1,2,3,4,5]
# b = lambda *args: sum(args)
# print(b(*a))
#
# c = lambda a:a*10
# print(c(5))
#
# d = list(map(lambda a: a%2==0, a))
# print(d)
#
# e = list(filter(lambda a: a%2==0, a))
# print(e)


'''Odd numbers from list'''
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = [i for i in l3 if i%2==0]
# odd = [j for j in l3 if j%2!=0]
# print(even)
# print(odd)
# ev = {i:v for i,v in enumerate(l3) if v%2==0}
d = {i: v for i, v in enumerate(l3) if v % 2 == 0}
# print(d)


myList = [5, 1, 'sanju', 'manoj', 1, 5, 'sanju', 'sanju']
# result = []
#
# for i in myList:
#     if i not in result:
#         result.append(i)
#
# highest_occ_ele = 0
# highest_times = 0
#
# for i in result:
#     count = myList.count(i)
#     if count > highest_times:
#         highest_times = count
#         highest_occ_ele = i
#
# print(f"highest occurence element is {highest_occ_ele}, i.e. {highest_times} times")

d = dict()
for i in myList:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
maxkey = max(d, key=d.get)
print(maxkey, d[maxkey])

'''prime'''


def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print("not prime")
                break
        else:
            print('prime')
    else:
        print('not prime')


prime(0)

# mylist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# for i in mylist:
#     factors=0
#     for j in range(2, i+1):
#         if i%j==0:
#             factors+=1
#     if factors==1:
#         print(i)

'''Guess the output'''
a, b = 'pq'
b, c = 'rs'

print(a, b, c)

lst1 = [5, 3, 6, 1, 7, 'sanju']
lst2 = [1, 2, 3, 5, 7, 'manoj', 0, 'sanju']
for i in lst1:
    for j in lst2:
        if i == j:
            print(i)

'''Class, static, Instance methods and variables'''


class student:
    college = 'GITAM'  #class variable

    def __init__(self, m1, m2, m3):  #parameterised constructor
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3  #isntance variables

    #instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    #class method
    @classmethod
    def getcollegename(cls):
        return cls.college

    #static method
    @staticmethod
    def info():
        print('this is about student class info')


s1 = student(1, 6, 3)
print(s1.college)
print(s1.avg())
print(student.getcollegename())
s1.info()


class sanjeev(student):
    def __init__(self, m1, m2, m3, m4):
        super().__init__(m1, m2, m3)
        self.m4 = m4

    def allsubavg(self):
        return (self.m1 + self.m2 + self.m3 + self.m4) / 4


a1 = sanjeev(2, 3, 4, 5)
print(a1.allsubavg())
print(a1.avg())
print(a1.college)
print(a1.getcollegename())
print(a1.info())

d1 = {1: 200, 2: 300, 3: 500}
d2 = {1: 500, 2: 700, 4: 600}

for key in d2:
    if key in d1:
        # If the key exists in d1, sum the values
        d1[key] += d2[key]
    else:
        # If the key does not exist in d1, add it
        d1[key] = d2[key]
print(d1)
