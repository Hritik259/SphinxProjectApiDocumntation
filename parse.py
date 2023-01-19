import pandas as pd
import csv

Documentation = pd.read_csv("./API Documentation - Drill.csv")
Documentation['Request Body'].fillna("NA",inplace=True)
Documentation['Sample successful Response'].fillna("NA",inplace=True)
df=Documentation
df.to_csv("./API Documentation - Drill.csv")
filename = open('./API Documentation - Drill.csv', 'r')
 
file = csv.DictReader(filename)
f1 = open(r'./docs/spamfilter.rst', 'w')
for row in file:
    with open(r'./docs/DEMO.txt', 'r') as file1:
        data = file1.read()
        ApiName = {'API_NAME':row['Sub resource/Action'],"API_METHOD":row['Method'],'API_URI':row['URL'],
        "API_DESCRIPTION":row['Description'],"API_REQUESTPARAMETER":row['Request Body'],"API_RESPONSE":row['Sample successful Response']}
        for key, value in ApiName.items():
            data = data.replace(key, value)
    with open(r'./docs/spamfilter.rst', 'a') as file2:
        file2.write("\n\n"+data+"\n")
lines = open("./docs/spamfilter.rst", 'r').readlines()
lines[0] = "User"+"\n"
lines[1] = "====================================="+"\n"
out = open("./docs/spamfilter.rst", 'w')
out.writelines(lines)
out.close()     