#prime number
# from traceback import print_tb
# from unittest.mock import right


def prime(n):
    if n > 1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(f"{n} is prime")
    else:
        print("not possible")

# prime(5)

def prime100to200():
    for i in range(100,200):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i, end=" ")

# prime100to200()


def primeFromList(lt):
    for i in lt:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

mylist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primeFromList(lt=mylist)


#fib
def fib(n):
    a,b=0,1
    for i in range(n):
        print(a, end=" ")
        a,b=b,a+b

# fib(10)

#fib with recursive
def fib2(n):
    a,b=0,1
    if n==1:
        return b
    elif n==0:
        return a
    elif n<0:
        return "not possible"
    else:
        return fib2(n-1) + fib2(n-2)

# for i in range(10):
#     print(fib2(i), end=" ")


#factorial
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

# fact(5)


#star right angle
def starangle(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end=" ")
        print()

# starangle(5)


#triangle
def triangle(n):
    k=n-1
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k=k-1
        for j in range(i+1):
            print("*", end=" ")
        print()

# triangle(5)


# inverted triangle
def invertTriangle(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(n-i):
            print("*", end=" ")
        print()

# invertTriangle(5)


#invertedrightangle
def invertRightAngle(n):
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for k in range(n-i):
            print("*", end=" ")
        print()

# invertRightAngle(5)


#palindrome
def pali(data):
    rev_data=''
    for i in str(data):
        rev_data=i+rev_data
    if str(data)==rev_data:
        print("palindrome")
    else:
        print("not palindrome")

# pali('madam')


#reverse char and replace in same position
def revreplace(data):
    result=[]
    split_data=data.split()
    for i in split_data:
        result.append(i[::-1])

    print(" ".join(result))

# revreplace('this is interview')


#bubble sort
def sort(mylist):
    for i in range(len(mylist)):
        for j in range(i+1):
            if mylist[i]<mylist[j]:
                mylist[i],mylist[j]=mylist[j],mylist[i]

    print(mylist)

# sort([8, 1, 9, 2, 7, 0, 4, 5, 3, 6])


#char occurance
def count(data):
    count_dict={}
    for i in data:
        if i in count_dict:
            count_dict[i]+=1
        else:
            count_dict[i]=1
    # print(max(count_dict,key=count_dict.get))
    result=''
    for k,v in count_dict.items():
        result=result+f"{k}{v}"
    print(result)
# count('aabbbcccc')


#char occurance to char
def count2(data):
    num=[]
    alpha=[]
    for i in data:
        if i.isalpha():
            alpha.append(i)
        else:
            num.append(i)
    result=''
    for i in range(len(num)):
        result=result+alpha[i]*int(num[i])
    print(result)

# count2("a2b3c4")


'''create a dict using two lists'''


def createdict():
    l1 = ['a', 'b', 'c']
    l2 = [1, 2, 3]
    dic={}
    for i in range(len(l1)):
        dic[l1[i]]=l2[i]
    print(dic)

# createdict()


'''addition of two dict's'''


def combinedicts():
    d1 = {1: 200, 2: 300, 3: 500}
    d2 = {1: 500, 2: 700, 4: 600}
    for i in d2:
        if i in d1:
            d1[i]=d1[i]+d2[i]
        else:
            d1[i]=d2[i]
    print(d1)

# combinedicts()


'''odd and multiples of 5'''


def oddAndMulOf5():
    l2 = [10, 15, 20, 25, 30, -5, -30, 3]
    for i in l2:
        if i%2!=0 and i%5==0:
            continue
        else:
            l2.remove(i)
    print(l2)
# oddAndMulOf5()


'''seperate even and odd list'''
def evenOrOddusingcomprehension():
    l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"even: {[i for i in l3 if i%2==0]}")
    print(f"odd: {[i for i in l3 if i%2!=0]}")
    # print(f"even_square: {i:i**2 for i in l3 if i%2==0}")


'''reverse a list ??????????????'''
def reverseList():
    l3 = [1, 2, 3, 4, 5]
    for i in range(len(l3)):
        l3.insert(0,l3.pop(i))
    print(l3)
# reverseList()


