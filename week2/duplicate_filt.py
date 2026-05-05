import pandas as pd
df = pd.read_csv("student.csv")
# add duplicate data to make data look messy
duplicate_rows = df.iloc[0:3]
# adds 3 duplicate rows to the dataframe
df = pd.concat([df,duplicate_rows], ignore_index = True)
print(df.shape) #it should show 1003
df = df.drop_duplicates()
print(df.shape) #it should show 1000