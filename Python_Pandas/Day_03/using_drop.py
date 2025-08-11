
import pandas as pd
data = pd.read_csv("nba.csv", index_col="Name")
remove = data.drop(["Age"],axis = 1,inplace= False )# gives out the new dataframe without the resp. column
remove = data.drop(["Age"],axis = 1,inplace= True )# gives out NONE as a result
print(remove)
remove_00 = data.drop(["Jae Crowder"],axis=0,inplace= False) 
print(remove_00)

#the AXIS indicates weather u want to remove a row or a column if its 1 then column and if its a row the its 0 


