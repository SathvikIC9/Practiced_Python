import pandas as pd  
 
df = pd.read_csv("Day_01/nba.csv")  
   
ser = pd.Series(df['Name']) 
data = ser.head(10)
print(data)