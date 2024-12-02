# Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> a=10
# >>> b=10
# >>> id(a)
# 1584261184
# >>> id(b)
# 1584261184
# >>> a==b?
# SyntaxError: invalid syntax
# >>> a==b
# True
# >>> aisb
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     aisb
# NameError: name 'aisb' is not defined
# >>> a is b
# True
# >>> a=52.56
# >>> b=52.56
# >>> id(a)
# 54318592
# >>> id(b)
# 55099280
# >>> a is b
# False
# >>> a=52+5j
# >>> b=52+5j
# >>> id(a)
# 58412880
# >>> id(b)
# 58412952
# >>> a is b
# False
# >>> a=1
# >>> b=1
# >>> id(a)
# 1584261040
# >>> id(b)
# 1584261040
# >>> a is b
# True
# >>> a=true
# Traceback (most recent call last):
#   File "<pyshell#23>", line 1, in <module>
#     a=true
# NameError: name 'true' is not defined
# >>> a="dsy"
# >>> b="dsy"
# >>> id(a)
# 52017536
# >>> id(b)
# 52017536
# >>> a is b
# True
# >>> a=257
# >>> b=257
# >>> id(a)
# 58506592
# >>> id(b)
# 58506832
# >>> type(id)
# <class 'builtin_function_or_method'>
# >>> x=[10,20,30]
# >>> type(x)
# <class 'list'>
# >>> b=bytes(x)
# >>> type(b)
# <class 'bytes'>
# >>> x
# [10, 20, 30]
# >>> x=[10,20,300]
# >>> b=bytes(x)
# Traceback (most recent call last):
#   File "<pyshell#51>", line 1, in <module>
#     b=bytes(x)
# ValueError: bytes must be in range(0, 256)
# >>> b=bytearray(x)
# Traceback (most recent call last):
#   File "<pyshell#52>", line 1, in <module>
#     b=bytearray(x)
# ValueError: byte must be in range(0, 256)
# >>> x=[10,20,30]
# >>> b=bytearray(x)
# >>> print(b)
# bytearray(b'\n\x14\x1e')
# >>> l=[10,10.5,12]
# >>> type(l)
# <class 'list'>
# >>> l[0]
# 10
# >>> l[0:1]
# [10]
# >>> l[0:2]
# [10, 10.5]
# >>> id(l)
# 58748200
# >>> l1[12,16,"hello",[1,2,3],34]
# Traceback (most recent call last):
#   File "<pyshell#62>", line 1, in <module>
#     l1[12,16,"hello",[1,2,3],34]
# NameError: name 'l1' is not defined
# >>> l1[12,16,"hello",(1,2,3),34]
# Traceback (most recent call last):
#   File "<pyshell#63>", line 1, in <module>
#     l1[12,16,"hello",(1,2,3),34]
# NameError: name 'l1' is not defined
# >>> l1[12,16.52,"hello",true]
# Traceback (most recent call last):
#   File "<pyshell#64>", line 1, in <module>
#     l1[12,16.52,"hello",true]
# NameError: name 'l1' is not defined
# >>> l1[12,16.56,"hello",34+5j]
# Traceback (most recent call last):
#   File "<pyshell#65>", line 1, in <module>
#     l1[12,16.56,"hello",34+5j]
# NameError: name 'l1' is not defined
# >>> l2[12,16,"hello",[1,2,3],34]
# Traceback (most recent call last):
#   File "<pyshell#66>", line 1, in <module>
#     l2[12,16,"hello",[1,2,3],34]
# NameError: name 'l2' is not defined
# >>> l1[12,16.56,"hello",34]
# Traceback (most recent call last):
#   File "<pyshell#67>", line 1, in <module>
#     l1[12,16.56,"hello",34]
# NameError: name 'l1' is not defined
# >>> l5[12,16.56,'hello',34]
# Traceback (most recent call last):
#   File "<pyshell#68>", line 1, in <module>
#     l5[12,16.56,'hello',34]
# NameError: name 'l5' is not defined
# >>> l=[12,23,45,'hi','no',100]
# >>> l[3:5]
# ['hi', 'no']
# >>> l=[12,23,45,'hi','no',100]
# >>> l[3:5]
# ['hi', 'no']
# SyntaxError: multiple statements found while compiling a single statement
# >>> l=[12,23+5j,45.56,'hello',100]
# >>>
# >>> type(l)
# <class 'list'>
# >>> id(l)
# 58457672
# >>> l[3:]
# ['hello', 100]
# >>> l.add(208)
# Traceback (most recent call last):
#   File "<pyshell#77>", line 1, in <module>
#     l.add(208)
# AttributeError: 'list' object has no attribute 'add'
# >>> t=10,20,30"sanju"
# SyntaxError: invalid syntax
# >>> t=10,20,30,"sanju"
# >>> type(t)
# <class 'tuple'>
# >>> range(10)
# range(0, 10)
# >>> range(1,9)
# range(1, 9)
# >>> range(1,10,step)
# Traceback (most recent call last):
#   File "<pyshell#83>", line 1, in <module>
#     range(1,10,step)
# NameError: name 'step' is not defined
# >>> range(1,10,2)
# range(1, 10, 2)
# >>> t[0]="hi"
# Traceback (most recent call last):
#   File "<pyshell#85>", line 1, in <module>
#     t[0]="hi"
# TypeError: 'tuple' object does not support item assignment
# >>>