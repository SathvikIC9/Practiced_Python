import pandas as pd 
data = pd.read_csv("nba.csv")
data["Class"] =[1 for i in range(len(data))] 
print(data["Class"])