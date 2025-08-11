import pandas as pd 
data = pd.read_csv("nba.csv", index_col="Name")

data.set_index("Name", inplace=True)
custom = data.loc["Avery Bradley":"Amir Johnson"]
print(custom)