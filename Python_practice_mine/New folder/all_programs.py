"""prime number"""
def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print('not a prime')
                break
        else:
            print("prime")

    else:
        print('not a prime')


# prime(4)

def prime100to200():
    for n in range(100,200):
        for i in range(2,n):
            if n % i == 0:
                # print(f'{n} not a prime')
                break
        else:
            print(f"{n} is prime")
# prime100to200()
# l=[]
#     if prime100to200(i):
#         l.append(i)
# print(l)


'''prime number from a list of numbers'''
def primeFromList(lst):
    # for i in lst:
    #     factors = 0
    #     for j in range(2, i + 1):
    #         if i % j == 0:
    #             factors += 1
    #     if factors == 1:
    #         print(i)
#or
    for i in lst:
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print(f'{i} is prime number')


mylist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primeFromList(mylist)


'''fibonacci without recursion'''
def fib(n):
    a, b = 0, 1
    if n == 0:
        print(f"fib series of {n} is {a}")
    # elif n == 1:
    #     print(f"fib series of {n} is {b}")
    elif n < 0:
        print("fib series is not possible")
    else:
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b


# fib(1)


'''fibonacci with recursion'''
def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n<0:
        return 'fib not possible'
    else:
        return (fib_recursive(n - 1) + fib_recursive(n - 2))


for i in range(5):
    # print(i)
    print(fib_recursive(i), end=" ")

def fib_recursive(n):
    if n < 0:
        return 'Fibonacci not possible for negative numbers'
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# Example usage:
# n = 10
# result = fib_recursive(n)
# print(f"The {n}th Fibonacci number is {result}")




'''factorial'''


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    print(fact)


# factorial(4)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(4))

'''star pattern right angle'''


def starRightAngle(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=" ")
        print()


# starRightAngle(7)
# for i in range(5):
#     for j in range(i+1):
#         print(" ", end="")
#     for k in range(5-j):
#         print("* ", end="")
#     print()

'''triangle star pattern'''


def startriangle(n):
    # k = n - 1
    # for i in range(0, n):
    #     for j in range(0, k):
    #         print(end=" ")
    #     k = k - 1
    #     for j in range(0, i + 1):
    #         print("*", end=" ")
    #     print()
    for i in range(n):
        for j in range(n - i):
            print(" ", end="")
        for k in range(i + 1):
            print("*", end=" ")
        print()

# startriangle(7)

'''inverted triangle'''

