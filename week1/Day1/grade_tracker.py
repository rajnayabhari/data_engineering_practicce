name=input("Enter the name of the student:")
score=int(input("Enter the score of the student:"))
student={"name":name,"score":score}
if student["score"]>=90:
    print(f"{student['name']} has an A grade.")
elif student["score"]>=80:
    print(f"{student['name']} has a B grade.")
elif student["score"]>=70:
    print(f"{student['name']} has a C grade.")
elif student["score"]>=60:
    print(f"{student['name']} has a D grade.")
else:    
    print(f"{student['name']} has an F grade.")