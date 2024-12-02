'''
Sort an Array or List
# # decending order - >=
# # ascending order - <=
'''
Array = [1, 7, 4, 1, 10, 9, -2]
for i in range(len(Array)):
    for j in range(i):
        if Array[i] < Array[j]:
            Array[i], Array[j] = Array[j], Array[i]

print(Array)

'''Triplet validation means sum of 3 digits = result value'''


def triplet(result):
    for i in range(len(Array)):
        for j in range(i + 1, len(Array)):
            for k in range(j + 1, len(Array)):
                if Array[i] + Array[j] + Array[k] == result:
                        return Array[i], Array[j], Array[k]


print(triplet(18))

'''Remove duplicate from list'''


def duplicateFromList():
    new_list = []
    for i in Array:
        if i in new_list:
            pass
        else:
            new_list.append(i)

    print(new_list)


duplicateFromList()

'''largest element in Array'''


def largestelement(Array):
    max = Array[0]
    for i in range(len(Array)):
        if Array[i] > max:
            max = Array[i]
    return max


'''Second Largest Element in a Array'''


def SecondLargest(Array):
    n = len(Array)
    for i in range(0, n):
        for j in range(i + 1, n):
            if (Array[i] > Array[j]):
                # temp = Array[i]
                # Array[i] = Array[j]
                # Array[j] = temp
                Array[i], Array[j] = Array[j], Array[i]
    print(Array[-2])


Array = [7, 3, 2, 4, 5, 6, 9]
print(largestelement(Array))
SecondLargest(Array)

'''Count a Vowels in An string'''


def count_vowels(string):
    count = 0
    for i in string:
        print(i, "_________")
        if i in "AaEeIiOoUu":
            count += 1
    print(count)


count_vowels("interview test")

"""Counts the occurrences of each character in a string and 
    returns a frequency-encoded string."""


def charCount(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print(char_count)
    countString = ""
    for k, v in char_count.items():
        countString = countString + f"{v}{k}"
    print(countString)


# charCount('aabbbccddd') #2a3b2c3d

'''replace key with values and vice versa in dict'''
d = {'a': 1, 'b': 2}
d_new = {}
for k, v in d.items():
    # k, v = v, k
    d_new[v] = k

print(d_new)

'''
    reverse the string without in-built method
    And check palindrome 
'''


def rev_str(string):
    rev_str = ""
    for i in str(string):
        rev_str = i + rev_str

    print(rev_str)
    if rev_str == str(string):
        print(f"{string} is palindrome")
    else:
        print(f"{string} is not a palindrome")


rev_str("madam")
rev_str(1234321)

'''Fibonacci'''


def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


fib(10)

'''List to Dict'''

listData = [4, 4, 5, 6]
for index, value in enumerate(listData):
    print(index, ":", value, "aaaaaaaaaaaaaaaaa")

'''Prime Number - (2, n) '''


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime")
            break

    else:
        print(f"{n} is a prime")


prime(50)

'''Factorial'''


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    print(fact)


factorial(5)

'''decorator'''


def decoratorFunc(func):
    def wrapper():
        result = func()
        return result.lower()

    return wrapper


@decoratorFunc
def run():
    return 'SANJU'


print(run())


'''Genarator -- Yield'''

def square(n):
    for i in range(1, n + 1):
        yield i * i


a = square(5)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

""" we can use __next__() or for loop to print output, 
    either of it works if we use both"""

for b in a:
    print(b)

'''
    Reverse the words in a string
    i.e. "Yash Sanju" -->  "Sanju Yash"
'''


def rev(string):
    stringSplit = string.split(" ")
    print(stringSplit)
    new_list = []
    for i in stringSplit:
        new_list.insert(0, i)

    print(new_list)
    return " ".join(new_list)


print(rev("Yash Sanju"))

'''Patterns'''


def starLadder(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")


starLadder(5)


def starTriangle(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k -= 1
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")


starTriangle(5)

'''Leap Year'''


def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


leapYear(2024)

'''Print odd nums using list comprehension'''
Even_result = [i for i in range(0, 100) if i % 2 == 0]  # even
Odd_result = [i for i in range(0, 100) if i % 2 != 0]  # odd

print(Even_result)
print(Odd_result)

'''dict comrehension'''

keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]

print({k: v for k, v in zip(keys, values)})

print({x: x ** 2 for x in range(1, 5)})


'''sum of digits'''


def sum(digits):
    result = 1
    for i in str(digits):
        result += int(i)

    print(result)


sum(12345)


""""""
string = "abcdieabdfitabcintrgabcab"

count = 0

splitString = string.split("i")
print(splitString)
for i in splitString:
    if 'abc' in i:
        count += 1

print(count)

"""Lambda
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression."""

print((lambda x: x * 2)(3))

# lambda function with *args

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]

val = lambda *args: sum(args)

print(val(*l1, *l2))

"""'Map' is used to apply a function on every item in an array/list and 
returns the new array/output. 
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x % 2 == 0, a)))

"""'Filter' is used to create a new array from an existing one, 
containing only those items that satisfy a condition specified in a function."""

print(list(filter(lambda x: x % 2 == 0, a)))

'''Adds List Element as value of List using Append.'''
List = ['Mathematics', 'chemistry', 1997, 2000]
List.append([20544, 134555])
print(List)

'''Adds List Element as value of List using Extend.'''
List = ['Mathematics', 'chemistry', 1997, 2000]
List.extend([20544, 134555])
print(List)

List = ['Mathematics', 'chemistry', 1997, 2000]
# Insert at index 2 value 10087
List.insert(2, 10087)
print(List)

# Conversion table of remainders to
# hexadecimal equivalent
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}


# function which converts decimal value
# to hexadecimal value
def decimalToHexadecimal(decimal):
    hexadecimal = ''
    while (decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    return hexadecimal


decimal_number = 69
print("The hexadecimal form of", decimal_number,
      "is", decimalToHexadecimal(decimal_number))

# x=5
print(eval("x**2+3", {'x': 5}))

print("Apples", "Orange", "Mango", sep=", ", end=" are fruits!\n")


'''Identity vs Equality operators'''

list1 = []
list2 = []
list3 = list1

# case 1
if (list1 == list2):
    print("True")
else:
    print("False")

# case 2
if (list1 is list2):
    print("True")
else:
    print("False")

# case 3
if (list1 is list3):
    print("True")
else:
    print("False")

# case 4
list3 = list3 + list2

if (list1 is list3):
    print("True")
else:
    print("False")

'''
The output of the first case, if the condition is “True” as both list1 and list2 are empty lists
The output of the second case, if the condition shows “False” because two empty lists are at different memory locations. Hence list1 and list2 refer to different objects. We can check it with id() function in python which returns the “identity” of an object.
The output of the third case, if the condition is “True” as both list1 and list3 are pointing to the same object.
The output of the fourth case, if the condition is “False” because the concatenation of two lists always produces a new list.
'''