import pandas as pd
import numpy as np
df = pd.read_csv("student.csv")
df.loc[5, "math score"] = np.nan
df.loc[12, "math score"] = np.nan
df.loc[3, "gender"] = np.nan

print(df.isnull().sum())# to check the number of missing values in each column


df["gender"] = df["gender"].fillna("unknown")
mean_score = df["math score"].mean()
df["math score"] = df["math score"].fillna(mean_score)

print(df.isnull().sum()) 

# After filling, spot check the exact rows you changed
print(df.loc[[3, 5, 12], ["gender", "math score"]])