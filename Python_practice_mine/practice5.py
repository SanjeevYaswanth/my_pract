# def fib(n):
#  p, q = 0, 1
#  while(p < n):
#   yield p
#   # s=p+q
#   # p = q
#   # q = s
#   p, q = q, p + q
# # x = fib(10)
# for i in fib(10):
#  print(i, end=', ')

##############################################################################

# def fib(n):
#  a = 0
#  b = 1
#  for i in range(n):
#   print(a)
#   s = a+b
#   a = b
#   b = s

# fib(10)

##############################################################################


# listData = [4, 4, 5, 6]
# for index, value in enumerate(listData):
#     print(index, ":", value)

##############################################################################

# def generateFibonacci():
#     a=0
#     b=1
#     for i in range(10):
#         yield b
#         a,b = b,a+b

# obj = generateFibonacci()

# print(obj)
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

##############################################################################

# def fibonacci():
#     x, y = 0, 1
#     while True:
#         yield x
#         x, y = y, x + y

# # Accept input from the user
# n = int(input("Input the number of Fibonacci numbers you
# want to generate? "))

# print("Number of first ",n,"Fibonacci numbers:")
# fib = fibonacci()
# for _ in range(n):
#     print(next(fib),end=" ")

##############################################################################

# class Queue(object):
#     def __init__(self):
#         self.instack=[]
#         self.outstack=[]
#     def enqueue(self,element):
#         self.instack.append(element)
#     def dequeue(self):
#         if not self.outstack:
#             while self.instack:
#                 self.outstack.append(self.instack.pop())
#         return self.outstack.pop()
# q=Queue()
# for i in range(2):
#     q.enqueue(i)
# for i in range(2):
#     print(q.dequeue())

##############################################################################

# def inverse_number(x):
#     return 15 - x


# # Example usage:
# result_for_4 = inverse_number(5)
# result_for_7 = inverse_number(10)

# print(result_for_4)  # Output: 7
# print(result_for_7)  # Output: 4

##############################################################################

# value = [10, 2]


# def f(value):
#     value.append(2)


# print(f(value))
# print(value)

##############################################################################

# def find_even_number(number):
#     if number % 2 == 0:
#         print(f"{number} is Even Number")
#     else:
#         print(f"{number} is Odd number")


# number = int(input("Enter the number:"))
# find_even_number(number)

##############################################################################

# def find_positive_negative(number):
#     if number < 0:
#         print(f"{number} is negative")
#     elif number == 0:
#         print(f"{number} is Zero")
#     else:
#         print(f"{number} is Positive")


# number = float(input("Enter the random number: "))
# find_positive_negative(number)

##############################################################################

# def find_prime_number(number):
#     flag = False
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 flag = True
#                 # print(i)
#                 break
#     if flag:
#         print(f"{number} is not prime number")
#     else:
#         print(f"{number} is prime number")
#
#
# number = int(input("Enter the random number: "))
# find_prime_number(number)

##############################################################################

# def is_palindrome(number):
#     original_number = number
#     reversed_number = 0
#
#     while number > 0:
#         print(number, "pppp")
#         digit = number % 10
#         print(digit, "qqqqq")
#         reversed_number = reversed_number * 10 + digit
#         print(reversed_number, "rrrrrrr")
#         number = number // 10
#         print(number, "ssssss")
#
#     return original_number == reversed_number
#
# # Example usage:
# num = 12321
#
# if is_palindrome(num):
#     print(f"{num} is a palindrome")
# else:
#     print(f"{num} is not a palindrome")

##############################################################################

# def check_anagrams(s1, s2):
#     if (sorted(s1) == sorted(s2)):
#         print("The strings are anagrams.", (sorted(s1), sorted(s2)))
#     else:
#         print("The strings aren't anagrams.")
#
#
# s1 = input("Enter string1: ")
# # input1: "listen"
# s2 = input("Enter string2: ")
# # input2: "silent"
# check_anagrams(s1, s2)
# # Output: the strings are anagrams.

##############################################################################

