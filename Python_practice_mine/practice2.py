# # # class accessVariables:
# # #     def __init__(self):
# # #         self.var1 = "aaaaaa"  # public
# # #         self._var2 = "bbbb"  # protected
# # #         self.__var3 = "cccc"  # private
# # #
# # #     def example(self):
# # #         print(f"public: {self.var1}, protected:"
# # #               f" {self._var2}, private: {self.__var3}")
# # #
# # #     def get_privateValue(self): #getter
# # #         return self.__var3
# # #
# # #     def set_privateValue(self, newData):  #setter
# # #         self.__var3 = newData
# # #
# # # # a=accessVariables()
# # # # a.example()
# # # # print(a.get_privateValue())
# # # # a.set_privateValue("ffffff")
# # # # a.example()
# # # # print(a.get_privateValue())
# # #
# # #
# # #
# # #
# # #
# # # # print(a.var1)
# # # # a.var1 = "dddddd"
# # # # a.example()
# # # # print(a._var2)
# # # # a._var2 = "eeeeeee"
# # # # a.example()
# # # # # a.__var3 = "ffff"
# # # # a.example()
# # # # print(a._accessVariables__var3) # able to access private variables
# # # # # print(a.__var3)
# # # # a._accessVariables__var3 = "ffffffffff"
# # # # print(a._accessVariables__var3)
# # # # a.example()
# # # # if __name__ == '__main__':
# # # #     a=accessVariables()
# # # #     a.example()
# # # #     print(a.var1, "1111",) #a._var2, "222", a.__var3)
# # # #     print(a._var2)
# # # #     print(a.__var3)
# # #
# # # # def gen(num1, num2):
# # #
# # string1 = "this is interview"
# # sample = []
# #
# # str3 = string1.split(" ")
# # print(str3)
# # for i in str3:
# #     result = i[::-1]
# #     sample.append(result)
# # print(sample)
# # print(" ".join(sample))
# # #
# # # # [12:00 PM] Mahendra (Guest)
# # # # s = "aabbbcceddbb"
# # # # #"2a3b2c1e2d2b"
# # # #
# # # # aCount = s.count("a")
# # # # bCount = s.count("b")
# # # # cCount = s.count("c")
# # # # dCount = s.count("d")
# # # # eCount = s.count("e")
# # #
# # # # print(s.split())
# # #
# # # # data = [10, 20, 30, 40, 30, 22, 30,40,30,50,30]
# # # # resultData = []
# # # # count = 0
# # # # for i in data:
# # # #     if i == 30:
# # # #         # print(i)
# # # #         count +=1
# # # #
# # # #         if count == 2 or count==3:
# # # #             continue
# # # #     resultData.append(i)
# # # #         # print(data.index(30))
# # # #         #     data.remove(30)
# # # # print(resultData)
# # # #
# # # # polymorpism examples
# # # # abstact
# # # # encapsualtion
# # # # generator
# # # # decorator
# # # # oops concepts
# # # # public private protected
# # #
# # # # polymorpism examples
# # # # poly - many  morp - forms
# # # # 1.Class & object Polymorphism in Python or Duck-Typing
# # # # def emptyLand(obj):
# # # #     obj.land()
# # # #
# # # # class office:
# # # #     def land(self):
# # # #         print("This land is for Office")
# # # #
# # # # class hotel:
# # # #     def land(self):
# # # #         print("this land is for hotel")
# # # #
# # # # off = office()
# # # # hot = hotel()
# # # #
# # # # emptyLand(off)
# # # # emptyLand(hot)
# # #
# # #
# # # # 2.  inheritance and method overriding
# # # # class Animal:
# # # #     def make_sound(self):
# # # #         print("Generic animal sound")
# # # #
# # # #
# # # # class Dog(Animal):
# # # #     def make_sound(self):  # Overridden method
# # # #         print("Boww!")
# # # #
# # # #
# # # # class Cat(Animal):
# # # #     def make_sound(self):  # Overridden method
# # # #         print("Meow!")
# # # #
# # # #
# # # # animals = [Dog(), Cat(), Animal()]
# # # # for animal in animals:
# # # #     animal.make_sound()  # Calls the appropriate version
# # # # c = Animal()
# # # # c.make_sound()
# # # # b=Dog()
# # # # b.make_sound()
# # #
# # # # 3. inbuilt polymorphic functions
# # #
# # # # len() being used for a string
# # # # print(len("geeks"))
# # # #
# # # # # len() being used for a list
# # # # print(len([10, 20, 30]))
# # # #
# # # #
# # # # # 4. operator overLoading
# # # # class marks:
# # # #     def __init__(self, a, b):
# # # #         self.a = a
# # # #         self.b = b
# # # #
# # # #     def __add__(self, other):
# # # #         a1 = self.a + other.a
# # # #         a2 = self.b + other.b
# # # #         return a1, a2
# # # #
# # # #     def __gt__(self, other):
# # # #         b1 = self.a + self.b
# # # #         b2 = other.a + other.b
# # # #         if b1 > b2:
# # # #             return True
# # # #         else:
# # # #             return False
# # # #
# # # #     def __str__(self):
# # # #         return f'{self.a}, {self.b}'
# # # #
# # # # s1 = marks(10, 20)
# # # # s2 = marks(12, 15)
# # # #
# # # # total = s1 + s2
# # # # print(total)
# # # #
# # # # greater = s1 > s2
# # # # if greater:
# # # #     print("s1 wins")
# # # # else:
# # # #     print("s2 wins")
# # # #
# # # # print(s1, s2)  # __str__
# # #
# # # #
# # # # Python doesn't support method overloading,
# # # # it will take the latest function,
# # # # if we have same function name
# # #
# # # class company:
# # #
# # #     def interview(self):
# # #         print('This is first Round')
# # #
# # #     def interview(self, round):
# # #         print(f"This is {round} round")
# # #
# # #     def interview(self, round, qualifyStatus):
# # #         print(f"This is {round} and you are {qualifyStatus}")
# # #
# # #
# # #
# # # a = company()
# # # # a.interview()
# # # # a.interview(round="Technical")
# # # a.interview(round="HR", qualifyStatus="Qualified")
# # #
# # # #abstract class & method
# # # from abc import ABC, abstractmethod
# # #
# # # class vehicle(ABC):
# # #     # def __init__(self, n):
# # #     #     self.num_of_Tyres = n
# # #     @abstractmethod
# # #     def start(self, n):
# # #         pass
# # #
# # # class bike(vehicle):
# # #     # def __init__(self, n):
# # #     #     self.num_of_tyres = n
# # #
# # #     def start(self, n):
# # #         print("starts with kick", f"and number of tyres: {n}")
# # #
# # # class scooty(vehicle):
# # #     # def __init__(self, n):
# # #     #     self.num_of_tyres = n
# # #
# # #     def start(self, n):
# # #         print("starts with self button", f"and number of tyres: {n}")
# # #
# # # a=bike()
# # # a.start(2)
# # #
# # # #Decorators
# # #
# # # def div(a,b):
# # #     print(a/b)
# # #
# # # def smart_div(func):
# # #
# # #     def inner_div(a,b):
# # #         if a<b:
# # #             a, b = b, a
# # #         return func(a,b)
# # #     return inner_div
# # #
# # # div1 = smart_div(div)
# # # div1(2,4)
# # #
# # #
# # # #Generators
# # #
# # # def gen():
# # #     yield 1
# # #     yield 2
# # #     yield 3
# # #     yield 4
# # #
# # # values = gen()
# # # # print(values.__next__())
# # # # print(values.__next__())
# # # # print(values.__next__())
# # # # print(values.__next__())
# # #
# # # # for i in values:
# # #     # print(i)
# # #
# # # #Generators
# # # def square(n):
# # #     for i in range(n):
# # #         sq = i*i
# # #         yield sq
# # #
# # # s = square(10)
# # # # print(s.__next__())
# # # # print(s.__next__())
# # # print("-----------------------------")
# # # for i in s:
# # #     print(i)
# #
# # # def fib(n):
# # #     a, b = 0, 1
# # #     while a < n:  # for i in range(n):
# # #         yield a
# # #         a, b = b, a+b
# # #
# # # a= fib(5)
# # # # print(a.__next__())
# # # # print(a.__next__())
# # # print("-----------------------------")
# # #
# # # for i in a:
# # #     print(i)
# # #
# # # #iterator
# # #
# # # l1 = [2,45,1,7,3,0]
# # #
# # # a= iter(l1)
# # #
# # # print(a.__next__())
# # # print(a.__next__())
# # # print("-----------------------------")
# # #
# # # # class iterator:
# # # #     def __init__(self):
# # # #         self.num = 1
# # # #
# # # #     def __iter__(self):
# # # #         return self
# # # #
# # # #     def __next__(self):
# # # #         if self.num <=10:
# # # #             val = self.num
# # # #             self.num+=1
# # # #             return val
# # # #         else:
# # # #             raise StopIteration
# # #
# # # # z= iterator()
# # # # print(z.__next__())
# # # # print(z.__next__())
# # # # print(z.__next__())
# # # # for i in z:
# # # #     print(i)
# # #
# # #
# # # #mutli level inheritance
# # #
# # # class a:
# # #     def x(self):
# # #         print("x")
# # # class b(a):
# # #     def y(self):
# # #         print("y")
# # # class c(b):
# # #     def z(self):
# # #         print("z")
# # #
# # # f=c()
# # # f.z()
# # # f.y()
# # # f.x()
# # #
# # # #decorator
# # #
# # # def my_logging_decorator(func):
# # #     def wrapper(*args, **kwargs):
# # #         print(f"Calling function {func.__name__} with arguments: {args}, {kwargs}")
# # #         result = func(*args, **kwargs)
# # #         print(f"Function {func.__name__} returned: {result}")
# # #         return result
# # #     return wrapper
# # #
# # # @my_logging_decorator
# # # def add(x, y, z):
# # #     return x + y + z
# # #
# # # add(5, 3, 2)  # Output:
# # # # Calling function add with arguments: (5, 3), {}
# # # # Function add returned: 8
# # #
# # # def hello_decorator(func):
# # #     def inner1(*args, **kwargs):
# # #         print("before Execution")
# # #
# # #         # getting the returned value
# # #         returned_value = func(*args, **kwargs)
# # #         print("after Execution of", func.__name__)
# # #
# # #         # returning the value to the original frame
# # #         return returned_value
# # #     return inner1
# # #
# # # # adding decorator to the function
# # # @hello_decorator
# # # def sum_two_numbers(a, b):
# # #     print("Inside the function")
# # #     return a + b
# # #
# # # @hello_decorator
# # # def div(a,b):
# # #     if a<b:
# # #         a,b = b,a
# # #     return a/b
# # #
# # # a, b = 1, 2
# # #
# # # # getting the value through return of the function
# # # print("Sum =", sum_two_numbers(a, b))
# # # print(f"division = {div(2,4)}")
# # #
# # #
# # # '''The key difference between `return` and `yield` in Python lies in how they control the execution flow and data generation within a function:
# # #
# # # **Return:**
# # #
# # # - Exits the function immediately.
# # # - Returns a single value to the caller.
# # # - Can only be used once per function invocation.
# # # - Used typically when a function completes a calculation and delivers a final result.
# # #
# # # **Yield:**
# # #
# # # - Temporarily pauses the function's execution.
# # # - Returns a value to the caller but retains the function's state.
# # # - Can be used multiple times within a function, generating a sequence of values.
# # # - Used when you want to produce a stream of values on demand, often for large datasets or iterators.
# # #
# # # Here's a table summarizing the key differences:
# # #
# # # | Feature             | `return`                                           | `yield`                                          |
# # # |--------------------|-------------------------------------------------------|----------------------------------------------------|
# # # | Execution          | Ends function immediately                          | Pauses execution temporarily                       |
# # # | Returned value     | Single value to the caller                           | Single value to the caller, retains function state |
# # # | Usages per call   | One usage per function call                          | Multiple usages per function call                   |
# # # | When to use        | Returning final result, exiting function         | Generating sequences, memory efficiency             |
# # #
# # # **Example:**
# # #
# # # ```python
# # # def calculate_squares_return(n):
# # #     squares = []
# # #     for i in range(n):
# # #         squares.append(i * i)
# # #     return squares
# # #
# # # def calculate_squares_yield(n):
# # #     for i in range(n):
# # #         yield i * i
# # #
# # # # Using return
# # # squares_list = calculate_squares_return(5)
# # # print(squares_list)  # Output: [0, 1, 4, 9, 16]
# # #
# # # # Using yield
# # # for square in calculate_squares_yield(5):
# # #     print(square)  # Output: 0, 1, 4, 9, 16
# # # ```
# # #
# # # **In essence:**
# # #
# # # - Use `return` when you're done with the function and want to send a single value back.
# # # - Use `yield` when you want to create a sequence of values on demand, making your function an iterator.'''
# # #
# # # x="12.0"
# # # print(int(x)*2)
# #
# # ##########
# #
# # # # calculator using OOPs
# # #
# # # class calculator:
# # #
# # #     def sum(self, a, b):
# # #         return a+b
# # #
# # #     def sub(self, a, b):
# # #         return a-b
# # #
# # #     def mul(self, a, b):
# # #         return a*b
# # #
# # #     def div(self, a, b):
# # #         return a/b
# # #
# # #
# # # class Maths(calculator):
# # #
# # #     def maths_operation(self, operation, var1, var2):
# # #         if operation == "+":
# # #             return self.sum(var1, var2)
# # #         elif operation == "-":
# # #             return self.sub(var1, var2)
# # #         elif operation == "*":
# # #             return self.mul(var1, var2)
# # #         elif operation == "/":
# # #             return self.div(var1, var2)
# # #
# # # result = Maths().maths_operation("+", 5, 5)
# # # print(result)
# #
# # #########################################################################
# #
# # # # Counting the Number of Occurances of a Character in a String
# # #
# # # string = "Sanjeev Yaswanth"
# # #
# # # char = "y"
# # # count = 0
# # #
# # # # for letter in string:
# # # #     if char == letter:
# # # #         count += 1
# # # # print(count)
# # #
# # # #########################################################################
# # #
# # # vowels = ['a', 'e', 'i', 'o', 'u']
# # #
# # # # vowels check
# # # for i in string:
# # #     if i in vowels:
# # #         count += 1
# # # print(count)
# # #
# # # consonants check
# # # for i in string.replace(" ", ""):
# # #     if i not in vowels:
# # #         count += 1
# # # print(count)
# #
# # #########################################################################
# #
# # # #reading JSON file
# # #
# # # import json
# # # path = r"C:\Users\duggisax\Downloads\BIOS_LNL_M_Internal_2470.83\LNL_BIOS_2470_83.json"
# # # with open(path, "r") as data:
# # #     result = json.load(data)
# # #     print(result.get('Name'))
# #
# # #########################################################################
# #
# # # List sorting without sort function
# #
# # l = [1, 10, 8, 6]
# #
# # # sort the list min to max without inbuilt sort
# #
# # for i in range(len(l)):
# #     for j in range(i+1, len(l)):
# #         if l[i] >= l[j]:
# #             l[i], l[j] = l[j], l[i]
# #
# # print(l)
# #
# # #########################################################################
# # #
# # # # print the max number from list without Max inbuilt function
# # #
# # # print(l[-1])
# #
# # #########################################################################
# # #
# # # #sort the list min to max with inbuilt sort
# # #
# # # l.sort()
# # # print(l)
# #
# # #########################################################################
# # #
# # # #sort the list and reverse the list max to min
# # # l.sort(reverse=True)
# # # print(l)
# #
# # #########################################################################
# # #
# sample_string = "this is an interview"
#
# sample = sample_string.replace(" ", "")
# count = 0
#
# # # 1st non-repeated character
# for i in range(len(sample)):
#     if sample[i] not in sample[i + 1:] and sample[i] not in sample[:i]:
#         print(sample[i])
#         break
#
# # # 2nd non-repeated character
# for i in range(len(sample)):
#     if sample[i] not in sample[i + 1:] and sample[i] not in sample[:i]:
#         count += 1
#
#     if count == 2:
#         print(sample[i])
#         break
#
# # # 3rd non-repeated character
# for i in range(len(sample)):
#     if sample[i] not in sample[i + 1:] and sample[i] not in sample[:i]:
#         count += 1
#     if count == 3:
#         print(sample[i])
#         break
#
#
# #
# # #########################################################################
# #
# # # def num(n):
# # #     for i in range(0, n):
# # #         for j in range(0, i+1):
# # #             print("* ", end="")
# # #         print("\r")
# # #
# # # num(5)
# # #
# # # #########################################################################
# # #
# # # # FIB
# # #
# # # def fib(n):
# # #     n1, n2 = 0, 1
# # #     if n == 0:
# # #         print(f"fib series of {n} is {n1}")
# # #     elif n<0:
# # #         print("fib series is not possible")
# # #     else:
# # #         for i in range(0, n):
# # #             print(n1)
# # #             # sum = n1+n2
# # #             # n1 = n2
# # #             # n2 = sum
# # #             n1, n2 = n2, n1+n2
# # #
# # # fib(5)
# #
# # #########################################################################
# #
# # # #Generator - yield
# # #
# # # def square(n):
# # #     for i in range(1,n+1):
# # #         x = i*i
# # #         yield x
# # #
# # # a=square(5)
# # # # print(a.__next__())
# # # # print(a.__next__())
# # # # print(a.__next__())
# # # # print(a.__next__())
# # # # print(a.__next__())
# # #
# # # for i in a:
# # #     print(i)
# #
# # # #########################################################################
# # #
# # # #Factorial
# # #
# def fact(n):
#     factorial = 1
#     for i in range(1, n+1):
#         factorial *= i
#     print(factorial)
#
# fact(5)
# # #
# # # #########################################################################
# # #
# # # #minimum number of 3
# # #
# # # def min(n1, n2, n3):
# # #     if n2>n1<n3:
# # #         return n1
# # #     elif n1>n2<n3:
# # #         return n2
# # #     elif n2>n3<n1:
# # #         return n3
# # #
# # # #or
# # #
# # #     # if n1<n2 and n1< n3:
# # #     #     return n1
# # #     # elif n2<n3 and n2< n1:
# # #     #     return n2
# # #     # else:
# # #     #     return n3
# # #
# # # print(min(1, 3, 0))
# # #
# # # #########################################################################
# # #
# # # def max(n1, n2, n3):
# # #     if n3<n1>n2:
# # #         return n1
# # #     elif n1<n2>n3:
# # #         return n2
# # #     elif n2<n3>n1:
# # #         return n3
# # #
# # # print(max(10,7 , 5))
# #
# # # #########################################################################
# #
# # # Anagram
# #
# # str1 = 'silent'
# # str2 = 'listen'
# # l1 = []
# # l2 = []
# #
# # # splitting the string
# # for i in str1:
# #     l1.append(i)
# # for j in str2:
# #     l2.append(j)
# # # print(l1, l2)
# #
# # # check anagram
# # # print(sorted(l1))
# # # if sorted(l1) == sorted(l2):
# # #     print("True")
# # # else:
# # #     print("False")
# #
# # # #########################################################################
# #
# # # #palindrome
# # #
# # # def isPalindrome(num):
# # #     original_Num = num
# # #     reverse_Num = 0
# # #
# # #     while num>0:
# # #         digit = num%10 # Modulus(%) - # Divides and returns the value of the remainder
# # #         reverse_Num = reverse_Num * 10 + digit
# # #         num = num // 10  # Floor Division(//) - Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
# # #
# # #     if reverse_Num == original_Num:
# # #         print(f'{original_Num} is palindrome')
# # #     else:
# # #         print(f'{original_Num} is not palindrome')
# # # isPalindrome(123421)
# #
# # # #########################################################################
# #
# # # `prime number
# # #
# # # def prime(num):
# # #     flag = False
# # #     if num > 1:
# # #         for i in range(2, num):
# # #             # print(i)
# # #             if num % i == 0:
# # #                 print(num)
# # #                 flag = True
# # #                 break
# # #     if flag:
# # #         print(f"{num} is not prime")
# # #     else:
# # #         print(f"{num} is prime")
# # #
# # # prime(20)
# #
# # # #########################################################################
# #
# # l1 = [10, 5, 7]
# # l2 = [1, 2, 4]
# # # l1.append(l2)  # [10, 5, 7, [1, 2, 4]]
# # # l1.extend(l2) # [10, 5, 7, 1, 2, 4]
# # # l1.insert(4,3) # [10, 5, 7, 3]
# # # print(l1)
# #
# # # #########################################################################
# #
# # # @lamda _:  _()
# # # def _():
# # #     print('_')
# #
# # n = 10000000000000
# # # print(f'{n:,}')
# #
# # sd = {1, 3} ^ {3, 4, 1}
# # print(sd)
# #
# # # #########################################################################
# #
# # l = [1, 2, 3, 5, 7, 8, 9]
# #
# # # we can multiple the list
# # print(l * 2)  # [1, 2, 3, 5, 7, 8, 9, 1, 2, 3, 5, 7, 8, 9]
# #
# #
# # # missing number from a list
# # # for i in range(1,len(l)+1):
# # #     if i not in l:
# # #         print(i)
# #
# # # sum of which 2 numbers is a given result
# # # n=10
# # # for i in range(1, len(l)):
# # #     for j in range(i+1, len(l)):
# # #         if (l[i] + l[j]) == n:
# # #             print(l[i], l[j])
# #
# # # #########################################################################
# #
# # def main():
# #     names = []
# #     # YOUR CODE GOES HERE
# #     names.append('Robin')
# #     names.append('Aman')
# #     names.append('Rahul')
# #     print(names)
# #     return 0
# #
# #
# # if __name__ == '__main__':
# #     main()
# #
# #
# # # #########################################################################
# #
# # def main():
# #     tuple1 = tuple(("one", "two", "three"))
# #     tuple2 = tuple(("1", "2", "3"))
# #
# #     # change value at index 0 of both tuple to string "number"
# #     # Your code goes here
# #
# #     print(tuple1)
# #     print(tuple2)
# #
# #     return 0
# #
# #
# # if __name__ == '__main__':
# #     main()
# #
# #
# # # #########################################################################
# #
# # def main():
# #     # Assign values to the following variable as described above
# #     # Don't change the variable name
# #     my_string1 = None
# #     my_string2 = None
# #     my_int = None
# #     my_float = None
# #
# #     # Don't change the below code
# #     print(f"String1: {my_string1}")
# #     print("String2: %s" % my_string2)
# #     print("Integer: %d" % my_int)
# #     print("Float: %f" % my_float)
# #     return 0
# #
# #
# # # if __name__ == '__main__':
# # #     main().my_string1 = "InterviewBit"
# # #     main().my_string1 = "Don't change the variable name"
# # #     main().my_int = 11
# # #     main().my_float = 20.0
# # #     main()
# # # #########################################################################
# #
# # import itertools
# # import operator
# #
# #
# # def main():
# #     arr1 = [2, 1, 3, 4, 1]
# #     arr2 = [1, 2, 4]
# #     arr3 = [10, 3, 4, 3, 5, 6, 32, 11]
# #
# #     # make a new arr4 which include all the elements in order first of arr1 then arr2 and then arr3
# #     # Write your code here
# #     arr4 = []
# #     arr4.extend(arr1)
# #     arr4.extend(arr2)
# #     arr4.extend(arr3)  # [2, 1, 3, 4, 1, 1, 2, 4, 10, 3, 4, 3, 5, 6, 32, 11]
# #     # or
# #     arr4 = arr1 + arr2 + arr3  # [2, 1, 3, 4, 1, 1, 2, 4, 10, 3, 4, 3, 5, 6, 32, 11]
# #     print(arr4)
# #
# #     # using accumulate(), store the successive muliplication of elements of arr4 in a new list arr5
# #     arr5 = itertools.accumulate(arr4, operator.add)
# #     #
# #     print(arr5)
# #     for i in arr5:
# #         print(i)
# #
# #     return 0
# #
# #
# # if __name__ == '__main__':
# #     main()
# # # #########################################################################
# #
# import time
#
# print(time.strftime("%H:%M:%S"), "-----") # 19:11:56
# print(time.strftime("%I:%M:%S"), "-----") # 07:11:56

