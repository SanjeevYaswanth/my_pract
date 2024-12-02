import json


with open("sample2.json", "r") as data:
    '''json.load'''
    # value = json.load(data)
    # print(value)
    # print(value['address']['city'])

    '''json.loads'''
    value = json.loads(data.read())
    print(value)
    print(value['address']['city'])

with open('sample1.json', "w") as data1:
    '''json.dump'''
    # json.dump(value, data1, indent=4)

    '''json.dumps'''
    write = json.dumps(value, indent=4)
    data1.write(write)
