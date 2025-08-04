'''
A dataframe is a data structure that has data involved in it using rows and columns ... 
and the data in that frame can be retrived by referring the name/title of the column /row and 
it will print the data within the row and column.

'''
import pandas as pd

data = {
    "Name":['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    "Age":[23,26,23,24,28],
    "Gender":["Male","Female","Male","Female","Male"],
    "Job Role": ["Junior Developer", "Senior Developer", "Project Manager", "UI/UX Designer", "DevOps Engineer"]
}
df = pd.DataFrame(data)
print(df)
# this is how u can create a dataframe 