# # # #########################################################################
# #
# # main_dict = {}
# #
# #
# # def insert_item(item):
# #     if item in main_dict:
# #         main_dict[item] += 1
# #     else:
# #         main_dict[item] = 1
# #
# #
# # # Driver code
# # insert_item('Key1')
# # insert_item('Key2')
# # insert_item('Key2')
# # insert_item('Key3')
# # insert_item('Key1')
# #
# # print(main_dict)  # {'Key1': 2, 'Key2': 2, 'Key3': 1}
# # print(len(main_dict))  # 3
# #
# #
# # # #########################################################################
# #
# # class X:
# #     def __init__(self):
# #         self.__num1 = 5
# #         self.num2 = 2
# #
# #     def display_values(self):
# #         print(self.__num1, self.num2)
# #
# #
# # class Y(X):
# #     def __init__(self):
# #         super().__init__()
# #         self.__num1 = 1
# #         self.num2 = 6
# #
# #
# # obj = Y()
# # obj.display_values()  ## 5 6
# #
# # # #########################################################################
# # print(type(5 / 2))  # <class 'float'>
# # print(type(5 // 2))  # <class 'int'>
# # # The 1st expression performs standard division so the result is stored as a float type.
# # # The 2nd expression performs integer division so the result is stored as int type.
# #
# # # #########################################################################
# #
# # numbers = (4, 7, 19, 2, 89, 45, 72, 22)
# # sorted_numbers = sorted(numbers)
# # print(type(sorted_numbers))  # <class 'list'>
# #
# # # #########################################################################
# #
# #
# # numbers = (4, 7, 19, 2, 89, 45, 72, 22)
# # sorted_numbers = sorted(numbers)
# # even = lambda a: a % 2 == 0
# # print(even, "11111")
# # even_numbers = filter(even, sorted_numbers)
# # for i in even_numbers:
# #     print(i)
# # '''o/p: 2
# # 4
# # 22
# # 72'''
# # print(type(even_numbers))  # <class 'filter'>
# #
# # # #########################################################################
# #
# # # convert even position elements to upper case
# #
# # word = "Python Programming"
# # n = len(word)  # 18 including space
# # word1 = word.upper()
# # word2 = word.lower()
# # converted_word = ""
# # for i in range(n):
# #     if i % 2 == 0:
# #         converted_word += word2[i]
# #     else:
# #         converted_word += word1[i]
# # print(converted_word)  # pYtHoN PrOgRaMmInG
# #
# # # #########################################################################
# #
# # square = lambda x: x ** 2
# # a = []
# # for i in range(5):
# #     a.append(square(i))
# #
# # print(a)  # [0, 1, 4, 9, 16]
# #
# # # #########################################################################
# #
# # # def tester(*argv):
# # #    for arg in argv:
# # #        print(arg, end = ' ')
# # # tester('Sunday', 'Monday', 'Tuesday', 'Wednesday')
# # #
# # # """*kwargs are stored in Python as a dictionary.
# # # *args are stored in Python as a tuple."""
# # #
# # # def tester(**kwargs):
# # #    for key, value in kwargs.items():
# # #        print(key, value, end = " ")
# # # tester(Sunday = 1, Monday = 2, Tuesday = 3, Wednesday = 4)
# # # # Sunday 1 Monday 2 Tuesday 3 Wednesday 4
# #
# # # #########################################################################
# # from math import *
# #
# # a = 2.19
# # b = 3.999999
# # c = -3.30
# # print(int(a), floor(b), ceil(c), fabs(c))  # 2 3 -3 3.3
# # # #########################################################################
# #
# # """The ^ operator in sets will return a set containing common of elements of its operand sets."""
# #
# # s1 = {1, 2, 3, 4, 5}
# # s2 = {2, 4, 6}
# # print(s1 ^ s2)   #{1, 3, 5, 6}
# # # #########################################################################
# # """prints the values in a, which are not present in b."""
# # a = [1, 2, 3, 4]
# # b = [3, 4, 5, 6]
# # c = [x for x in a if x not in b]
# # print(c)
# # # #########################################################################
# #
# # """The above function basically calculates the gcd of 2 numbers recursively.
# #  The gcd of 20 and 50 is 10, so the answer is A."""
# # def solve(a, b):
# #    return b if a == 0 else solve(b % a, a)
# # print(solve(20, 50))
# # # #########################################################################
# # def compress_string(s):
# #   """
# #   Compresses a string by counting consecutive occurrences of each character.
# #
# #   Args:
# #       s: The string to compress.
# #
# #   Returns:
# #       The compressed string.
# #   """
# #   compressed_string = ""
# #   char_count = 1
# #   for i in range(1, len(s)):
# #     if s[i] == s[i - 1]:
# #       char_count += 1
# #     else:
# #       compressed_string += s[i - 1] + str(char_count)
# #       char_count = 1
# #   compressed_string += s[-1] + str(char_count)
# #   return compressed_string
# #
# # # Test the function
# # string = "aabbbcceddbb"
# # compressed_string = compress_string(string)
# # print(compressed_string)  # Output: 2a3b2c1e2d2b
# #
# # # #########################################################################
# #
# # #Decorator - double
# #
def dec1(fun):
    def inner():
        x = fun()
        return x * x

    return inner


