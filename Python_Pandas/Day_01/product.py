import pandas as pd
ser1 = pd.Series([1,2,3], index=["a", "b" ,"c"])
ser2 = pd.Series([6,4,5], index=["a", "b" ,"c"])
adding = ser1.prod()
adding2 = ser2.prod()
print(adding)
print(adding2)