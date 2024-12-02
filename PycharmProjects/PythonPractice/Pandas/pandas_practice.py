import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.arange(1,21).reshape(5,4), index=['R1', 'R2', 'R3', 'R4', 'R5'], columns=['C1', 'C2', 'C3', 'C4'])
print("*"*20)
print(df.head(2))
print("*"*20)
print(df)
print("*"*20)

print(df.loc['R1'])
print(type(df.loc['R1']))
print("*"*20)

print(df.iloc[:3,:4])
print(type(df.iloc[:3,:4]))
print("*"*20)

print(df[['C1','C2','C3']])
print("*"*20)

print(df.shape)
print("*"*20)

print(df.iloc[:3,:3].values)
print("*"*20)

print(type(df.iloc[:3,:3].values))
print("*"*20)

print(df.to_string())
print(df.ndim)
# df.to_csv( "smart.csv")
print(pd.read_csv('smart.csv', usecols=['C1', 'C4']))
# print(df[df['C1']>10])