# def maximum_Number(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2


# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# f = maximum_Number(num1, num2)
# print(f)

##############################################################################

# def maximum_Number(num1, num2, num3):
#     if num3 < num1 > num2:
#         return num1
#     if num3 < num2 > num1:
#         return num2
#     if num1 < num3 > num2:
#         return num3


# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# num3 = int(input("Enter number3: "))

# f = maximum_Number(num1, num2, num3)
# print(f)

##############################################################################

# def minimum_Number(num1, num2, num3):
#     if num3 > num1 < num2:
#         return num1
#     if num3 > num2 < num1:
#         return num2
#     if num1 > num3 < num2:
#         return num3


# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# num3 = int(input("Enter number3: "))

# f = minimum_Number(num1, num2, num3)
# print(f)

##############################################################################

# def factorials(num):
#     factorial = 1
#     if num < 0:
#         print("Please provide a positive number")
#     elif num == 0:
#         print("Factorial of zero is 1")
#     else:
#         for i in range(1, num+1):
#             factorial = factorial * i
#         print(f"Factorial of {num} is {factorial}")


# number = int(input("Enter the random number: "))
# f = factorials(number)

##############################################################################

# def fibonacci(nterms):
#     a, b = 0, 1
#     count = 0

#     print(f"Fibonacci series of {nterms} is : ")
#     while count < nterms:
#         print(a, end=", ")
#         sum = a + b
#         a = b
#         b = sum
#         count += 1


# number = int(input("Enter the random number: "))
# fibonacci(number)

# def fibonacci(nterms):
#     a, b = 0, 1
#     count = 0

#     print(f"Fibonacci series of {nterms} is : ")
#     while count < nterms:
#         yield(a)
#         sum = a + b
#         a = b
#         b = sum
#         count += 1


# number = int(input("Enter the random number: "))
# for i in fibonacci(number):
#     print(i, end = ", ")

##############################################################################

# def find_gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# # Example usage:
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# gcd = find_gcd(num1, num2)
# print(f"The GCD of {num1} and {num2} is: {gcd}")

##############################################################################

# def myfunc(n):
#     for i in range(0, n):
#         for j in range(0, i+1):
#             print("* ", end="")
#         print("\n")


# n = 5
# myfunc(n)

##############################################################################

# def num(n):
#     num = 1
#     for i in range(0, n):
#         # num = 1
#         for j in range(0, i + 1):
#             print(num, end=" ")
#             num = num + 1
#         print("\r")
#
# n = 5
# num(n)
# #output
# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10
# # 11 12 13 14 15
##############################################################################

# l1 = [76, 23, 45, 12, 54, 9]
# print("Original List:", l1)

# # sorting list using nested loops
# for i in range(0, len(l1)):
#   for j in range(i+1, len(l1)):
#       if l1[i] >= l1[j]:
#           l1[i], l1[j] = l1[j], l1[i]

# # sorted list
# print("Sorted List", l1)

##############################################################################

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         less_than_pivot = [x for x in arr[1:] if x <= pivot]
#         greater_than_pivot = [x for x in arr[1:] if x > pivot]
#         return quicksort(less_than_pivot) + [pivot] + quicksort(
# greater_than_pivot)

########################################################################

# # Example usage:
# my_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# sorted_array = quicksort(my_array)
# print(sorted_array)

########################################################################

# non-repeated chars from string

# sample_string = "this is an interview"

# sample = sample_string.replace(" ", "")

# # 1st non-repeated character
# for i in range(len(sample)):
#     if sample[i] not in sample[i+1:] and sample[i] not in sample[:i]:
#         print(sample[i])
#         break


# # 3rd non-repeated character
# counter = 0
# for i in range(len(sample)):
#     if sample[i] not in sample[i+1:] and sample[i] not in sample[:i]:
#         counter += 1
#     if counter == 3:
#         print(sample[i])
#         break


#########################################################################

# Sort list without using inbuilt functions

# l = [1, 10, 8, 6]

# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[i] >= l[j]:
#             l[i], l[j] = l[j], l[i]
# print(l)

######################################################################
# List sorting without sort function

# l = [1, 10, 8, 6]

# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[i] >= l[j]:
#             l[i], l[j] = l[j], l[i]
# print(l)

# List sorting with sort function

# l = ["Shivu", "Raju", "Raghu", "Arun", "Yuvi"]

# l.sort()
# # l.sort(reverse=True)

# print(l)

#########################################################################

# reverse the String

# string = "string"
# reversedStr = string[:1]
# print(reversedStr)

#########################################################################

# read JSON data

# import json


# def readJson():
#     path = r"iexample.json"
#     f = open(path, "r")
#     data = json.loads(f.read())
#     print(data)
#     print(data.get("name"))
#     print(data.get("languages"))


# readJson()

#########################################################################

# # count the vowels in given string

# vowel = ['a', 'e', 'i', 'o', 'u']
# string = "My name is Yuvaraj"

# vowels_count = 0
# for char in string:
#     if char in vowel:
#         vowels_count += 1
# print(vowels_count)

# # counting consonants in given string

# vowel = ['a', 'e', 'i', 'o', 'u']
# string = "My name is Yuvaraj"

# consonants_count = 0
# for char in string.replace(" ", ""):
#     if char not in vowel:
#         consonants_count += 1
# print(consonants_count)

########################################################################

# # Counting the Number of Occurances of a Character in a String

# string = 'yuvaraj'

# char = 'a'
# count = 0
# for letter in string:
#     if letter == char:
#         count += 1
# print(count)

########################################################################

# fibonacci series using list

# n = 10
# fib = [0, 1]
# for i in range(n):
#     sum = fib[-1] + fib[-2]
#     fib.append(sum)
#     if sum >= n:
#         break
# print(fib)

########################################################################

# find maximum number for the unordered list

# l = [2, 4, 1, 5, 3]

# l.sort()
# print(l[-1])
#
# print(max(l))

# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[i] >= l[j]:
#             l[i], l[j] = l[j], l[i]
#         print(l)
# print(l[-1])

# maxNum = l[0]
# for num in l:
#     if maxNum < num:
#         maxNum = num
#         print(maxNum, "000")
#     # print(num)
# print(maxNum)

#######################################################################

# program to perform calculator using OOPs/inheritance

# class Calculator:
#     # def __init__(self) -> None:
#     #     pass

#     def summing(self, num1, num2):
#         return num1 + num2

#     def substract(self, num1, num2):
#         return num1 - num2

#     def multiply(self, num1, num2):
#         return num1 * num2

#     def divide(self, num1, num2):
#         return num1 / num2


# class Maths(Calculator):
#     # def __init__(self) -> None:
#     #     pass

#     def maths_operations(self, operation, num1, num2):
#         if operation == "+":
#             return self.summing(num1, num2)
#         if operation == "-":
#             return self.substract(num1, num2)
#         if operation == "*":
#             return self.multiply(num1, num2)
#         if operation == "/":
#             return self.divide(num1, num2)


# output = Maths().maths_operations('*', 5, 5)
# print(output)

#######################################################################

# Decorators

# def decore(fun):
#     def inner():
#         x = fun()
#         return x * x
#     return inner
#
# def decore1(fun):
#     def inner():
#         x = fun()
#         return 2 * x
#     return inner
#
# @decore
# @decore1
# def num():
#     return 10


# print(num())

#######################################################################

# lamda, filter and map funtion

# lamda
print((lambda x: x * 2)(3))

# filter
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter(lambda x: x % 2 == 0, list1)
d = list(filter(lambda x: x % 2 == 0, list1))
print(d)

# map
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = list(map(lambda x: x * 2, list1))
print(d)

#######################################################################

# # reverse string with multiple words

# name = "YUVARAJ AR"
# name1 = name.split(" ")
# print(name1)
# rev_name = []
# for word in name1:
#     rev_name.insert(0, word)
#     print(rev_name)
# print(" ".join(rev_name))

#######################################################################
