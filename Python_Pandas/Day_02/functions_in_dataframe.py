import pandas as pd

data = {
    "Name":['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    "Age":[23,26,23,24,28],
    "Gender":["Male","Female","Male","Female","Male"],
    "Job Role": ["Junior Developer", "Senior Developer", "Project Manager", "UI/UX Designer", "DevOps Engineer"]
}
df = pd.DataFrame(data)
print(df)







# now ... suppose you just want a single row or a column to be printed from a dataframe then ... we can use - 
age_column = df["Age"]
print(age_column)
row_01 = df.iloc[0] # used just for specific positional indexing
print(row_01)
double_rows = df.loc[0:2] # for multiple rows and columns to be mentioned 
print(double_rows)


# now if u want a filtered data for example ... printing age greater than 25 the we can use -
greater_than_25 = df[df["Age"]>25]
print(greater_than_25)

#  now if u want to know whose age will be at position 3 (index 2) in a specific column then we can use -
at_pos_2 = df.at[2, "Age"] 
print(at_pos_2)
