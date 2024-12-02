#Reading the contentsa of a file and writing some part of it to the other file
f=open("F:\Training\Python Assignments\Assignment1\sample_w.txt", "r")
rd = f.read()
rdn = rd[10:20] #Extracting content of the file
b = open("F:\Training\Python Assignments\Assignment1\sample_w_w.txt", "wt")
b.write(rdn) #writing the extracted content to other file 