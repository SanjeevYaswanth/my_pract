#program to read and write content from and to a csv file
import csv #importing required module
f = open("F:\Training\Python Assignments\Assignment2\SampleCSV.csv", "r")
rd= csv.reader(f, delimiter=",") #reading from file specifying the delimiter
lc = 0 #initialising line count
for row in rd:
    print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
    lc += 1
print("Total", lc, "lines processed.")

wf= open('F:\Training\Python Assignments\Assignment2\G_edu.csv', "w") #writing the contents in g_edu.csv
wr = csv.writer(wf, delimiter=',', quotechar='"') #writing commences, list of row contents get written to file
wr.writerow(['Nipon', 'IT', 'November', 1996])
wr.writerow(['Praddy', 'IT', 'April', 1996])
wr.writerow(['Gharitha', 'IT', 'Jan', 1996])
wr.writerow(['Chandan', 'IT', 'May', 1996])
wr.writerow(['Ravi', 'IT', 'March', 1996])