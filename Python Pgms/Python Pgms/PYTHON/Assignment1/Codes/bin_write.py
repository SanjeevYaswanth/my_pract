#program to read binary contents of a file and then writing the same to another file
f = open("F:\Training\Python Assignments\Assignment1\picture038.jpg", "rb")
rd = f.read()
b = open("F:\Training\Python Assignments\Assignment1\picture.jpg", "wb")
b.write(rd) #writing rd to another file.