def dec2(fun):
    def inner():
        x = fun()
        return 2 * x

    return inner


@dec1
@dec2
def num():
    return 10


print(num(), "1111111111")
# #
# # """first dec1 starts and inside dec1 fun is there so it goes to dec2,
# # inside dec2 another fun is there so it goes to num and return 10 to x in dec2 inner method
# # so next return 2*10=20, 20 returns to x in dec1 and next return x*x= 20*20=400
# # output is 400
# # """
# # # #########################################################################
# #
'''remove 30 at 2nd and 3rd time # duplicate'''


# #
# # data = [10, 20, 30, 40, 30, 22, 30,40,30,50,30]
# # new_data = []
# # count = 0
# # for x in data:
# #     if x==30:
# #         count +=1
# #
# #         if count ==2 or count==3:
# #             continue
# #     new_data.append(x)
# #
# # print(new_data)
# # # #########################################################################
#
# def star(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("\r")
#
# star(5)
#
#
# def myfunc(n):
#     k = n - 1
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("\r")
#
# n = 5
# myfunc(n)
#
#
# def starnum(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print(f"{j} ", end="")
#         print("\r")
#
# starnum(5)
#
#
# def starnum(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print(f"{j + 1} ", end="")
#         print("\r")
#
# starnum(5)
#
#
# def starnum(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print(f"{i + 1} ", end="")
#         print("\r")
#
# starnum(5)
#
# # # #########################################################################
# #prime number: num divide by 1 and itself
def prime(n):
    # if n>1:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime")
            break

    else:
        print(f"{n} is prime")


