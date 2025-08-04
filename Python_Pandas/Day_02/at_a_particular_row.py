import pandas as pd
data = pd.read_csv("nba.csv", index_col="Name")
element = data.iat[2,3]#prints the element at the specified location
print(element)

remove = data.pop("Age")
print(remove)#removes the particular column and
print(data)# prints the new dataframe without the column 





