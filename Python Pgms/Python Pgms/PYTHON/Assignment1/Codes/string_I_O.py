#taking a particular string from one file and placing it into other.
f=open("F:\Training\Python Assignments\Assignment1\sample_w.txt", "r")
rd = f.read()
print("Enter the string to be compared and written:")
n=input() #taking input from the user whether what string is to be placed in other file
b = open("F:\Training\Python Assignments\Assignment1\sample_w_w.txt", "wt")
for x in rd: #iterating through the file to check for the string
    for y in x:
        if y==n:
            b.write(y) #writing the content in file if matches.