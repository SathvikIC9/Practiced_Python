import pandas as pd
data = pd.read_csv("nba.csv")
renamed = data.rename(columns={"TIME":"Age"},inplace=True)
print(renamed)