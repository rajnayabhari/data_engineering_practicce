import pandas as pd # we imported pandas library as pd so that it is easier to call and use

df = pd.read_csv("student.csv") #we load csv file to dataset for cleaning and visualization

print(df.columns) # we check colmn names

df.columns = df.columns.str.replace(" ","_") #we replace space with underscore so that it looks uniform
print(df.columns) #we check updated column name

def assign_grade(score): #this function assign grade accoriding to the total_score of student
    if score >= 270:
        return "A"
    elif score >= 225:
        return "B"
    elif score >= 180:
        return "C"
    else:
        return "F"
    

def is_passed(total_score): #this function checks if the student has obatined over passing marks or not
    return total_score >= 180


df["total_score"] = df["math_score"] + df["reading_score"] + df["writing_score"] # we add multiple column_values to obatin total score
print(df[["total_score", "writing_score", "reading_score", "math_score"]]) # we print and check if the total is correcr or not

df["grade"] = df["total_score"].apply(assign_grade) #we use the apply function to call our function to assign grade based on total score
print(df[["grade", "total_score"]]) # we check if the assigned grade is corret with the toatl marks or not

df["passed"] = df["total_score"].apply(is_passed) # we check if the student is passed or not and add a new column called passed
print(df[["total_score","passed"]])

average_total_by_gender = df.groupby("gender")["total_score"].mean().round(2) # we find average marks obtaine with respect to the gender
print(average_total_by_gender)

avg_by_parent_level_of_education = df.groupby("parental_level_of_education")["total_score"].mean().round(2)
print(avg_by_parent_level_of_education)

df = df.sort_values(by = 'total_score', ascending=False) #here we arrange the data in dataframe in descending order based on total marks so that we can see the top scorer
print(df.head(5)) #we print top 5 student based on top score

grade_count = df["grade"].value_counts() # we count how many student achieved what grade
print(grade_count)

print(df.shape) # we check the shape of data frame

df=df.dropna() # before preparing a cleaned csv we drop n/a data from dataset
df.to_csv("student_report.csv", index=False) # we export updated dataset with various table in to new csv file for further analysis

df_check = pd.read_csv("student_report.csv") # we load and check if the csv is correct or not
print(df_check.shape)