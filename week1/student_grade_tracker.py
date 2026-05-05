# Student Grade Tracker
# Your job: complete the three functions below

students = {
    "Raj":   {"score": 92, "city": "Kathmandu"},
    "Sita":  {"score": 74, "city": "Pokhara"},
    "Shyam": {"score": 55, "city": "Biratnagar"},
    "Priya": {"score": 88, "city": "Butwal"},
    "Anil":  {"score": 61, "city": "Birgunj"},
}

# Function 1: return the grade letter for a score
def get_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"

# Function 2: return the name of the top scoring student
def find_top_student(students):
    top_student = None
    top_score = -1
    for name, info in students.items():
        if info["score"] > top_score:
            top_score = info["score"]
            top_student = name
    return top_student
# Function 3: return the class average score (round to 2 decimals)
def class_average(students):
    total_score=0
    for name, info in students.items():
        total_score += info["score"]
    return round(total_score / len(students), 2)

# --- Report ---
print("===== STUDENT GRADE REPORT =====")
for name, info in students.items():
    grade = get_grade(info["score"])
    print(f"{name}  |   Score={info['score']},| City={info['city']},| Grade={grade}")
    # print each student's name, score, city and grade

top = find_top_student(students)
avg = class_average(students)
print(f"Top student: {top}")
print(f"Class average score: {avg}")
# print the top student and class average