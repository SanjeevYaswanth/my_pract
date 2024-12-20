#program to extract contents of a zipped folder
# importing required modules
from zipfile import ZipFile

# specifying the zip file name
file_name = "F:\Training\Python Assignments\Assignment1\my_python_files.zip"

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()

    # extracting all the files
    zip.extractall("F:\Training\Python Assignments\Assignment1\Extract_all")
    print('Done!')