def invertedpyramid(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(n - i):
            print("*", end=" ")
        print()

# invertedpyramid(7)

'''invert triangle Left Side'''

def invertRightTriangeLeftSide(n):
    for i in range(n):
        for j in range(i):
            print("", end="")
        for k in range(n-i):
            print("*", end=" ")
        print()

# invertRightTriangeLeftSide(7)


'''Invert right Triangle Right Side'''
def invertRightTriangeRightSide(n):
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for k in range(n-i):
            print("*", end=" ")
        print()

# invertRightTriangeRightSide(7)


'''palindrome'''


def palindrome(data):
    rev_data = ""
    for i in str(data):
        rev_data = i + rev_data
    print(rev_data)

    if rev_data == str(data):
        print("palindrome")
    else:
        print("not a palindrome")


# palindrome("samase")


'''reverse the char and place in same position'''
def reverse(string):
    reversedlist = []
    # revstr = ""
    splitstring = string.split()
    # print(splitstring[::-1])
    for i in splitstring:
        # # print(i)
        # for char in i:
        #     revstr = char+revstr
        revstr = i[::-1]
        reversedlist.append(revstr)

    print(reversedlist)
    print(" ".join(reversedlist))

string1 = "this is interview"
output = ""
word = ""
# for work in string1.split():
def reverseString():
    for char in string1:
        print(char)
        if char != " ":
            word = char + word
            print(word, "111111")
        else:
            output = output + word + char
            word = ""
            print(output, "2222222")
    print(output, word)
    output += word
    print(output)
# Loop through each character in the string
# for char in string1:
#     print(char)
#     if char != " ":  # If the character is not a space
#         word = char + word  # Prepend the character to the word
#     else:
#         # When a space is encountered, add the reversed word to output
#         output += word + " "
#         word = ""  # Reset word for the next word
#
# # Don't forget to add the last word after the loop
# output += word  # Add the final reversed word
# print(output, "11111")
# Now we need to remove the spaces between the reversed words
# final_output = ""
# for i in output.split():
#     reversed_word = ""
#     for char in i:
#         reversed_word = char + reversed_word  # Reverse the current word
#     final_output += reversed_word + " "
#
# # Trim the final output to remove any trailing space
# final_output = final_output.strip()
#
# print(final_output)



# string1 = "this is interview"
# reverse(string1)

'''bubble sort or sorting a list'''
def sortinglist(lt):
    for i in range(len(lt)):
        for j in range(i + 1):
            if lt[i] < lt[j]:
                lt[i], lt[j] = lt[j], lt[i]
    print(lt)


listt = [8, 1, 9, 2, 7, 0, 4, 5, 3, 6]
# sortinglist(lt=listt)


'''sum of two values = target in a list'''
def getTargetvalues(lt, target):
    targetvalueslist = []
    for i in range(len(lt)):
        for j in range(i + 1):
            if lt[i] + lt[j] == target and i != j:
                print(lt[i], lt[j])
                # targetvalueslist.extend([lt[i], lt[j], "&&"])

    # print(targetvalueslist)


listt = [8, 1, 9, 2, 7, 0, 4, 5, 3, 6, 10]
# getTargetvalues(lt=listt, target=10)


'''count the occurences of char's in a string'''
def count(data):
    count_dict = {}
    for i in data:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    print(count_dict)

    print(max(count_dict, key=count_dict.get))

    combinestr = ""
    for k, v in count_dict.items():
        combinestr = combinestr + f"{v}{k}"
    print(combinestr)


# count('aabbbccddd')


'''reverse to above i/p:  a4b3c2   o/p:  aaaabbbcc'''
def aaabbccc(data):
    num = []
    alpha = []
    for i in data:
        if i.isnumeric():
            num.append(i)
        elif i.isalpha():
            alpha.append(i)
    print(alpha, num)

    combstr = ''
    for j in range(len(num)):
        combstr = combstr + alpha[j]*int(num[j])
    print(combstr)

# aaabbccc(data='a4b3c2')

#or

def aabbbcccc(data):
    final = ''
    for i in range(len(data)):
        if i%2==0:
            key = data[i]
        else:
            value = data[i]
            key = key*int(value)
            final += key
    print(final)

# aabbbcccc("a4b3c3")

'''
sentence= "Given a text file fname the task characters and the lines"
d = {'G':'Given', 'a':['a','and'], 't':['text','task','the', 'the'], 'f': ['file', 'fname'], 'c':'characters', 'l':'lines'}
'''

def countWords(sentence):
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


'''create a dict using two lists'''
def createdict():
    l1 = ['a', 'b', 'c']
    l2 = [1, 2, 3]
    dic = {}

    # for k, v in zip(l1, l2):
    #     dic[k] = v
    for i in range(len(l1)):
        dic[l1[i]] = l2[i]
    print(dic)


# createdict()


'''addition of two dict's'''
def combinedicts():
    d1 = {1: 200, 2: 300, 3: 500}
    d2 = {1: 500, 2: 700, 4: 600}
    for k in d2:
        if k in d1:
            d1[k] += d2[k]
        else:
            d1[k] = d2[k]

    print(d1)

    # print({**d1, **d2}) #merge two dicts in a single line
# combinedicts()


'''leap year'''
def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is leap year")
            else:
                print(f"{year} is not leap year")
        else:
            print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")


# leap(2006)


'''odd and multiples of 5'''
def oddAndMulOf5():
    l2 = [10, 15, 20, 25, 30, -5, -30, 3]
    for i in l2:
        # if i >= 5:
        if i % 2 != 0 and i % 5 == 0:
            continue
        else:
            l2.remove(i)

    print(l2)


# oddAndMulOf5()

'''seperate even and odd list'''
def evenOrOddusingcomprehension():
    l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even = [i for i in l3 if i % 2 == 0]
    odd = [j for j in l3 if j % 2 != 0]
    evendict = {i: i ** 2 for i in l3 if i % 2 == 0}
    odddict = {i: i ** 2 for i in l3 if i % 2 != 0}

    print(f"even: {even}\nodd: {odd}\neven dict: {evendict}\nodd dict: {odddict}")


# evenOrOddusingcomprehension()


'''reverse a list ??????????????'''
def reverseList():
    l3 = [1, 2, 3, 4, 5]
    # rev_l3 = []
    for i in range(len(l3)):
        l3.insert(i, l3.pop())
    print(l3)


# reverseList()


'''lambda(single and multiple args) & map & filter'''

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = lambda a: a ** 2
# print(a(5)) #25

d = lambda *arg: sum(arg)  # multiple arguments
# print(d(*l)) #55

b = list(map(lambda a: a % 2 == 0, l))
# print(b) #[False, True, False, True, False, True, False, True, False, True]

c = list(filter(lambda a: a % 2 == 0, l))
# print(c) # [2, 4, 6, 8, 10]

from functools import reduce
result = reduce(lambda x,y : x+y, l)
# print(result)


'''SET'''

my_set = {9, 9.0}

# Display the set
# print("Set contents:", my_set) #{9}

# for item in my_set:
# print(f"Element: {item}, Type: {type(item)}") #Element: 9, Type: <class 'int'>


'''print calender'''
import calendar

# print(calendar.TextCalendar().formatmonth(theyear=2024, themonth=9))


'''add two matrix'''
def addTwoMatrix():
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        # [7, 8, 9]
    ]
    m2 = [
        [10, 11, 12],
        [13, 14, 15],
        # [16, 17, 18]
    ]
    # result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    result = [[0,0,0],
              [0,0,0],]
              # [0,0,0]]
    for i in range(len(m1)):
        for j in range(len(m2)):
            result[i][j] = m1[i][j] + m2[i][j]

    for r in result:
        print(r)


