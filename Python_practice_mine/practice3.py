#Quick Sort
# Array=[1, 7, 4, 1, 10, 9, -2]
# def sortArray(Array):
#     if len(Array) <= 1 :
#         return Array
#     else:
#         pivot=Array[0]
#         left=[x for x in Array[1:] if x < pivot]
#         right=[x for x in Array[1:] if x >= pivot]
#         return sortArray(left) + [pivot] + sortArray(right)
#
#
# obj=sortArray(Array)
# print(obj)

# Array=[5,8,6,9,10]
# def Triplet(Array):
#     n=len(Array)
#     TargetSum=24
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if Array[i] + Array[j] + Array[k] == TargetSum:
#                     return [Array[i],Array[j],Array[k]]
#
# obj=Triplet(Array)
# print(obj)


'''Duplicate Element in Array'''
# def DuplicateArray(Array):
#     seen=[]
#     Duplicate=[]
#     for i in range(len(Array)):
#         if Array[i] in seen:
#             Duplicate.append(Array[i])
#         else:
#             seen.append(Array[i])
#     return seen, Duplicate


# Array=[1,1,2,3,4,5,8,2]
# obj=DuplicateArray(Array)
# print(obj)

'''Duplicate in 2 list'''
# def Dupin2():
#     A=[1,3,6,7,8]
#     B=[1,2,0,4,9]
#     c=[]
#     for i in range(len(A)):
#         for j in range(len(B)):
#             if A[i] == B[j]:
#                 c.append(A[i])
#     print(c)
#
# Dupin2()

'''largest element in Array'''
# def largestelement(Array):
#     max=Array[0]
#     for i in range(len(Array)):
#         if Array[i] > max:
#             max = Array[i]
#     return max
#
#

'''Second Largest Element in a Array'''
# def SecondLargest(Array):
#     n=len(Array)
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if (Array[i]>Array[j]):
#                 temp = Array[i]
#                 Array[i] = Array[j]
#                 Array[j] = temp
#     print(Array[-2])
#
# Array=[9,3,2,4,5,6,9]
# SecondLargest(Array)

'''frequency of the Element in Array'''
# def frequecny(Array):
#     freq={}
#     for i in Array:
#         freq[i] = freq.get(i,0)+1
#     return freq
#
# Array=[1,2,1,3,4,5,3]
# obj=frequecny(Array)
# print(obj)


'''Given String is Anagram'''
# def Anagram():
#     str1="heart"
#     str2="earth"
#     if len(str1) != len(str2):
#         print("its not A Anagram")
#     else:
#         if sorted(str1) == sorted(str2):
#             print("its a Anagram")
#         else:
#             print("its not a Anagarm")
#
# Anagram()

'''Reverse an Array'''
# def reverseArray():
#     str="GADAG"
#     if str == str[::-1]:
#         print("its a Palindrome")
# reverseArray()


'''Count a Voules in An string'''
# def countvowel():
#     str="some test Text"
#     count=0
#     for vowel in str:
#         if (vowel in "AaEeIiOoUu"):
#             count = count+1
#     print(count)
#
# countvowel()
# def vowels(str):
#     newstr=""
#     index=len(str)-1
#     while index >= 0:
#         newstr =newstr+str[index]
#         index =index -1
#     print(newstr)
# vowels("Television")

'''Sum of the Array'''
# def sumofArray():
#     Array=[2,9,0,0]
#     sum=0
#     for i in Array:
#         sum=sum+i
#     print(sum)
#
# sumofArray()

