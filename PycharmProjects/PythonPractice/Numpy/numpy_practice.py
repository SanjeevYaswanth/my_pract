import numpy as np
from numpy.ma.core import shape

l = [1,2,3,4,5]

m1 = [1, 2, 3, -1]
m2 = [4, 5, 6, -2]
m3 = [7, 8, 9, -3]


arr = np.array((m1,m2,m3))
# print(arr)
# print(arr.shape)
# arr2 = arr.reshape(4,3)
# print(arr2)
# print(arr2.shape)
# arr3 = arr2.reshape(1,12)
# print(arr3)
# print(arr3.shape)
# arr4 = arr3.reshape(4,3)
# print(arr4)
# print(arr4.shape)
# print(arr4[1][0])
# print(arr4[:,1:])
# print(arr4[0:2,0:3])
# print(arr4.dtype)

arr = np.arange(0,12)
print(arr)
print(arr[arr<2])
v = arr.reshape(4,1,3)
print(v)
print(v.shape)
print(v.reshape(-1))

x = int(5)
print(x)

import pandas as pd

a = [1,2,3,4]
sr = pd.Series(a)
print(sr)
