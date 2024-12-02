# def dictToList():
#     d = {'a': 1, 'b': {'c': 2}, 'd': [3, 4]}
#     lt = []
#     for k,v in d.items():
#         lt.append(k)
#         if type(v) is dict:
#             for k1,v1 in v.items():
#                 lt.extend([k1,v1])
#         elif type(v) is list:
#             for i in v:
#                 lt.append(i)
#         else:
#             lt.append(v)
#     print(lt)  # ['a', 1, 'b', 'c', 2, 'd', 3, 4]
# dictToList()

# def expandstring(data):
#     # i/p:  a4b3c2   o/p:  aaaabbbcc
#     alpha, digit =[], []
#     stringcombo = ''
#     l={}
#     for i in data:
#         if i.isalpha():
#             alpha.append(i)
#         elif i.isdigit():
#             digit.append(i)
#     print(alpha,digit)
#     # '''
#     for i in range(len(alpha)):
#         stringcombo = stringcombo + alpha[i]*int(digit[i])
#     print(stringcombo)
#     # '''
#     '''
#     for k,v in zip(alpha,digit):
#         l[k] = v
#     print(l)
#     for k,v in l.items():
#         stringcombo = stringcombo + (k*int(v))
#     print(stringcombo)
#     '''
# expandstring('a4b3c2')

# def readevenlinesfromfile(filepath):
#     with open(filepath, 'r') as file:
#         i=1
#         for line in file.readlines():
#             if i % 2==0:
#                 print(line)
#             i+=1
#
# readevenlinesfromfile(r"C:\Users\Admin\Desktop\common_practiceed_code.txt")

# import sys
# '''printing the hello world without print() function'''
# sys.stdout.write('Hello world')

# d = {'a': 1, 'b': {'c': 2}, 'd': [3, 4]}

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# # Example usage
# arr = [64, 34, 25, 12, 22, 11, 90]
# print("Bubble Sort:", bubble_sort(arr))

# def selectionsort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr
#
# arr = [64, 34, 25, 12, 22, 11, 90]
# print(f"selection sort: {selectionsort(arr)}")

# def insersionsort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         for j in range(i,0,-1):
#             if key < arr[j-1]:
#                 arr[j] = arr[j-1]
#             else:
#                 arr[j] = key
#                 break
#         else:
#             arr[0] = key
#     return arr
# arr = [64, 34, 25, 12, 22, 11, 90]
# print(f"insersion sort: {insersionsort(arr)}")

def mergesort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        leftarr=arr[:mid]
        rightarr=arr[mid:]

        mergesort(leftarr)
        mergesort(rightarr)

        i = j = k = 0

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i+=1
            else:
                arr[k] = rightarr[j]
                j+=1
            k+=1

        while i<len(leftarr):
            arr[k] = leftarr[i]
            i+=1
            k+=1

        while j<len(rightarr):
            arr[k] = rightarr[j]
            j+=1
            k+=1
    return arr

# arr = [64, 34, 25, 12, 22, 11, 90]
# print(f'merge sort: {mergesort(arr)}')

import os

# print(os.getcwd())
# os.makedirs(r"file1\file2\file3")

# os.makedirs(r"file1\file2\file6")
# os.rename('file1', 'filessss1')
# print(os.listdir())
# print(os.stat('filessss1'))
# for dirpath, folder, files in os.walk(r"C:\Source\practice\filessss1"):
#     print(f"dir path: {dirpath}")
#     print(f"dir folder names: {folder}")
#     print(f"file names: {files}")
#     if r"New folder" in folder:
#         print(dirpath)
#         break

# print(os.path.isfile(r"C:\Source\practice\filessss1\New Bitmap Image.bmp"))
# a = os.fork()
# print(a)

# import subprocess
# try:
#     ans = subprocess.check_output(["ls", ""], text=True)
#     print(ans)
#
# except subprocess.CalledProcessError as e:
#     print(f"Command failed with return code {e.returncode}")

# parent class
class Person:

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    # child class


class Employee(Person):
    def __init__(self, name, idnumber, salary):
        self.salary = salary

        # invoking the constructor of
        # the parent class
        # Person.__init__(self, name, idnumber)
        super().__init__(name, idnumber)

    def show(self):
        print(self.salary, self.name, self.idnumber)

# Person('smart', 5626)
# a = Employee(name='sanju', idnumber=5626, salary=5000)
# a.show()
# a.display()

from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def info(self):
        return "This is an animal."

# Base class
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Encapsulation example
class Person:
    def __init__(self, name):
        self.__name = name  # private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

# Inheritance example
class Owner(Person):
    def __init__(self, name, pet):
        super().__init__(name)
        self.pet = pet  # Owner has a pet

    def pet_sound(self):
        return f"{self.get_name()}'s pet goes: {self.pet.sound()}"

# Polymorphism example
def make_animal_sound(animal):
    print(animal.sound())

# Sample usage
# if __name__ == "__main__":
#     dog = Dog()
#     cat = Cat()

    # Demonstrating polymorphism
    # make_animal_sound(dog)  # Output: Bark
    # make_animal_sound(cat)  # Output: Meow
    #
    # # Demonstrating encapsulation
    # owner = Owner("Alice", dog)
    # print(owner.get_name())  # Output: Alice
    # print(owner.pet_sound())  # Output: Alice's pet goes: Bark
    #
    # # Changing the name
    # owner.set_name("Bob")
    # print(owner.get_name())  # Output: Bob


from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# Derived class for Car
class Car(Vehicle):
    def __init__(self, model):
        self.__model = model  # private attribute
        self.__engine_running = False

    def start_engine(self):
        self.__engine_running = True
        return f"{self.__model} engine started."

    def stop_engine(self):
        self.__engine_running = False
        return f"{self.__model} engine stopped."

    # Encapsulation: getter method
    def get_model(self):
        return self.__model

# Derived class for Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, model):
        self.__model = model  # private attribute
        self.__engine_running = False

    def start_engine(self):
        self.__engine_running = True
        return f"{self.__model} motorcycle engine started."

    def stop_engine(self):
        self.__engine_running = False
        return f"{self.__model} motorcycle engine stopped."

    # Encapsulation: getter method
    def get_model(self):
        return self.__model

# Function to demonstrate polymorphism
def tst_vehicle(vehicle):
    print(vehicle.start_engine())
    print(vehicle.stop_engine())

# Sample usage
# if __name__ == "__main__":
#     car = Car("Toyota")
#     motorcycle = Motorcycle("Harley")
#
#     tst_vehicle(car)        # Output: Toyota engine started. / Toyota engine stopped.
#     tst_vehicle(motorcycle) # Output: Harley motorcycle engine started. / Harley motorcycle engine stopped.


sentence= "Given a text file fname the task characters and the lines"
d = {'G':'Given', 'a':['a','and'], 't':['text','task','the', 'the'], 'f': ['file', 'fname'], 'c':'characters', 'l':'lines'}

def countWords(sentence=sentence):
    words = sentence.split()
    d = {}

    for word in words:
        key = word[0]
        if key in d:
            if isinstance(d[key], list):
                d[key].append(word)
            else:
                d[key] = [d[key], word]
        else:
            d[key] = word
    print(d)

sentence = "Given a text file fname the task characters and the lines"
# countWords(sentence)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo*2)