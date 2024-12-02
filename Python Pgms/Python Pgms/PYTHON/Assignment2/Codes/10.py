# Program to merge mails
# name.txt file contains names one by one
with open("F:/Training/Python Assignments/Assignment2/names.txt",'r') as names_file:
   # open body.txt for  reading body
   with open("F:/Training/Python Assignments/Assignment2/body.txt",'r') as body_file:
       # read entire content of the body
       body = body_file.read()
       # iterate over names
       for name in names_file:
           mail = "Hi "+name+body
           # write the mails to individual files
           with open(name.strip()+".txt",'w') as mail_file:
               mail_file.write(mail)