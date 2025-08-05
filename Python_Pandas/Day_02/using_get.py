import pandas as pd 
data = pd.read_csv("nba.csv", index_col="Name")
read_cols = data.get("Age")# getting a single column 
print(read_cols)

multi_cols = data.get(["Age","Salary","Height"])
print(multi_cols)# getting multiple columns 

