import pandas as pd

# A dataframe = a table built from a list of dicts 
# Each dict = one row, each key = a column name

data = [
    {"name": "Raj", "age": 23, "score": 92, "city": "Kathmandu"},
    {"name": "Sita", "age": 25, "score": 74, "city": "Pokhara"},
    {"name": "Shyam", "age": 22, "score": 55, "city": "Biratnagar"},
    {"name": "Priya", "age": 24, "score": 88, "city": "Butwal"},
    {"name": "Anil", "age": 26, "score": 61, "city": "Birgunj"},
]

df = pd.DataFrame(data)
print(df)
print(df["score"]) # to acess only one column data
print(df.shape) # to know the number of rows and columns in dataframe
print(df.dtypes) # to know the data types of each column