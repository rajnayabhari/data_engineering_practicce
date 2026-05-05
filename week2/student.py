import pandas as pd

df = pd.read_csv("/home/raj/Learning/python/student.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.columns)