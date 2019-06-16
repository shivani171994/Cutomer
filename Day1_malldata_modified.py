# Finding the average time spend

path = open (r'C:\Users\SHIVANI\Github_Tutorial\Clustering-of-Mall-Customers\Mall_Customers.csv','r')
gender_dict= dict()
for line in path:
     coloumn = line.split(',')
     #print coloumn
     gender,score = coloumn[1],coloumn[4]
     #print gender,score
     if line[0].isalpha():
         continue
     if gender in gender_dict:
         gender_dict[gender].append(int(score))
     else:
         gender_dict[gender] = list()
#print gender_dict

for gender,score in gender_dict.items():
    print gender_dict.items()
    #print (gender,sum(score)/len(score))
path.close()
