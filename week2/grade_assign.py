import pandas as pd

df = pd.read_csv("student.csv")

def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
df["grade"] = df["math score"].apply(assign_grade)
print(df)
print(df[["math score", "grade"]].head(10))
print(df["grade"].value_counts())