# Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> print(dir(str))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# >>> a="sanju"
# >>> a.class()
# SyntaxError: invalid syntax
# >>> a.__class()
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     a.__class()
# AttributeError: 'str' object has no attribute '__class'
# >>> a.replace("sanju","manu")
# 'manu'
# >>> a
# 'sanju'
# >>> a=="sanju"
# True
# >>> a is "sanju"
# True
# >>> a="sanjeev yaswanth manoj kumar"
# >>> a.find("manoj")
# 17
# >>> a.upper()
# 'SANJEEV YASWANTH MANOJ KUMAR'
# >>> a.expandtabs()
# 'sanjeev yaswanth manoj kumar'
# >>> a.find("duggi")
# -1
# >>> a.split()
# ['sanjeev', 'yaswanth', 'manoj', 'kumar']
# >>> a.find("noj")
# 19
# >>> a.find("Noj")
# -1
# >>> a.index("y")
# 8
# >>> a.index("Y")
# Traceback (most recent call last):
#   File "<pyshell#17>", line 1, in <module>
#     a.index("Y")
# ValueError: substring not found
# >>> a.len()
# Traceback (most recent call last):
#   File "<pyshell#18>", line 1, in <module>
#     a.len()
# AttributeError: 'str' object has no attribute 'len'
# >>> len(a)
# 28
# >>> a.replace("duggi","hero")
# 'sanjeev yaswanth manoj kumar'
# >>> a.replace("manoj","hero")
# 'sanjeev yaswanth hero kumar'
# >>> a.replace("duggi","hero")
# 'sanjeev yaswanth manoj kumar'
# >>> id(a)
# 58183144
# >>> a.replace("duggi","hero")
# 'sanjeev yaswanth manoj kumar'
# >>> id(a)
# 58183144
# >>> a.replace("manoj","hero")
# 'sanjeev yaswanth hero kumar'
# >>> id(a)
# 58183144
# >>> a[1]
# 'a'
# >>> a
# 'sanjeev yaswanth manoj kumar'
# >>> a='sanjeev yaswanth,manoj kumar'
# >>> a.split()
# ['sanjeev', 'yaswanth,manoj', 'kumar']
# >>> b=13-10-2020
# >>> b.split()
# Traceback (most recent call last):
#   File "<pyshell#33>", line 1, in <module>
#     b.split()
# AttributeError: 'int' object has no attribute 'split'
# >>> b="13-10-2020"
# >>> b.split()
# ['13-10-2020']
# >>> c="hello : good Morning"
# >>> c.split()
# ['hello', ':', 'good', 'Morning']
# >>> a="   hello  good  Morning  "
# >>> a.strip()
# 'hello  good  Morning'
# >>> a.remove("good")
# Traceback (most recent call last):
#   File "<pyshell#40>", line 1, in <module>
#     a.remove("good")
# AttributeError: 'str' object has no attribute 'remove'
# >>> a.remove()
# Traceback (most recent call last):
#   File "<pyshell#41>", line 1, in <module>
#     a.remove()
# AttributeError: 'str' object has no attribute 'remove'
# >>> a
# '   hello  good  Morning  '
# >>> a.casefold()
# '   hello  good  morning  '
# >>> a.center()
# Traceback (most recent call last):
#   File "<pyshell#44>", line 1, in <module>
#     a.center()
# TypeError: center expected at least 1 argument, got 0
# >>> a.center("hello")
# Traceback (most recent call last):
#   File "<pyshell#45>", line 1, in <module>
#     a.center("hello")
# TypeError: 'str' object cannot be interpreted as an integer
# >>> a
# '   hello  good  Morning  '
# >>> a.strip('go')
# '   hello  good  Morning  '
# >>> a.strip()
# 'hello  good  Morning'
# >>> a
# '   hello  good  Morning  '
# >>> b
# '13-10-2020'
# >>> a.join(b)
# '1   hello  good  Morning  3   hello  good  Morning  -   hello  good  Morning  1   hello  good  Morning  0   hello  good  Morning  -   hello  good  Morning  2   hello  good  Morning  0   hello  good  Morning  2   hello  good  Morning  0'
# >>> a
# '   hello  good  Morning  '
# >>> a
# '   hello  good  Morning  '
# >>> a.startwith("good")
# Traceback (most recent call last):
#   File "<pyshell#54>", line 1, in <module>
#     a.startwith("good")
# AttributeError: 'str' object has no attribute 'startwith'
# >>> a.startswith("good")
# False
# >>> a.startswith("hello")
# False
# >>> a='sanjeev yaswanth manoj kumar'
# >>> a.startswith("kumar")
# False
# >>> a.startswith("sanjeev")
# True
# >>> a.endswith("kumar")
# True
# >>> a.isalpha()
# False
# >>> a.isstr()
# Traceback (most recent call last):
#   File "<pyshell#62>", line 1, in <module>
#     a.isstr()
# AttributeError: 'str' object has no attribute 'isstr'
# >>> print("{0} 's salary is {1} and his age is {2}".format(name,salary,age))
# Traceback (most recent call last):
#   File "<pyshell#63>", line 1, in <module>
#     print("{0} 's salary is {1} and his age is {2}".format(name,salary,age))
# NameError: name 'name' is not defined
# >>> a
# 'sanjeev yaswanth manoj kumar'
# >>> a.reverse()
# Traceback (most recent call last):
#   File "<pyshell#65>", line 1, in <module>
#     a.reverse()
# AttributeError: 'str' object has no attribute 'reverse'
# >>> a.append("duggi")
# Traceback (most recent call last):
#   File "<pyshell#66>", line 1, in <module>
#     a.append("duggi")
# AttributeError: 'str' object has no attribute 'append'
# >>> a
# 'sanjeev yaswanth manoj kumar'
# >>> b
# '13-10-2020'
# >>> join(a,b)
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     join(a,b)
# NameError: name 'join' is not defined
# >>> b.capitalize()
# '13-10-2020'
# >>> b.isdigit()
# False
# >>> print(dir(list))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# >>>