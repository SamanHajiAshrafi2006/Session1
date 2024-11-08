import csv
import math
# This code helps you to add new students and their results to the csv file :)


print("do you want to re-write or append(1 for re-write and 2 for append)")
x = input() # if we want to re-write the whole file  we should use write which is 'w' and if we just want to add to our csv file we need to append by 'a'
writeOrappend = 'a'
if x == '1': writeOrappend = 'w'  # check what does our client wants
MyFields = ["ID", "name", "Result"] # our headers!

print("how many rows do you want to add: ") # to realise how many rows we need to add
i = int(input())
with open("Data.csv", mode=writeOrappend) as csvfile: #opening the csv file
    writer = csv.DictWriter(csvfile, MyFields)
    if writeOrappend == 'w': # the only diffrence between write and append in this case is headers, if its 'w' we need to write them
        writer.writeheader() # writing the headers

    
    for j in range (i): # we get the student's info at first then add them to our csv file! 
        print("enter the ID:")
        Id = input()
        print("enter the name:")
        name = input()
        print("enter the Result:")
        Result = float(input())
        
        writer.writerow({"ID":Id, "name":name, "Result":Result}) # writing the rows in Data.csv
