import pandas as pd
data = pd.read_csv("nba.csv", index_col="Name") # incrementing the name column as the index column 
print("Dataset")
print(data.head(5))

first = data["Age"] # selecting a single column from the dataset
print("\n Single column selected- ")
print(first.head(5))

second = data[["Age", "Height", "Weight"]]# selecting multiple columns from the dataset
print("\n Multiple columns selected- ")
print(second.head(5))