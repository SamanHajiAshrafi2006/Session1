import csv
#This file checks if the student is failed or passed the class
#the author knows that this code could be merged to GetData.py but foe the sake of the project and class it had to be writen like this

counter = 0 #we use counter to remove empty lists and fieldnames 
Condition = "passed" #or failed
MyFields = ["ID", "name", "Result", "condition"] #our headers for Final.csv!

with open("Data.csv", 'r') as csv_file: #opening our data to work on it
    csv_reader = csv.reader(csv_file)
    with open("Final.csv", 'w') as MyFile: #making a new data file to put our finalised data in it(with condition)
        writer = csv.DictWriter(MyFile, MyFields)
        writer.writeheader() #writing the headers
        for row in csv_reader:
            if counter > 1 and counter %2 == 0:
                Flag = float(row[2]).__ceil__() #rounding the numbers upwards for the sake of project
                if Flag < 10: 
                    Condition = "FAILED" #check if the student is passed or failed
                row.append(Condition) #adding condiotion to our lists to finalise our data
                writer.writerow({"ID":row[0], "name":row[1], "Result":row[2], "condition": row[3]}) #adding a new row of data to our fina.csv

            counter +=1