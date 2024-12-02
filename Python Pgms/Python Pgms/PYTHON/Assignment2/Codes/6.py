#program to parse huge xml files
import xml.etree.ElementTree as ET #importing required modules
for a, b in ET.iterparse("F:\Training\Python Assignments\Assignment2\huge_xml.xml"): #a corresponds to the events and b corresponds to the elements
    if b.tag == "color_swatch" and a=="end": #directly accessing the element
        print(b.text)
    if a == "end":
        print(b.tag, b.attrib, b.text) 