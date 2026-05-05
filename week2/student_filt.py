import pandas as pd
df = pd.read_csv("student.csv")
# print(df.columns)
# Step 2 — math above 80 only
math_df = df[df["math score"] > 80]
print(math_df.shape[0])

# Step 3 — completed prep course only
prep_df = df[df["test preparation course"] == "completed"]
print(prep_df.shape[0])

# Step 4 — both combined
both_df = df[(df["math score"] > 80) & (df["test preparation course"] == "completed")]
print(both_df.shape[0])