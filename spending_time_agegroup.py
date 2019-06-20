import pandas as pd

file1 = (r'C:\Users\SHIVANI\Github_Tutorial\Clustering-of-Mall-Customers\Mall_Customers.csv')
df = pd.read_csv(file1)

df['Agegroup'] = pd.cut(df.Age,bins=[0,18,29,39,49,59,69,79],labels= ['0-18','19-29','30-39','40-49','50-59','60-69','70-79'])


new_df = df.groupby(['Agegroup']).sum().sort_values('Spending Score (1-100)',ascending=False)
#print (df['AgeGroup'])
#new_df = df.groupby(['AgeGroup'])
#print (new_df['AgeGroup'])
print (new_df['Spending Score (1-100)'][:1])
