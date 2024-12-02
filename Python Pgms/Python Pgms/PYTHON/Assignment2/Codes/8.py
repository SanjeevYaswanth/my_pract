#program to update contents of an xml file
import xml.etree.ElementTree as ET #importing required modules 
f = ET.parse("F:\Training\Python Assignments\Assignment2\sampleXml.xml")
root = f.getroot() #parsing & getting the root
print(root.tag)
print(root.attrib)
for child in root: #iterating through file
    print(child.tag, child.attrib, child.text)
    for gc in child:
        print(gc.tag, gc.attrib, gc.text)

c1 = root.find('./country[@name="Panama"]') #reaching a particular element and updating it
c1.attrib["name"]="India"
c2 = root.find('./country/year')
c2.text="1"
'''c3 = root.find("./country/neighbor[@name=""]")
c3.attrib["name"]="India"
c3.attrib["direction"] ="gh"'''
'''for neighbor in root[2].iter("neighbor"):
    neighbor.attrib["name"]="fgfdgfd"
    neighbor.attrib["direction"]="gffd"'''


f.write("F:\Training\Python Assignments\Assignment2\output.xml") #writing the updated contents to a different file


