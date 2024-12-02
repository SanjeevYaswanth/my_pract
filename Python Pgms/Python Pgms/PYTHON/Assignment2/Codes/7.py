#program to change dictionary to xml
from dicttoxml import dicttoxml #importing required modules

dictionary = {
    "time": {"hour":"1", "minute":"30","seconds": "40"},
    "place": {"street":"40 something", "zip": "00000"},
    "location":{"continent":"Asia", "Country":"India"},
    "Sport":{"National":"Hockey", "Preffered":"Cricket"}
} #defining a dictionary

xml = dicttoxml(dictionary, custom_root='data', attr_type=False).decode() #changing the dictionary to xml and decoding it so that it can be written into a file.
'''print(xml)'''
b = open("F:\Training\Python Assignments\Assignment2\dict-xml.xml", "wt")
b.write(xml) #writing to file