prime(13)


# # # #########################################################################
# # Fibonacci series without recursive: 0 1 1 2 3 5 8 ....

def fib(n):
    a, b = 0, 1
    if n <= 1:
        return 1
    else:
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b


# fib(5)
# # # #########################################################################
# # Fibonacci series with recursive:
def fib(n):
    if n <= 1:
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))


# a = fib(5)
# a = int(input("enter num:"))
# for i in range(a):
#     print(fib(i), end=" ")

# # # #########################################################################
## factorial

def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print(factorial)


fact(5)
# # # #########################################################################
#Sum of any 2 digits in a list == required num

l = [4, 5, 7, 9, 1, 3]


def sum(n):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if i != j and l[i] + l[j] == n:
                print(l[i], l[j])


sum(10)


#sort the list

def sort():
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] >= l[j]:
                l[i], l[j] = l[j], l[i]


sort()
print(l)


# # # #########################################################################
#palidrome or not
#
def paliStr(n):
    rev_str = ""
    for i in str(n):
        rev_str = i + rev_str

    if rev_str == str(n):
        print(f"{n} is palindrome")
    else:
        print(f"{n} is not palindrome")


paliStr('madam')
paliStr(12321)


#palindrome of Numbers

def paliNum(n):
    a = n
    rev = 0
    while a > 0:
        x = a % 10
        rev = rev * 10 + x
        a = a // 10

    if rev == n:
        print(f"{n} is palindrome")
    else:
        print(f"{n} is not palindrome")


