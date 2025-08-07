import pandas as pd 
data = pd.read_csv("nba.csv")
print(len(data["Age"]))