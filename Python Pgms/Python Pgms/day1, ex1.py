# # Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
# # Type "help", "copyright", "credits" or "license()" for more information.
# # >>> s="hello world"
# # >>> s[0:5]
# # 'hello'
# # >>> s[-5:-1]
# # 'worl'
# # >>> s[:]
# # 'hello world'
# # >>> s[:1]
# # 'h'
# # >>> s+s
# # 'hello worldhello world'
# # >>> s + s
# # 'hello worldhello world'
# # >>> s*3
# # 'hello worldhello worldhello world'
# # >>> len(s)
# # 11
# # >>> s[:]
# #
#
# # import numpy as np
# # a=np.array([1,2,3,4])
# # b = a+2
# # print(b)
#
# # from selenium import webdriver
# #
# # result = webdriver.Edge()
# # result.get("https:/www.google.com")
# # from time import sleep
# # sleep(5)
# # # print(result)
#
# print([x**2 for x in range(5) if x%2==0])
# print({x:x**2 for x in range(5) if x%2==0})
#
# x=[1,2,3]
# y=[4,5,6]
#
# z = [(x,y) for x,y in zip(x,y)]
# print(z)
#
# a,b = zip(*z)
# print(a,b)
#
#
# def decoFunc(func):
#     def innerWrapper():
#         result = func()
#         return result.upper()
#     return innerWrapper
#
# def decoFunc2(func):
#     def innerWrapper2():
#         result2 = func()
#         return result2.lower()
#     return innerWrapper2
#
# @decoFunc2 # second
# @decoFunc #first
# def data():
#     return 'hello'
#
# print(data())
#
# result = lambda x: x+2
#
# print(result(2))
#
# a = map(lambda x:x**2,x)
# print(list(a))
#
# v = 'hi ra mawa'
# y = v.split()
#
# print(' '.join(y))
#
#
# def modify_list(lst):
#     print(id(lst))
#     lst.append(4)
#     print(id(lst))
#     print(f"Inside function: {lst}")
#
# my_list = [1, 2, 3]
# print(id(my_list))
# modify_list(my_list)
# print(f"Outside function: {my_list}")
#
# original_list = [0, [1, 2, 3], 'a', [4, 5, [6,7]], [7, 8, 9]]
#
# import copy
#
# shallowcopy = copy.copy(original_list)
# print(shallowcopy)
#
# shallowcopy[0] = 1
# shallowcopy[2] = 'b'
# shallowcopy[1][0] = 1111
# shallowcopy[3][2][0] = 6666
#
# print(shallowcopy)
# print(original_list)
#
#
# # deepcopy = copy.deepcopy(original_list)
# #
# # deepcopy[0] = 1
# # deepcopy[2] = 'b'
# # deepcopy[1][0] = 1111
# # deepcopy[3][2][0] = 6666
# #
# # print(deepcopy)
# # print(original_list)
#
#
# class parent(object):
#     def __init__(self, name):
#         self.name = name
#
#
# class child(parent):
#     def __init__(self, name, age):
#         parent.name = name
#         self.age = age
#
#     def display(self):
#         print(f'parent name: {parent.name} and age :{self.age}')
#
# a = child('sanju', 26)
# a.display()
#
#
# class parent2:
#     def __init__(self, name):
#         self.name = name
#
# class child2(parent):
#     def __init__(self, name, age):
#         super(child2, self).__init__(name)
#         self.age = age
#
#     def display2(self):
#         print(f'parent name: {self.name} and age :{self.age}')
#
# b= child2('yash', 27)
# b.display2()
#
# l = ['sanju', 'yash']
# newL = []
# for i in range(len(l)):
#     newL.insert(0, l[i])
#
# print(newL)
#
#
# def armstrong():
#     num= int(input("enter number"))
#     add = 0
#     for i in str(num):
#         add += int(i)**3
#
#     print(add)
#     if add == num:
#         print(f"{num} is an armstrong")
#     else:
#         print(f"{num} is not an armstrong")
# # armstrong()
#
#
# def decimalToBinary():
#     num = int(input("enter number: "))
#
#     # print(bin(num))
#     #or
#
#     bin = ''
#     while num >0:
#         bin = str(num%2) + bin
#         num = num//2
#     print(bin)
# decimalToBinary()
#


class Car:
    __brk = False
    clutch = False
    accelerator = False
    name = "sadhik"

    @staticmethod
    def __start():
        print("car started:")

    @staticmethod
    def stop():
        print("car stoped")


class Tata(Car):
    def __init__(self, type):
        self.type  = type


class Harier(Tata):
    def __init__(self, colour, meilage):
        super().__init__(type)
        self.colour = colour
        self.meilage = meilage
        self.type = type
        super().start()

        @classmethod
        def change_name(cls, name):
            cls.name = name
            Car.name = ""


s1 = 'sms'
s2 = ""
for i in s1:
    s2 = i + s2
if s1 == s2:
    print("palindrome")
else:
    print