paliNum(112321)

# # # #########################################################################


a = "sanjeev"

print(a[1:5][::-1])


# # # #########################################################################

#patterns

def pat(n):
    k = n - 1
    for i in range(0, n):
        # for j in range(0, k):
        #     print(end=" ")
        # k=k-1
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")


pat(5)


# # # #########################################################################

#Leap Year

def leapYear(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                print(f"{n} is a Leap Year")

            else:
                print(f"{n} is not a Leap Year")
        else:
            print(f"{n} is a leap year")
    else:
        print(f"{n} is not a leap year")


leapYear(1992)

import re

text = "hellohelloworld"

# Remove the first occurrence of "hello" using a case-insensitive search
new_text = re.sub(r"hello", "", text, count=1)

print(new_text)  # Output: helloworld

d1 = {1: 200, 2: 300, 3: 500}
d2 = {1: 500, 2: 700, 4: 600}
# result_dict = {}
# for k1, v1 in d1.items():
#     for k2, v2 in d2.items():
#         if k1 == k2:
#             result_dict[k1] = v1+v2
result = {k2: d1[k2] + v2 if d1.get(k2) else v2 for k2, v2 in d2.items()}
print(result)

"x **2 +3"

# x=5
print(eval("x**2+3", {'x': 5}))


# Python3 program to
# Check if the string is pangram


def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True


# Driver code
string = 'the quick brown fox jumps over the lazy dog'
if ispangram(string) == True:
    print("Yes")
else:
    print("No")