'''Find Missing Element in An Array'''
def MissingElement():
    Array=[1,3,4,]
    N=len(Array)
    sum=((N+1)*(N+2)//2)
    total=0
    for i in Array:
        total=total+i
    missingElement=sum-total
    print(missingElement)

# MissingElement()

'''Even No'''
# def evenNo():
#     num=3
#     if num <= 0:
#         print("its  not a even no")
#     else:
#         if num > 1:
#             if num%2 == 0:
#                 print("its a even No")
#             else:
#                 print("its a Odd no")
#
# evenNo()
'''Factorial of a no'''
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num* factorial(num-1)
#
# obj=factorial(5)
# print(obj)

# def factorial(Num):
#     if Num ==0 or Num == 1:
#         return 1
#     else:
#         return Num * factorial(Num-1)
#
# obj=factorial(5)
# print(obj)
''''''
"""prime no"""
# def primeno(N):
#     c=2
#     while N!=0:
#         for i in range(2,int(c**0.5)):
#             if c%i == 0:
#                 break
#         else:
#             print(c,end=" ")
#             N=N-1
#         c=c+1
#
# primeno(13)

'''FibocisSerie'''
# def fib(N):
#     S=0
#     A=0
#     B=1
#     for i in range(N):
#         print(S,end=" ")
#         S=A+B
#         B=A
#         A=S
#
# fib(10)
# def fibnocis(N):
#     if N <= 1:
#         return N
#     else:
#         return fibnocis(N-1) + fibnocis(N-2)
#
#
# N=15
# if N <=1:
# for i in range(N):
#     print(fibnocis(i))


'''ValidateIp'''
#
#
# def validation1(ip_address):
#     ip = ip_address.replace(".", "")
#     valid_ip1 = ip.isnumeric()
#     return valid_ip1
#
#
# def validation2(ip_address):
#     ip = ip_address.split(".")
#     if len(ip) == 4:
#         return True
#     else:
#         return False
#
#
# def validation3(ip_address):
#     ip = ip_address.split(".")
#     for i in ip:
#         if int(i) <= 0 or int(i) >= 255:
#             return False
#         return True
#
#
# ip_address = "255.255.255.255"
#
# if all([validation1(ip_address), validation2(ip_address), validation3(ip_address)]):
#     print("Given IP is Valid")
# else:
#     print("Given IP is Invalid")

# import re
#
# def validateIp(Ip):
#     # IPv4=r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
#     # IPv4=r"((([0-9a-fA-F]){1,4})\:){7}([0-9a-fA-F]){1,4}"
#     # # IPv4="((([0-9a-fA-F]){1,4})\\:){7}([0-9a-fA-F]){1,4}"
#     IPv4=r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
#     IPv6=r"^((([0-9a-fA-F]){1,4})\:){7}([0-9a-fA-F]){1,4}"
#
#     if re.match(IPv4,Ip):
#         print("Match")
#     elif re.match(IPv6,Ip):
#         print("Match is Found")
#     else:
#         print("its neither IPV4 or IPv6")
# # validateIp(Ip="fffe:3465:efab:23fe:2235:6565:aaab:0001")
# validateIp(Ip="255.120.223.13")


'''Stringadding'''
# input_str = "Television"
# result_str = ""
#
# for char in input_str:
#     if input_str.count(char) > 1:
#         result_str += '*'
#     else:
#         result_str += char
#
# print(result_str)

'''Reversing an List'''
# Array=[1,2,90,5,8]
# ReveresedArray=[]
# index=len(Array)-1
# while index >=0:
#     ReveresedArray = ReveresedArray + [Array[index]]
#     index-=1
#
# print(ReveresedArray)

'''Find a Key in Dictionary'''
# dict={1:"shiv",2:"raj"}
# user_ip="shiv"
# if user_ip in dict.values():
#     print("its present")
#     # print(dict.keys())

'''counr in Dictionary'''
# str="python is a programming Language python learn"
# words=str.split(" ")
# dict={}
# for word in words:
#     letter=word[0]
#     if letter not in dict:
#         dict[letter] = []
#     dict[letter].append(word)
# print(dict)
'''string Manupulation'''

# str="ceredian"
# output="c1e2r3.."
# str="ceredian"
# newOutpuu="".join(f"{i}{char}" for i,char in enumerate(str,start=1))
# print(newOutpuu)
''' '''
# import subprocess
#
# def hostname():
#     # hostname=socket.gethostname()
#     # print(hostname)
#     subprocess.run(['hostname'])
#     subprocess.run(['ipconfig'])
#
#
#     # # Get the IP address of the local machine
#     # # ip_address = socket.gethostbyname(socket.gethostname())
#     # ip_address=socket.gethostbyname(socket.gethostname())
#     #
#     # print("IP Address:", ip_address)
#
#
# # hostname()
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Remove the third item (key-value pair)
for _ in range(2):
    key, value = my_dict.popitem()
print("Removed Item:", (key, value))
print("Updated Dictionary:", my_dict)

# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#
# # Remove the third item (key-value pair)
# for _ in range(2):
#     key, value = my_dict.popitem()
#
# print("Removed Item:", (key, value))
# print("Updated Dictionary:", my_dict)


'''Reversing an List'''
# Array=[1,2,90,5,8]
# ReveresedArray=[]
# index=len(Array)-1
# while index >=0:
#     ReveresedArray = ReveresedArray + [Array[index]]
#     index-=1
#
# print(ReveresedArray)
# string=[1,3,5,7]
# index=len(string)-1
# rever=[]
# while index >=0:
#     rever = rever + [string[index]]
#     index =index -1
# print(rever)
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         # Check if the target is in the middle
#         if arr[mid] == target:
#             return mid
#
#         # If the target is smaller, ignore the right half
#         elif arr[mid] > target:
#             right = mid - 1
#
#         # If the target is larger, ignore the left half
#         else:
#             left = mid + 1
#
#     # If the target is not in the array
#     return -1

# Example usage
# sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target_element = 2
#
# result = binary_search(sorted_list, target_element)
#
# if result != -1:
#     print(f"Element {target_element} found at index {result}")
# else:
#     print(f"Element {target_element} not found in the list")

# def recursive_fibonacci(n):
#   if n <= 1:
#       return n
#   else:
#       return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
# recursive_fibonacci(5)
#
# n_terms = 10
# if n_terms <= 0:
#   print("Invalid input ! Please input a positive value")
# else:
#   print("Fibonacci series:")
# for i in range(n_terms):
#     print(recursive_fibonacci(i))

# def Freq(Array):
#     freq={}
#     for i in Array:
#         freq[i] = freq.get(i,0)+1
#         A=max(freq,key=freq.get)
#     return A
#
# R=Freq("shivaraj")
# print(R)



# class School:
#     def __init__(self):
#         print("HI i am Shivaraj")
#
#
#     def E1(self):
#         print("A")
#
# class student(School):
#
#     def __init__(self):
#         # super().__init__()
#         print("Shruddha")
#
#     def E2(self):
#         print("B")
#
# class Name(student):
#
#     def __init__(self):
#         super().E1()
#         print("Ravan")
#
#     def E3(self):
#         print("C")
#
# # obj=School()
# # obj.
# # obj=student()
# # obj.E2()
# obj=Name()
# obj.E3()
# Input = {"vjw": "ap", "vsp": "ap", "bng": "ka", "chn": "tn", "cmb": "tn", "mys": "ka", "hyd": "tg", "tpt": "ap"}
# output={}
# for city,state in Input.items():
#     if state not in output:
#         output[state] = [city]
#     else:
#         output[state].append(city)
#
# print(output)
# output["ka"] =["blr","mys"]
# print(output)

# def fibonacci_generator():
#     # Initialize first two Fibonacci numbers
#     a, b = 0, 1
#     while True:
#         yield a  # Yield the current Fibonacci number
#         a, b = b, a + b  # Calculate the next Fibonacci number
#
# # Create a generator object for Fibonacci sequence
# fib_gen = fibonacci_generator()
#
# # Generate and print the first 10 Fibonacci numbers
# for _ in range(10):
#     print(next(fib_gen))

# def validateIP():
#     IP="250.223.250.a."
#     splitedString=IP.split(".")
#     if len(splitedString) == 4:
#         numeric = "".join(splitedString)
#         if numeric.isnumeric():
#             for i in splitedString:
#                 if 0 <= int(i) <= 255:
#                     return True
#                 else:
#                     return False
#         else:
#             return False
#
#     else:
#         return False
#
#
# if validateIP():
#     print("its valid")
# else:
#     print("not valid")
import ipaddress


# def validateIP(IP):
#     # octets = IP.split(".")
#     # return len(octets) == 4 and all(o.isdigit() and 0 <= int(o) <= 255 for o in octets)
#     IpAddress=IP.split(".")
#     return len(IpAddress) == 4 and all(i.isdigit() and 0 <= int(i) <= 255 for i in IpAddress)
#
# IP="1.250.214.56"
# if validateIP(IP):
#     print("true")
# else:
#     print("False")