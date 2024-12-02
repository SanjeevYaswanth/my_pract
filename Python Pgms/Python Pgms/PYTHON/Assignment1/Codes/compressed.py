#program to read from and write to a compressed file.
import gzip #importing required module
with gzip.open(r'F:\Training\Python Assignments\Assignment1\my_python_files.zip', 'rt') as f:
    text = f.read() #opening and reading the compressed file.
    print(text)
with gzip.open(r'C:\Users\hp\Desktop\file\ser.zip', 'wt') as f:
    f.write('qwerty') #opening and writing to a compressed file.