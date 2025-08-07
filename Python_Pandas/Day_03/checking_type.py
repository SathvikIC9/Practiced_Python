import pandas as pd 
data = pd.read_csv("nba.csv")
diff = type(data["Age"])
print(diff)
diff = type(data)
print(diff)