'''lambda(single and multiple args) & map & filter'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a=lambda i: i*2
# print(a(5))

b=lambda *i: sum(i)
# print(b(*l))

c=list(map(lambda i: i%2==0, l))
# print(c)

d=list(filter(lambda i: i%2==0, l))
# print(d)

from functools import reduce
e = reduce(lambda x,y: x+y, l)
# print(e)


#add two mmatrix
def addTwoMatrix():
    a=[[1,2,3],[4,5,6],[7,8,9]]
    b=[[1,2,3],[4,5,6],[7,8,9]]
    result=[[0,0,0],[0,0,0],[0,0,0]]

    for i in range(len(a)):
        for j in range(len(b)):
            result[i][j]= a[i][j] + b[i][j]
    print(result)


#generator
def square(n):
    for i in range(1,n):
        # print(i, "jjjj")
        yield i**2
z=square(5)
# print(z.__next__())
# print(z.__next__())
# print(z.__next__())
# print(z.__next__())
# print(z.__next__())


#decorator
def deco_func(fun):
    def inner_func():
        result=fun()
        return result.upper()
    return inner_func

@deco_func
def string_value():
    return "python"

# print(string_value())


'''missing elements in an array'''
def missing(arr):
    for i in range(len(arr)):
        for j in range(i+1):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    # print(arr)
    miss_ele=[]
    for i in range(arr[0], arr[-1]+1):
        if i not in arr:
            miss_ele.append(i)

    print(miss_ele)

lt=[1, 7, 4, 3, 9, 2]
# missing(arr=lt)


'''file handling'''

def read_data_from_file(filepath):
    with open(filepath, 'r') as data:
        print(data.read())
        print(data.read(5))
        print(data.readline())
        print(data.readlines())

# read_data_from_file(filepath=r"C:\Users\Admin\OneDrive\Desktop\data.txt")


def returnLinenumber(filepath, line):
    try:
        with open(filepath, 'r') as data:
            for linenumber, value in enumerate(data, start=1):
                if line in value:
                    print(linenumber)
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print(f"exceprion is {e}")

# returnLinenumber(filepath=r"C:\Users\Admin\OneDrive\Desktop\data.txt", line="Remove all")

def read_even_lines(filepath):
    with open(filepath, "r") as data:
        for linenumber, value in enumerate(data, start=1):
            if linenumber%2==0:
                print(value)
# read_even_lines(filepath=r"C:\Users\Admin\OneDrive\Desktop\data.txt")

def writedata(filepath):
    text = r"HEROOOOC:\Python312\python.exe C:\Source\Python_practice_mine\New folder\all_programs.py"
    with open(filepath, 'a+') as data:
        data.seek(0,2)
        data.write(text)

# writedata(filepath=r"C:\Users\Admin\OneDrive\Desktop\data.txt")


'''json'''
import json
def readJsonFile(filepath):
    with open(filepath, 'r') as data:
        result = json.load(data)
        print(result)

# readJsonFile(filepath=r"C:\Source\Python_practice_mine\New folder\csvtojsoncontent.json")

def writeJsonFile(filepath):
    writeData={'1': '200', '2': '41', '3': '58', '5': '86', '7': '95', '11': '13', '13': '91', '17': '17', '19': '47'}
    with open(filepath,'r') as data:
        existed_data = json.load(data)
        if isinstance(existed_data, list):
            existed_data.append(writeData)
        else:
            existed_data.update(writeData)
    print(existed_data)
    with open(filepath, 'w') as opendata:
        json.dump(existed_data, opendata, indent=4)

# writeJsonFile(filepath=r"C:\Source\Python_practice_mine\New folder\csvtojsoncontent.json")


import csv
def readcsvFile(filepath):
    result_data=[]
    with open(filepath, 'r') as data:
        result=csv.reader(data)
        header = next(result)
        for i in result:
            result_data.append(i)
    # print(header)
    # print(result_data)


#def writecsvfile(filepath):
    import os
    path = os.path.split(filepath)[0]
    new_filepath = os.path.join(path,"new_csv_file.csv")
    print(new_filepath)
    print(header)
    print(result_data)
    with open(new_filepath, 'w', newline='') as content:
        content_write = csv.writer(content)
        content_write.writerow(header)
        content_write.writerows(result_data)

# readcsvFile(filepath=r"C:\Source\Python_practice_mine\New folder\content.csv")


def jsonDataToCsvFile(jsonfilepath, csvfilepath):
    with open(jsonfilepath, 'r') as jsondata:
        jsondataresult = json.load(jsondata)

    with open(csvfilepath, 'w', newline='') as csvdata:
        content = csv.DictWriter(csvdata, jsondataresult.keys())
        content.writeheader()
        content.writerow(jsondataresult)

# jsonDataToCsvFile(jsonfilepath=r"C:\Source\Python_practice_mine\New folder\content.json", csvfilepath="new_json_to_csv.csv")


'''OOPs'''

from abc import ABC, abstractmethod


class vehicle(ABC):

    @abstractmethod
    def engine_condition(self):
        pass


class specs(vehicle):
    def __init__(self, vehicle_type, color, engine_state):
        self.type = vehicle_type#$
        self.color = color#$
        self.engine = engine_state #$

    def engine_condition(self):# $
        if self.engine is True:
            print('engine started')
        else:
            print('engine stopped')


# multi level ineritance
class car(specs):
    wheels = 4#

    def __init__(self, gears, vehicle_type, color, engine_state):
        self.gears = gears#$
        super().__init__(vehicle_type, color, engine_state)

    # instancemethod
    def details(self):# $
        # self.engine_condition()
        print(f"This car has {self.gears} gears in {self.color} color with {self.type} type {self.wheels}")

    @classmethod
    def get_wheel_details(cls):# $
        print(f"this car has {cls.wheels} wheels")

    @staticmethod
    def get_info():# $
        print("this is car class")


# hierarical inheritance
class bike(specs):
    wheels = 2  # class variable

    def __init__(self, gears, vehicle_type, color, engine_state):
        self.gears = gears
        super().__init__(vehicle_type, color, engine_state)

    # instancemethod
    def details(self):
        print(f"This bike has {self.gears} gears in {self.color} color with {self.type} type")

    @classmethod
    def get_wheel_details(cls):
        print(f"this bike has {cls.wheels} wheels")

    @staticmethod
    def get_info():
        print("this is bike class")


# polymorphism
def transport(obj):
    obj.get_info()
    obj.get_wheel_details()
    obj.details()
    obj.engine_condition()


car_obj = car(6, "diesel", "black", True)
bike_obj = bike(5, "petrol", "white", False)
# transport(car_obj)
# transport(bike_obj)

# print(dir(car))
# print(dir(car_obj))

'''super with init printing'''

class A:
    def __init__(self):
        print('A class init')

class B(A):
    def __init__(self):
        super().__init__()
        print('B class init')

# obj = B()
# import time
# ctime=time.localtime()
# time_past = time.strftime(("%H%M%S"),ctime)
# print(time_past)
# import dask.dataframe as dk
#
# result = dk.read_csv("new_csv_file.csv")
# print(result.head())
# print((result.groupby('revenue').sum().compute()))

# import pandas as pd
# result = pd.read_csv("new_csv_file.csv")
# print(result.head(1))

# ctime=time.localtime()
# print(time.strftime(("%H%M%S"),ctime))

import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        print(letter)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
# thread1.start()
# thread2.start()
#
# # Wait for threads to complete
# thread1.join()
# thread2.join()
#
# print("Threads have completed execution.")


import multiprocessing, time

def print_numbers():
    for i in range(1, 6):
        time.sleep(0.2)
        print(i)

def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        time.sleep(0.2)
        print(letter)

if __name__ == '__main__':
    # Create processes
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters)

    # Start processes
    # process1.start()
    # process2.start()
    #
    # # Wait for processes to complete
    # process1.join()
    # process2.join()
    #
    # print("Processes have completed execution.")



import multiprocessing, time

def square():
    for i in range(1,5):
        print(f"square: {i*i}",)
        time.sleep(0.5)


def cube():
    for i in range(1,5):
        print(f"cube: {i*i*i}")
        time.sleep(0.5)


t1 = multiprocessing.Process(target=square)
t2 = multiprocessing.Process(target=cube)

t1.start()
time.sleep(0.2)
t2.start()

t1.join()
t2.join()