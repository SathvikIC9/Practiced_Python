import pandas as pd 
data = pd.read_csv("nba.csv")
data["Age"] = data["Age"].astype(object)
print(data.info())