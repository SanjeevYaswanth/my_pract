#program to get resolution of an image
from PIL import Image #importing required modules
img = Image.open("F:\Training\Python Assignments\Assignment2\picture038.jpg")
a = img.size #storing resolution in "a"
print(a) #prints resolution