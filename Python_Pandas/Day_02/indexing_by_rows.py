import pandas as pd
data = pd.read_csv("nba.csv", index_col="Name")
row = data.loc['Jonas Jerebko']# used to print a particular row
print(row)

multi_rows = data.loc[["Jonas Jerebko", "Amir Johnson"]]
print(multi_rows)  # used to print multiple rows at the same time

specific_row = data.iloc[3]
print(specific_row) # used to print the row at a particular index 


specific_row = data.iloc[[3,5,6]]
print(specific_row) # used to print the multiple rows with particular index 


