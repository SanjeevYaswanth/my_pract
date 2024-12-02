# # # # import json
# # #
# # # # with open('example_2.json', 'r') as f:
# # # #     data = json.load(f)
# # # #     print(data)
# # #
# # #     # a = data['quiz']['maths']['q1']['options']
# # #     # print(a)
# # #     # for i in a:
# # #     #     print(i)
# # #     # print(data)
# # #
# # # # with open('new_converted.json', 'w') as g:
# # # #     b = json.dumps(data, indent=4)
# # # #     g.write(b)
# # #
# # # import pandas as pd
# # #
# # # data = pd.read_json('example_2.json')
# # # print(data.to_html())
# # #
# #
# # st = 'aabbbccddd'
# #
# # count_dict = {}
# #
# # for ch in st:
# #     if ch in count_dict:
# #         count_dict[ch] +=1
# #     else:
# #         count_dict[ch] = 1
# #
# # print(count_dict)
# #
# # s = ''
# # for k,v in count_dict.items():
# #     s += f'{v}{k}'
# #
# # print(s)
#
# nested_list = [[1, 2], [3, 4], [5, 6]]
#
# lists = [i for lt in nested_list for i in lt if i%2==0]
#
# print(lists)
#
# a='hello2'
# print(a*3)
#
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
#
#
# for k,v in dict2.items():
#     if k in dict1:
#         print(dict1[k], v)
#         dict1[k] = dict1[k] + v
#
#     else:
#         dict1[k] = v
#
# dict1.update(dict2)
# print(dict1) # {'a': 1, 'b': 5, 'c': 4}
#
# myDict = {'b': 2, 'a': 1, 'c': 3}
#
# keys = list(myDict.keys())
#
# for i in range(len(keys)):
#     for j in range(i+1):
#         if keys[i] < keys[j]:
#             keys[i], keys[j] = keys[j], keys[i]
#
# print(keys)
#
# sortedDict = {}
#
# for k in keys:
#     sortedDict[k] = myDict[k]
#
# print(sortedDict)

# dict1 = {'a': 1}
# dict2 = {'b': 2}
# dict3 = {'c': 3}
#
# dict1.update(dict2)
#
# dict1.update(dict3)
# print(dict1)

# lt = [0,1,2,3,4]
# squares = {x: x**2 for x in lt}
# squares = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
#
# l1 = [0,1,2,3,4]
# l2 = [0,1,2,3,4]
#
# print(id(l1)) #3015489106048
# print(id(l2)) #3015489104960
# if l1 is l2: # to compare the memory location of the 2 variables
#     print(True)
# else:
#     print(False)
#
# if l1 == l2: # to compare elements of both varibles are equal
#     print(True)
# else:
#     print(False)

# def word_count(sentence):
#     # Convert the sentence to lowercase to make the counting case-insensitive
#     sentence = sentence.lower()
#
#     # Split the sentence into words (assuming words are separated by spaces)
#     words = sentence.split()
#     print(words)
#
#     # Dictionary to store word counts
#     count_dict = {}
#
#     # Count occurrences of each word
#     for word in words:
#         if word in count_dict:
#             count_dict[word] += 1
#         else:
#             count_dict[word] = 1
#
#     return count_dict


# Example usage
# sentence = "This is a test. This test is only a test."
# result = word_count(sentence)
# print("Word counts:", result)
# print(min(result, key=result.get))


# l = [1,2,3,4,5,6,7,8,9,10,11]

# print([for i in l if ])

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n): #int(n**0.5) + 1):
#         # print(int(n**0.5))
#         if n % i == 0:
#             return False
#     return True
#
# def prime_numbers_in_range(lt:list):
#     primes = []
#     for num in lt:
#         if is_prime(num):
#             primes.append(num)
#     return primes
#
# print(prime_numbers_in_range([1,2,3,4,5,6,7,8,9,10,11]))

import json

#dt = {1: 73, 2: 41, 3: 58, 4: 12, 5: 86, 6: 24, 7: 95, 8: 37, 9: 62, 10: 79, 11: 13, 12: 22, 13: 91, 14: 54, 15: 69, 16: 33, 17: 17, 18: 88, 19: 47, 20: 59}

# primeKeys = []
#
# with open('dict.json', 'r') as f:
#     data = json.load(f)
#
# print(data)
# dictKeys = data.keys()
# print(dictKeys)
#
# for i in dictKeys:
#     if int(i) > 1:
#         for j in range(2, int(i)):
#             if int(i) % j == 0:
#                 break
#
#         else:
#             primeKeys.append(i)
# print(primeKeys)
#
# primedict = {}
#
# for i in primeKeys:
#     primedict[i] = data[i]
#
# print(primedict)
# with open('primedict.json','w') as h:
#     json.dump(primedict, h, indent=4)


def find_Line_Number_in_File(sentence, filePath):
    try:
        with open(filePath, 'r') as data:
            for line_number, line_value in enumerate(data, start=1):
                if sentence in line_value:
                    return line_number
    except FileNotFoundError:
        print("file not found")

    except Exception as e:
        print(f"execption occured as {e}")

    return None

x = find_Line_Number_in_File(sentence='class grandparents:', filePath=r'C:\Users\Admin\Desktop\OOPS.txt')
print(x)