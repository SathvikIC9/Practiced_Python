import pandas as pd 
data = pd.read_csv("nba.csv" , index_col="Name")
selection = data.iloc[[3,4],[1,2]]
print(selection)# used to select particular rows and columns 

# specific_value = data.loc[["Age"],['Amir Johnson']]
# print(specific_value)

allR_col = data.iloc[:, [1,2]]
print(allR_col)# prints all the rows with specific number of columns

