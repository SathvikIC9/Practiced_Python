import pandas as pd 
data = pd.read_csv("nba.csv")
id = data[["Age","Height"]]
print(id)