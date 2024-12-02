#program to check the frequency of a particular string in a text file
f = open("F:/Training/Python Assignments/Assignment2/this.txt", "r")
rd = f.read().strip().split() #reading and splitting the read contents to remove trailing and following spaces and indivisualising words
c=0 #initialising the counter
print("Enter the string to find the frequency:")
n=input() #asking the user for the string
for row in rd:
    if word in row:
        c = c+1 #increasing the counter if the word is found
w = open("F:\Training\Python Assignments\Assignment2\this_o.txt", "w")
print("The word this is being repeated ", c, "times", w=file) #writing the output in file