# addTwoMatrix()


'''generator - yield, __next__()'''
def square(n):
    for i in range(1, n):
        yield i * i


a = square(5)
# for i in a:
#     print(i)
# print(a.__next__())


'''decorator'''
def decorfun(fun):
    def inner_fun():
        result = fun()
        return result.upper()

    return inner_fun


@decorfun
def str():
    return 'sanju'


# print(str())


# Decorators

def decore(fun):
    def inner():
        x = fun()
        return x * x

    return inner


def decore1(fun):
    def inner():
        x = fun()
        return 2 * x

    return inner


@decore
@decore1
def num():
    return 10

# print(num())

# def main():
#     print("This is the main function.")
#
# if __name__ == '__main__':
#     main()  # This will only run if the script is executed directly


'''missing elements in an array'''
def miss(arr):
    for i in range(len(arr)):
        for j in range(i + 1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    missingelements = []
    for i in range(arr[0], arr[-1] + 1):
        if i not in arr:
            missingelements.append(i)
    print(missingelements)


Array = [1, 3, 4, 7, 9]
# miss(arr=Array)


'''Ip validation'''
def ipValidate(ip):
    ipsplit = ip.split(".")
    print(ipsplit)
    if len(ipsplit) != 4:
        return False
    # ipsplit = ip.split(".")
    for i in ipsplit:
        if not i.isnumeric() or not (0 <= int(i) <= 255):
            return False
    return True


ip = "192.168.0.255"
# if ipValidate(ip):
#     print(f"{ip} is valid")
# else:
#     print(f"{ip} is not a valid")


'''string manupilation by adding index'''
def strmanind(string):
    addstring = ''
    for i, v in enumerate(string, start=1):
        addstring = addstring + f"{i}{v}"
    print(addstring)


str = "ceredian"
# strmanind(str)

'''SUBPROCESS & OS module'''
import subprocess

# subprocess.run('ipconfig')
# subprocess.run(["python", "--version"])


import os
# os.system('ipconfig')
# os.system("python --version")


'''convert even position elements to Upper'''
def converteven(string):
    conword = ''
    word1 = string.upper()
    word2 = string.lower()
    for i in range(len(string)):
        if i % 2 == 0:
            conword += word1[i]
        else:
            conword += word2[i]

    print(conword)


# converteven("python programming")


'''Identity vs Equality operators'''

list1 = []
list2 = []
list3 = list1

# # case 1
# if (list1 == list2):
#     print("True")
# else:
#     print("False")
#
# # case 2
# if (list1 is list2):
#     print("True")
# else:
#     print("False")
#
# # case 3
# if (list1 is list3):
#     print("True")
# else:
#     print("False")
#
# # case 4
# list3 = list3 + list2
#
# if (list1 is list3):
#     print("True")
# else:
#     print("False")

'''
'==' checks values for equality.
'is' checks object identity (same location in memory).

The output of the first case, if the condition is “True” as both list1 and list2 are empty lists
The output of the second case, if the condition shows “False” because two empty lists are at different memory locations. 
    Hence list1 and list2 refer to different objects. We can check it with id() function in python which returns the “identity” of an object.
The output of the third case, if the condition is “True” as both list1 and list3 are pointing to the same object.
The output of the fourth case, if the condition is “False” because the concatenation of two lists always produces a new list.
'''

'''Shallow copy and deep copy'''

import copy

mylst = [2, 3, [4, 5, [6, 7, 8], 9, 10], [11, 12, 13], 14, 15]


def shallowcopy(lt):
    s_lst_copy = copy.copy(mylst)
    s_lst_copy[0] = 'a'
    s_lst_copy[2][0] = 'b'
    s_lst_copy[2][2][0] = 'c'
    print(f"shallow copy list: {s_lst_copy}")  # ['a', 3, ['b', 5, ['c', 7, 8], 9, 10], [11, 12, 13], 14, 15]
    print(f"original list: {mylst}")           # [2, 3, ['b', 5, ['c', 7, 8], 9, 10], [11, 12, 13], 14, 15]


#deep copy
def deepcopy(lt):
    deep_copy = copy.deepcopy(mylst)
    deep_copy[0] = 'a'
    deep_copy[2][0] = 'b'
    deep_copy[2][2][0] = 'c'
    print(f"deep copy list: {deep_copy}")  # ['a', 3, ['b', 5, ['c', 7, 8], 9, 10], [11, 12, 13], 14, 15]
    print(f"original list: {mylst}")       # [2, 3, [4, 5, [6, 7, 8], 9, 10], [11, 12, 13], 14, 15]


# shallowcopy(lt=mylst)
# deepcopy(lt=mylst)


'''sorted dict keys'''


def sortdictkeys(dt):
    keys = list(dt.keys())
    print(keys)
    for i in range(len(keys)):
        for j in range(i + 1):
            if keys[i] < keys[j]:
                keys[i], keys[j] = keys[j], keys[i]

    print(keys)
    sorteddict = {}
    for i in keys:
        sorteddict[i] = dt[i]
    print(sorteddict)


# sortdictkeys(dt = {'b': 1, 'a': 2, 'c': 3})



'''dict to list'''

def dictToList(dt):
    lt = []
    for k,v in dt.items():
        lt.append(k)
        if type(v) == dict:
            for k1,v1 in v.items():
                lt.extend([k1,v1])
        elif type(v) == list:
            lt.extend(v)
        else:
            lt.append(v)
    print(lt)

# dictToList({'a': 1, 'b': {'c': 2}, 'd': [3, 4]})



'''File Handling'''

'''return the line number of sentence from a file'''


def line_number(sentence, filepath):
    try:
        with open(filepath, 'r') as data:
            # print(data.readlines())
            for lineNumber, value in enumerate(data, start=1):
                if sentence in value:
                    return lineNumber
    except FileNotFoundError:
        print(f"{filepath} is not found")
    except Exception as e:
        print(f"exception error is {e}")


# print(line_number(sentence="Smoke Testing", filepath=r"C:\Users\Admin\Desktop\python_questions.txt"))


# Replace the old word with the new word in a file

def replace_word_in_file(filepath, oldword, newword):
    with open(filepath, 'r') as file:
        content = file.read()

    updated_content = content.replace(oldword, newword)
    with open(filepath, 'w') as file:
        file.write(updated_content)

# replace_word_in_file(filepath=r"C:\Users\Admin\OneDrive\Desktop\data.txt", oldword='java', newword='python')


'''reading even lines from the file'''
def readEvenLinesFromFile(filepath):
    with open(filepath, 'r') as data:
        i=1
        for line in data.readlines():
            if i%2==0:
                print(line)
            i+=1

# readEvenLinesFromFile(filepath=r'C:\Users\Admin\Desktop\python_questions.txt')


'''reading data from a file'''

def readData(filePath):
    text = r"C:\Python312\python.exe C:\Source\Python_practice_mine\New folder\all_programs.py"
    try:
        with open(filePath, 'r+') as data:
            result = data.readlines()
            # print(result[-1].strip())
        #     print(result)
        # with open("writedata.txt", 'w') as write:
        #     for i in result:
            data.seek(0,2) # go to end of the file
            data.write(text)
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print(f"exception is {e}")
    finally:
        data.close()
        # write.close()
# readData(filePath=r"C:\Users\Admin\Desktop\data.txt")



'''printing the hello world without print() function'''

import sys
# sys.stdout.write('Hello World')


'''JSON file operations'''

# from PycharmProjects.PythonPractice.JsonAndCSVPractice import
import json

def JsonFileReadData(filepath):
    try:
        with open(filepath, 'r') as data:
            result = json.load(data)
            return result
    except FileNotFoundError:
        print("file not found")
    finally:
        data.close()


def JsonFileWriteData(data, filePath):
    with open(filePath, 'w') as write:
        json.dump(data, write, indent=4)


'''write And Append Data To Existed Json File'''
def writeAndAppendDataToExistedJsonFile(filepath):
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

# writeAndAppendDataToExistedJsonFile(filepath=r"C:\Source\Python_practice_mine\New folder\csvtojsoncontent.json")


d1 = {1: 200, 2: 300, 3: 500}

# a = JsonFileReadData(filepath=r'C:\Source\PycharmProjects\PythonPractice\JsonAndCSVPractice\primedict.json')
# print(a)
# d1.update(a)
# print(d1.keys())
# JsonFileWriteData(data=d1, filePath="content.json")


'''CSV File Operations'''

import csv

def csvreaderdata(filepath):
    remainingdata= []
    with open(filepath, 'r') as f:
        data = csv.reader(f)
        header = next(data) # gets the first line as a title/header
        # print(f"title header: {header}")
        for i in data:
            remainingdata.append(i)

        # print(remainingdata)
        return header, remainingdata


def csvwriterdata(filepath, data, header):
    print(header)
    print(data)
    with open(filepath, 'w', newline='') as w:
        writer = csv.writer(w)
        writer.writerow(header)
        writer.writerows(data)

# b,c = csvreaderdata(filepath=r"C:\Source\PycharmProjects\PythonPractice\JsonAndCSVPractice\stock_data.csv")
# print(b,c)
# c[0][0] = 'SAMSUNG'
# csvwriterdata(filepath=r"content.csv", data=c, header=b)

'''JSON to CSV'''

# import json
# import csv

def jsonToCsv(jsonfilepath, csvfilepath):
    with open(jsonfilepath, 'r') as jsondata:
        result = json.load(jsondata)
        print(result)
    with open(csvfilepath, 'w', newline='') as csvdata:
        writer = csv.DictWriter(csvdata, result.keys())
        writer.writeheader()
        writer.writerow(result)

# jsonToCsv(jsonfilepath="content.json", csvfilepath="jsontocsvcontent.csv")


'''CSV to JSON'''

def csvToJson(jsonfilePath, csvFilepath):
    with open(csvFilepath, 'r') as data:
        result = csv.DictReader(data)
        # header = next(result)
        values = []
        for i in result:
            values.append(i)
        #
        # print(header)
        print(values)
    with open(jsonfilePath, 'w') as writer:
        json.dump(values[0], writer, indent=4)
# csvToJson(jsonfilePath="csvtojsoncontent.json", csvFilepath="jsontocsvcontent.csv")


"**********************************************************************"
def extract_values(file_path):
    # Dictionary to store the extracted values
    extracted_values = {}

    # Open the file and read its contents
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into key and value based on the delimiter ": "
            if ": " in line:
                # print(line)
                key, value = line.strip().split(": ")
                print(line.strip().split(": "))
                print(key, "mmmmmm", value)
                extracted_values[key] = value

    return extracted_values

# Example usage
# file_path = r'C:\Users\Admin\OneDrive\Desktop\example.txt'
# values = extract_values(file_path)
# print(values)
#
# # # Accessing specific values
# name = values.get('Name')
# age = values.get('Age')
# occupation = values.get('Occupation')
# location = values.get('Location')
#
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Occupation: {occupation}")
# print(f"Location: {location}")

# def values_target():
# # Example of extracting values from a file with space-separated data
#     with open(r"C:\Users\Admin\OneDrive\Desktop\example.txt", 'r') as file:
#         for line in file:
#             # Strip any leading/trailing spaces or newline characters
#             line = line.strip()
#
#             # Split the line based on spaces
#             parts = line.split()  # You can use a different delimiter, such as ',' or '\t'
#
#             # Extract key and value (assuming the first part is the key and the second is the value)
#             key = parts[0]
#             value = parts[1] if len(parts) > 1 else None
#
#             print(f"Key: {key}, Value: {value}")
#
# # values_target()



"**********************************************************************"
def extract_values_by_line_position(file_path):
    extracted_values = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(lines)
        # Iterate over lines in pairs (key, value)
        for i in range(0, len(lines), 2):
            print(i)
            key = lines[i].strip()
            print(key)
            if i + 1 < len(lines):
                value = lines[i + 1].strip()
                extracted_values[key] = value

    return extracted_values


# Example usage
# file_path = r'C:\Users\Admin\OneDrive\Desktop\example.txt'
# values = extract_values_by_line_position(file_path)
# print(values)


"**********************************************************************"
def csvreaderdataForRequiredValue(filepath):
    remainingdata= []
    with open(filepath, 'r') as f:
        data = csv.reader(f)
        header = next(data) # gets the first line as a title/header
        # print(f"title header: {header}")
        print(header, type(header))
        for i in data:
            remainingdata.append(
                {header[name]: i[name] for name in range(len(header))}
            )
        for i in range(len(remainingdata)):
            print(remainingdata[i].get('tickers'))
        # return header, remainingdata

# csvreaderdataForRequiredValue(filepath=r"C:\Source\PycharmProjects\PythonPractice\JsonAndCSVPractice\stock_data.csv")


#
# '''convert even opsition elemements to Upper'''
#
# def uppercovert(data):
#     new  = ''
#     word1 = data.upper()
#     word2 = data.lower()
#     for index in range(0, len(data)):
#         if index%2==0:
#             new = new+ word1[index]
#         else:
#             new = new + word2[index]
#     print(new)
#
# uppercovert('hihowareyou')


'''dict to list'''

def dictToList(dt):
    lt = []
    for k,v in dt.items():
        lt.extend([k,v])

    print(lt)

d1 = {1: 200, 2: 300, 3: 500}
# dictToList(dt=d1)


'''duplicate'''

def dup(lt):
    for i in range(len(lt)):
        if i < len(lt):
            if lt.count(lt[i]) > 1:
                lt.remove(lt[i])

    print(lt)

# dup(lt=[1,2,3,4,1,2,3,4,5,110,120,110])

'''Remove all duplicates from a given string'''

def removeDuplicateFromString(strng):
    # st = ''
    for i in strng:
        # if i not in st:
        #     st += i
        if strng.count(i) >1:
            strng.replace(i, "")
    print(strng)

# removeDuplicateFromString(strng='hi how our you?')


# Function to print inverted full pyramid pattern
def inverted_full_pyramid(n):
    # Outer loop for the number of rows
    for i in range(n, 0, -1):
        # Inner loop for leading spaces in each row
        for j in range(n - i):
            print(" ", end="")
        # Inner loop for printing asterisks in each row
        for k in range(2*i - 1):
            print("*", end="")
        # Move to the next line after each row
        print("")

# Set the value of n (number of rows)
n = 5

# Call the function to print the inverted full pyramid
# inverted_full_pyramid(n)


'''Numbers triangle pattern 
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5  
'''

def numpattern(n):
    for num in range(n):
        for i in range(num):
            print(num, end=" ")
        print(" ")

# numpattern(6)


'''most Repeated Element In Matrix'''

matlist = [[1,2,4],
           [3,4,5],
           [4,6,7]]

def mostRepeatedElementInMatrix(matrix=matlist):
    countdict = {}
    for lst in matrix:
        for i in lst:
            if i in countdict:
                countdict[i] +=1
            else:
                countdict[i] = 1
    print(countdict)
    for k,v in countdict.items():
        if v == len(matrix):
            return k

# print(mostRepeatedElementInMatrix())


'''get highest count word from sentence'''

st = 'hi sadik hello hi how sadik hi'
res = 2
sp = st.split()
def count(st=sp, res=res):
    d = {}
    for i in st:
        if  i in d:
            d[i] +=1
        else:
            d[i] = 1
    print(d)
    for k,v in d.items():
        if v >= res:
            yield k

# a = count()
# for i in a:
#     print(i)


'''sample example code contains all OOPS Concepts'''

from abc import ABC, abstractmethod
'''Abstraction'''
class vehicle(ABC):

    @abstractmethod
    def engineCondition(self):
        pass


class specs(vehicle):
    '''parameterized constructor'''
    def __init__(self, color, features, varients, engineCondition):
        '''encapsulation'''
        self.color = color # public
        self.features = features
        self.varients = varients
        self._engineCondition = engineCondition # protected

    def engineCondition(self):
        if self._engineCondition is True:
            print("Engine started")
        else:
            print("Engine stopped")


class car(specs):
    '''class variable'''
    wheels = 4
    def __init__(self, brand, color, features, varients, engineCondition):
        self.brand = brand
        '''super method - used to call the variables from inherited class'''
        super().__init__(color, features, varients, engineCondition)

    '''instance method'''
    def fullDetails(self):
        print(
            f"This {self.brand} car has {self.features} features contains in {self.varients} varients in {self.color} color")

    @staticmethod
    def getInfo():
        print("this is car class")

    @classmethod
    def getWheelsDetails(cls):
        print(f"This car has {cls.wheels} wheels")

'''hierarical Inheritance'''
class bike(specs):
    wheels = 2

    def __init__(self, brand, color, features, varients, enginecondition):
        self.brand = brand
        super().__init__(color, features, varients, enginecondition)

    '''instance method'''
    def fullDetails(self):
        print(
            f"This {self.brand} Bike has {self.features} features contains in {self.varients} varients in {self.color} color")

    @staticmethod
    def getInfo():
        print("this is Bike class")

    @classmethod
    def getWheelsDetails(cls):
        print(f"This bike has {cls.wheels} wheels")

'''polymorpism'''
def transport(vehicle):
    vehicle.getInfo()
    vehicle.fullDetails()
    vehicle.engineCondition()
    vehicle.getWheelsDetails()


# if __name__ == "__main__":
#     a = car('TATA', '(White/Black/Red)', '6Air Bags', 5, True)
#     b = bike('HERO', '(White/Black/Gray)', 'DISC brakes & 6 gears', 2, True)
#     transport(a)
#     print("*" * 50)
#     transport(b)


import os

# print(os.name)
# print(os.listdir("."))
# print(os.getcwd())
# print(os.chdir("path"))
# print(os.mkdir("example"))
# print(os.rmdir("example"))
#print(os.remove("write.txt"))
# print(os.path.exists("writedata.txt"))
# print(os.path.abspath("writedata.txt"))
# print(os.path.basename("writedata.txt"))
# print(os.path.basename(r"C:\Source\Python_practice_mine\New folder\writedata.txt"), "----basename")
# split_path = os.path.split(r"C:\Source\Python_practice_mine\New folder\writedata.txt")
# print(split_path)
# print(os.path.join(split_path[0], "content.csv"))
# print(os.path.isfile("writedata.txt"))
# print(os.path.isdir("example"))


'''input: [1, 2, 3, 4, 5]
   output: [123, 124, 125, 134, 135, 145, 234, 235, 245, 345]
'''

lt = [1, 2, 3, 4, 5]

import itertools

newLt = []

# for combination in itertools.combinations(lt, 4):
# print(combination)
#   newLt.append(int("".join(str(i) for i in combination)))

# print(newLt) #[123, 124, 125, 134, 135, 145, 234, 235, 245, 345]

#or

n = len(lt)
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            newLt.append(int(f"{lt[i]}{lt[j]}{lt[k]}"))

# print(newLt) #[123, 124, 125, 134, 135, 145, 234, 235, 245, 345]


'''
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
'''

def stringManipulation1(st):
    if len(st) <2:
        return "Empty String"
    else:
        return f"{st[:2]+st[-2:]}"

st = 'w'
# print(stringManipulation1(st))

'''i/p: 'abc', 'xyz'
   o/p: 'xyc abz'
'''

def stringManipulation2(st1, st2):
    newst1 = st2[:2] + st1[2:]
    newst2 = st1[:2] + st2[2:]
    # , st2[-2:] = st2[-2:], st1[:2]
    print(newst1, newst2)
    newjoinedst = newst1 + " " + newst2
    print(newjoinedst) #'xyc abz'

st1, st2 = 'abc', 'xyz'
# stringManipulation2(st1,st2)

'''
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''

def stringManipulation3(st1):
    if len(st1)>=3:
        if not st1.endswith('ing'):
            return st1+'ing'
        else:
            return st1+"ly"
    else:
        return "string should be more than 3 char"
st1 = 'string'
# print(stringManipulation3(st1))


'''removing the Kth idex from a string in list'''

def removeNindex(arr, nindex):
    result_arr = []
    for word in arr:
        result_arr.append(word[:3]+word[4:])

    print(result_arr)

    '''k=3
# # lt = []
# # for i in arr:
# #     s=""
# #     for j in range(len(i)):
# #         if k != j:
# #             s+=i[j]
# #             # print(s)
# #     lt.append(s)'''

arr = ['ankitha', 'sindhu', 'sanjeev', 'sadik']
# removeNindex(arr=arr, nindex=3)


'''Email validation'''
import re
def mail_validation(mail_id):
    # pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+.com+$'
    result = re.match(pattern, mail_id)
    if result:
        print('valid mail-Id')
    else:
        print('In-Valid mail-Id')

# mail_validation('d.sanju1998_@hot.com')


import time
# print(time.ctime(time.time()))

# ctime=time.localtime()
# time_past = time.strftime(("%H%M"),ctime)
# # print(time_past)
# for i in range(1,10):
#     # print(i)
#     time.sleep(2)
#
# curr_time = time.strftime("%H%M", time.localtime())
# print(curr_time)
# print(int(curr_time)-int(time_past))

'''Ip validation'''
def ip_validation(ip_address):
    ip_split = ip_address.split(".")
    if len(ip_split)!=4:
        return False
    for n in ip_split:
        # print(type(n))
        if not n.isnumeric() or not (0<=int(n)<=255):
            return False
    return True

# if ip_validation('10.223.217.2555'):
#     print('valid')
# else:
#     print('in-valid')


import ast
def file(filepath):
    with open(filepath, 'r') as data:
        result = eval(data.read())
        print(type(result))
        # d = result['company']['Engineering']['Alice']
        # print(d, type(d))


# file(filepath=r"C:\Users\Admin\OneDrive\Desktop\example.toml")