# customer mall data

import csv
from csv import DictReader
count=cf=sumM=sumF=avgm=avgf=0

path = open (r'C:\Users\SHIVANI\Github_Tutorial\Clustering-of-Mall-Customers\Mall_Customers.csv','r')
csv_reader = DictReader(path)
for row in csv_reader:
    checkinput=((row['Genre'],row['Spending Score (1-100)']))
    if (row['Genre'] == 'Male'):
        #print checkinput 
        count= count + 1
        sumM =(sumM+int(checkinput[1]))
    if (row['Genre'] == 'Female'):
        #print checkinput
        cf= cf+1
        sumF=(sumF+int(checkinput[1]))
avgm= sumM/count
avgf= sumF/cf
print 'The average speding score of male is ',avgm
print 'The average Spending score of female is',avgf
path.close()
