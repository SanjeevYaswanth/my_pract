#program to simply parse xml 
import xml.etree.ElementTree as ET #importing the required module
f = ET.parse("F:\Training\Python Assignments\Assignment2\sampleXml.xml") #parsing the data and storing it in f
root = f.getroot() #getting the root
print(root.tag) #.tag returns the tag of elements, .attrib returns the set of attributes and .text returns the value of the element 
print(root.attrib)
for child in root: #iterating through the xml tree
    print(child.tag, child.attrib, child.text)
    for gc in child:
        print(gc.tag, gc.attrib, gc.text)
