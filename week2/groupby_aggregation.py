import pandas as pd

df = pd.read_csv("student.csv")

# to find average math score by gender
# .round(2) is used to round the average score to 2 decimal places
avg_score_by_gender = df.groupby("gender")["math score"].mean().round(2)
print(avg_score_by_gender)

# to find average math score by test preparation course
avg_score_by_prep = df.groupby("test preparation course")["math score"].mean().round(2) 
print(avg_score_by_prep)

# to find average across all three score column grouped by parental level of education
avg_score_by_parent_edu = df.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean().round(2)
print(avg_score_by_parent_edu)