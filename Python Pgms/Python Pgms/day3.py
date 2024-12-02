# Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> l=[10,20,30]
# >>> type(l)
# <class 'list'>
# >>> l2=[40,50,60]
# >>> l3=l1+l2
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     l3=l1+l2
# NameError: name 'l1' is not defined
# >>> l3=l+l2
# >>> l+l2
# [10, 20, 30, 40, 50, 60]
# >>> l1=[10,20,30]
# >>> l2=[40,50,60]
# >>> l1+l2
# [10, 20, 30, 40, 50, 60]
# >>> s={1,2,3,4}
# >>> s
# {1, 2, 3, 4}
# >>> s
# {1, 2, 3, 4}
# >>> s[1]
# Traceback (most recent call last):
#   File "<pyshell#12>", line 1, in <module>
#     s[1]
# TypeError: 'set' object is not subscriptable
# >>> s(1)
# Traceback (most recent call last):
#   File "<pyshell#13>", line 1, in <module>
#     s(1)
# TypeError: 'set' object is not callable
# >>> s[0]
# Traceback (most recent call last):
#   File "<pyshell#14>", line 1, in <module>
#     s[0]
# TypeError: 'set' object is not subscriptable
# >>> l1[0]
# 10
# >>> s{1,2,2,22,22,3}
# SyntaxError: invalid syntax
# >>> s={1,2,2,22,22,3}
# >>> s
# {1, 2, 3, 22}
# >>> frozenset(s)
# frozenset({1, 2, 3, 22})
# >>> d={10:"hi",20:"hello"}
# >>> type(d)
# <class 'dict'>
# >>> keys()
# Traceback (most recent call last):
#   File "<pyshell#22>", line 1, in <module>
#     keys()
# NameError: name 'keys' is not defined
# >>> keys(d)
# Traceback (most recent call last):
#   File "<pyshell#23>", line 1, in <module>
#     keys(d)
# NameError: name 'keys' is not defined
# >>> values(d)
# Traceback (most recent call last):
#   File "<pyshell#24>", line 1, in <module>
#     values(d)
# NameError: name 'values' is not defined
# >>> d1={name:"sanju",id:2020}
# Traceback (most recent call last):
#   File "<pyshell#25>", line 1, in <module>
#     d1={name:"sanju",id:2020}
# NameError: name 'name' is not defined
# >>> d1={"name":"sanju","id":2020}
# >>> type(d1)
# <class 'dict'>
# >>> d1[1]
# Traceback (most recent call last):
#   File "<pyshell#28>", line 1, in <module>
#     d1[1]
# KeyError: 1
# >>> d[10]
# 'hi'
# >>> l[]
# SyntaxError: invalid syntax
# >>> l=[]
# >>> l
# []
# >>> nonw
# Traceback (most recent call last):
#   File "<pyshell#33>", line 1, in <module>
#     nonw
# NameError: name 'nonw' is not defined
# >>> none
# Traceback (most recent call last):
#   File "<pyshell#34>", line 1, in <module>
#     none
# NameError: name 'none' is not defined
# >>> exit
# Use exit() or Ctrl-Z plus Return to exit
# >>> def M1()
# SyntaxError: invalid syntax
# >>> def m1():
# 	a=10
# 	print(m1())
#
#
# >>>
# >>>
# >>>
# >>> del
# SyntaxError: invalid syntax
# >>> del(m1)
# >>> a=10
# >>> b=20
# >>> a+b
# 30
# >>> a-b
# -10
# >>> a*b
# 200
# >>> a/b
# 0.5
# >>> a%b
# 10
# >>> a//b
# 0
# >>> a**b
# 100000000000000000000
# >>> a>b
# False
# >>> a<b
# True
# >>> a<=b
# True
# >>> a>=b
# False
# >>> a and b
# 20
# >>> a or b
# 10
# >>> a not b
# SyntaxError: invalid syntax
# >>> a not
# SyntaxError: invalid syntax
# >>> not a
# False
# >>> not b
# False
# >>> a=1
# >>> b=0
# >>> a and b
# 0
# >>> a or b
# 1
# >>> not a
# False
# >>> not b
# True
# >>> a =0
# >>> b="hi"
# >>> a and b
# 0
# >>> a or b
# 'hi'
# >>>  not b
#
# SyntaxError: unexpected indent
# >>> not b
# False
# >>> not a
# True
# >>> a=10
# >>> b=4
# >>> a & b
# 0
# >>> a | b
# 14
# >>> a<<1
# 20
# >>> a+=b
# >>> print(a)
# 14
# >>> print(b)
# 4
# >>> a=+b
# >>> a=-b
# >>> print(a)
# -4
# >>> a-=b
# >>> print(a)
# -8
# >>> a=10
# >>> b=4
# >>> a-=b
# >>> print(a)
# 6
# >>>