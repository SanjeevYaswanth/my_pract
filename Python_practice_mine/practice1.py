"""Pattern"""


def starAngle(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print('* ', end=" ")

        print("\r")


starAngle(5)


def starTriangle(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print('* ', end=" ")
        print("\r")


starTriangle(5)

'''sum of digits'''


def sum(n):
    sum = 0
    for i in str(n):
        sum = sum + int(i)
    print(sum)


sum(1233333333)

'''palindrome for string and number'''


def palindrome(string):
    rev_str = ""
    for i in str(string):
        rev_str = i + rev_str

    print(rev_str)
    if rev_str == str(string):
        print(f"{string} is palindrome")
    else:
        print(f"{string} is not a palindrome")


palindrome("madam")
palindrome(12321)

'''Leap year'''


def leap(n):
    if n % 4 == 0:
        if n % 400 == 0:
            if n % 100 == 0:
                print(f"{n} is a leap year")
            else:
                print(f"{n} is not a leap year")
        else:
            print(f"{n} is a leap year")
    else:
        print(f"{n} is not a leap year")


leap(2000)


def fun():
    for x in range(22, 23, 24):
        print(x)


fun()

'''Odd numbers from list'''
l = [45, 65, 12, 32, 99, 87]
odd_list = []
for i in l:
    if i % 2 == 0:
        continue
    else:
        odd_list.append(i)

print(odd_list)

'''Odd numbers and multiple by 5'''
l2 = [10, 15, 20, 25, 30]
l1=[]
for i in l2:
    if i%2!=0 and i%5==0:
        l1.append(i)
print(l1)
'''or'''
l2 = [10, 15, 20, 25, 30]
for i in l2:
    if i%2!=0 and i%5==0:
        continue
    else:
        l2.remove(i)
print(l2)


'''seperate even and odd list'''
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenlist = []
oddList = []
for i in l3:
    if i % 2 == 0:
        evenlist.append(i)
    elif i % 2 == 1:
        oddList.append(i)

print(f"evenlist: {evenlist}")
print(f"oddlist: {oddList}")

# even = [i for i in l3 if i%2==0]
# odd = [j for j in l3 if j%2!=0]
# print(even)
# print(odd)

'''Combine List using extend and +'''
combined_list = []

combined_list.extend(evenlist)
combined_list.extend(oddList)
print(combined_list)

combined_list2 = []
combined_list2 = evenlist + oddList
print(combined_list2)

'''copy the list in reverse order'''

l1 = [5, 7, 9, 100, 75, 95]
new_l1 = []
new_l1 = l1.copy()
new_l1.reverse()
print(new_l1)

'''Print highest occurence element in list'''

myList = [5, 1, 'sanju', 'manoj', 1, 5, 'sanju', 'sanju']
result = []

for i in myList:
    if i not in result:
        result.append(i)

highest_occ_ele = 0
highest_times = 0

for i in result:
    count = myList.count(i)
    if count > highest_times:
        highest_times = count
        highest_occ_ele = i

print(f"highest occurence element is {highest_occ_ele}, i.e. {highest_times} times")

print(float('-inf'))

'''product of all elements in list'''
mylist = [1, 2, 3, 4, 5]
product = 1
for i in mylist:
    product = product * i

print(product)

'''Print all prime number in the list'''
mylist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in mylist:
    factors = 0
    for j in range(2, i + 1):
        if i % j == 0:
            factors += 1
    if factors == 1:
        print(i)

'''swap first and last element in a list'''

List = [5, 7, "sanju", 55.55, 100]

List[0], List[-1] = List[-1], List[0]
print(List)

'''Guess the output'''
a, b = 'pq'
b, c = 'rs'

print(a, b, c)

'''range'''

mylist = [i for i in range(0, 21)]
print(mylist)

'''create dict using 2 lists'''

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]
dic = {}

for i in range(0, len(l1)):
    dic[l1[i]] = l2[i]

### or

# for i, j in zip(l1,l2):
#     dic[i] = j

print(dic)

'''count the character and create dict'''


def countChar(string):
    result_dict = {}
    for ch in string:
        if ch in result_dict:
            result_dict[ch] += 1
        else:
            result_dict[ch] = 1

    print(result_dict)


countChar("hello world")

'''print common elements from the 2 lists'''

lst1 = [5, 3, 6, 1, 7, 'sanju', 1]
lst2 = [2, 3, 5, 7, 'manoj', 0]

set1 = set(lst1)
set2 = set(lst2)

print(set1.intersection(set2))
# or
print(set1 & set2)

# new_set: set = {}
# for i in int(set1):
#     if i in set2:
#         continue
#     else:
#         new_set.update(i)
# print(new_set)


'''OOPS'''

'''Abstraction'''

from abc import ABC, abstractmethod

class payment(ABC):

    @abstractmethod
    def paymentViacards(self, amount):
        pass


class debitCard(payment):
    def paymentViacards(self, amount):
        print(f"Payment via debit card of amount:{amount}")


class creditCard(payment):
    def paymentViacards(self, amount):
        print(f"payment via credit card of amount: {amount}")


a = creditCard()
a.paymentViacards(2000)

b = debitCard()
b.paymentViacards(1000)

# c = payment()
# c.paymentViacards(2000)

'''Encapsulation'''


class AccessModifiers:
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    def getAllVariableValues(self):
        print(f"public: {self.var1}, "
              f"protected: {self._var2}, "
              f"private: {self.__var3}")

    def setPrivateVariable(self, newvalue):
        self.__var3 = newvalue


a = AccessModifiers(1, 2, 3)
a.getAllVariableValues()
print(a.var1)
print(a._var2)
print(a._AccessModifiers__var3)

'''change the private varibale as below or add a new method to set the private variable - setPrivateVariable'''
a._AccessModifiers__var3 = 55
print(a._AccessModifiers__var3)

a.setPrivateVariable(65)
a.getAllVariableValues()

'''Inheritance'''

'''single'''


class parent:
    def fun(self):
        print('this is parent class')


class child(parent):
    def fun1(self):
        print('this is child class')


a = child()
a.fun()
a.fun1()

'''multiple'''


class father:
    def fun1(self):
        print('this is father class')


class mother:
    def fun2(self):
        print('this is mother class')


class child(father, mother):
    def fun3(self):
        print('this is child class')


b = child()
b.fun1()
b.fun2()
b.fun3()

'''multi level'''


class grandParent:
    def fun1(self):
        print('this is grand parent class')


class parent(grandParent):
    def fun2(self):
        print('this is parent class')


class child(parent):
    def fun3(self):
        print('this is child class')


c = child()
c.fun1()
c.fun2()
c.fun3()

'''hybrid'''


class A:
    def fun1(self):
        print("A class")


class B(A):
    def fun2(self):
        print("B class")


class C(A):
    def fun3(self):
        print("C class")


class D(C, B):
    def fun4(self):
        print("D class")


d = D()
d.fun1()
d.fun2()
d.fun3()
d.fun4()

'''Hierarical'''


class Parent:
    def fun1(self):
        print('parent class')


class child1(Parent):
    def fun2(self):
        print('child1 class')


class child2(Parent):
    def fun3(self):
        print('child2 class')


e = child1()
f = child2()
e.fun1()
e.fun2()
f.fun3()

'''Ploymorphism'''

'''Duck Typing'''


def emptyLand(obj):
    obj.land()


class hotel:
    def land(self):
        print('this is for hotel land')


class office:
    def land(self):
        print('this is for office land')


a = office()
emptyLand(a)
b = hotel()
emptyLand(b)

'''operator overloading'''


class calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        x = self.a + other.a
        y = self.b + other.b
        return x, y


s1 = calculation(2, 3)
s2 = calculation(4, 5)
print(s1 + s2)

'''Method Overriding'''


class Animal:
    def sound(self):
        print('Animal sound')


class cat(Animal):
    def sound(self):
        print('Meow meow')


class dog(Animal):
    def sound(self):
        print('Bow Bow')


a = dog()
a.sound()

'''Decorator'''


def upper_dec(fun):
    def wrapper():
        string = fun()
        return string.upper()

    return wrapper


@upper_dec
def string():
    return "hello world"


print(string())

'''Genarator'''


def square(n):
    for i in range(n):
        yield i * i


sq = square(5)
print(sq.__next__())
print(sq.__next__())
print(sq.__next__())
print(sq.__next__())
print(sq.__next__())

# or

for i in sq:
    print(i)


'''Counts the occurrences of each character in a string and 
    returns a frequency-encoded string.'''

def count(string):
    occ_count = {}
    for ch in string:
        if ch in occ_count:
            occ_count[ch] += 1

        else:
            occ_count[ch] = 1

    print(occ_count)
    comb_str = ''
    for k, v in occ_count.items():
        comb_str = comb_str +f"{k}{v}"
    print(comb_str)

count('aabbccdd')

d1 = {1: 200, 2: 300, 3: 500}
d2 = {1: 500, 2: 700, 4: 600}

for key in d2:
    if key in d1:
        # If the key exists in d1, sum the values
        d1[key] += d2[key]
    else:
        # If the key does not exist in d1, add it
        d1[key] = d2[key]
print(d1) # {1: 500, 2: 700, 3: 500, 4: 600}