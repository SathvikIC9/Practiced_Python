import pandas as pd
import numpy as np

# --Using Series--
ser = pd.Series()
print("Pandas Series: ", ser) # printing a blank sequence
data = np.array([1,2,3,4,5])

ser = pd.Series(data)
print("Pandas Series: \n ", ser) # printing our own sequnence
#printing a specific value in a series
print(ser[0])

# giving own indexing
ser = pd.Series(data, index = ["x", "y", "z", "a", "b"])
print("Pandas Series: \n ", ser)