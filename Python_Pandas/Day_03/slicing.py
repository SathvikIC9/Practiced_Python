import pandas as pd 
data = pd.read_csv("nba.csv", index_col="Name")



# selecting few rows from the dataframe from 0 to n-1

df_01 = data.iloc[0:4]
# print(df_01)

#selecting few columns from the dataframe from 0 to n-1 without effecting the number of rows

df_02 = data.iloc[:,0:2]
# print(df_02)

#selecting a few columns and the rows from the dataframe from 0 to n-1 

df_03 = data.iloc[0:2,0:2]
# print(df_03)


# slicing using boolean functions
df_04 = data[(data["Age"]>25)&(data["Team"]=="Boston")].iloc[:,:]
print(df_04)

