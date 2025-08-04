import pandas as pd 
data = pd.read_csv("nba.csv", index_col="Name")
check = data["Age"].isin([27.0]) #checking single value in a dataframe
print(check)

check_01 = data["Age"].isin([29.0])
check_02 = data["Team"].isin(["Boston", ])
print(data[check_01 & check_02])
