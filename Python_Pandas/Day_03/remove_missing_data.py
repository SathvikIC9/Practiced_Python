import pandas as pd
data = pd.read_csv("nba.csv")
remove = data.dropna()
print(remove)# removes the data that has Nan labelled in it 

filling = data.fillna("Hello",inplace=False)
print(filling)#filling the data in the Nan solts 
