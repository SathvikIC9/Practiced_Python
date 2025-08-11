import pandas as pd 
data = pd.read_csv("nba.csv", )
summary = data.describe()
print(summary)# complete summary of the file

name_summary = data["Name"].describe()
print(name_summary)# summary of a single column

complete = data.describe(include = 'all')
print(complete)