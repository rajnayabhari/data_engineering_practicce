import pandas as pd
df = pd.read_csv("student.csv")

# to remove n/a data from dataframe
df = df.dropna()

# to remove duplicates from dataframe
df = df.drop_duplicates()

# to save the cleaned data to a new csv file
df = df[["gender", "math score", "test preparation course"]]
df.to_csv("cleaned_student.csv", index=False)
# When you save a DataFrame, Pandas tries to save the row numbers (0, 1, 2...) as an extra column called index. With index=False you tell it not to — otherwise your CSV gets an ugly unnamed first column full of row numbers that wasn't in your original data.

# Confirm save worked
df_check = pd.read_csv("cleaned_student.csv")
print(df_check.shape)
print(df_check.head())