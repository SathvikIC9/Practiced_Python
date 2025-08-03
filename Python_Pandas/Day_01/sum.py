import pandas as pd
ser1 = pd.Series([1,2,3], index=["a", "b" ,"c"])
ser2 = pd.Series([6,4,5], index=["a", "b" ,"c"])
adding1 = ser1.sum()
adding2 = ser2.sum()
print(adding1)
print(adding2)
# this is used to add the elements in the list