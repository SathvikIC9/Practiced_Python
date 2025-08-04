import pandas as pd 
data = pd.read_csv("nba.csv", index_col="Name")
top_5 = data.head(5)
print(top_5)# prints the top 5 rows from the file

bottom_5 = data.tail(5)
print(bottom_5) # prints the bottom 5 rows from the file 

value = data.at["Avery Bradley","Age"]
print("\n",value)

result = data.query("Age > 25 and College == 'Duke'" )
print(result)