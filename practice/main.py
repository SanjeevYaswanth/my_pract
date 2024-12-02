# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# bubblesort
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(i+1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"bubble sort: {bubblesort(arr)}")

#selection sort

def selectionsort(arr):
    for i in range(len(arr)):
        mid_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mid_idx]:
                mid_idx = j
        arr[i], arr[mid_idx] = arr[mid_idx], arr[i]

    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"selection sort: {selectionsort(arr)}")


#insersion sort

def insersionsort(arr):
    for i in range(len(arr)):
        key = arr[i]
        for j in range(i,0,-1):
            if key < arr[j-1]:
                arr[j] = arr[j-1]

            else:
                arr[j] = key
                break
        else:
            arr[0] = key
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"insersion sort: {insersionsort(arr)}")

#merge sort

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        leftarr = arr[:mid]
        rightarr = arr[mid:]

        mergesort(leftarr)
        mergesort(rightarr)

        i=j=k=0
        while i<len(leftarr) and j<len(rightarr):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i+=1
                # k+=1
            else:
                arr[k] = rightarr[j]
                j+=1
            k+=1

        while i<len(leftarr):
            arr[k] = leftarr[i]
            i+=1
            k+=1

        while j<len(rightarr):
            arr[k] = rightarr[j]
            j+=1
            k+=1
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"merge sort: {mergesort(arr)}")

s='aabbbcccc'
acount = s.count('a')
bcount = s.count('b')
ccount = s.count('c')

counts = ''
counts ='a'+str(acount)+'b'+str(bcount)+'c'+str(ccount)
print(counts)
print(list(s))

arr = [64, 34, 25, 12, 22, 11, 90, 'a']

for i, j in enumerate(arr):
    print(i,j)

t1=(1,2)
t2 = (2,3)
print(t1+t2)
print(t1*5)

# Using all() with a list
numbers = [0,1, 2, 3, 4]
print(all(x > 0 for x in numbers))  # True, because all numbers are greater than 0

# Using all() with a tuple
words = ("hello", "world")
print(all(len(word) > 2 for word in words))  # True, because all words have more than 2 characters

l=[]
# Using all() with an empty iterable
print(all(l))  # True, because an empty iterable is considered to have all elements as True

s={5,1,4, 55,2,7,0, 25, 5,2, 8, -1}
# s.pop()
s.remove(-1)
print(s)

s1={3,4}
s2={4,5,6,7, 0, 3}
print(s1.issubset(s2))

def filedata(path):
    f = open(path, 'r')
    # data = f.read()
    data = f.readline()
    # data = f.readlines()
    print(data)

filedata(r'C:\Users\Admin\Desktop\data.txt')
from collections import deque
q = deque()
q.appendleft(10)
q.appendleft(20)
q.append(30)
q.append(40)
print(q)
q.pop()
print(q)
q.popleft()
print(q)

#class super static


for i in range(2,3):
    print(i)