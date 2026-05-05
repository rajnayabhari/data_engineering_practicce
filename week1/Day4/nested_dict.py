classroom={
    "raj":{"score":90,"city":"ktm"},
    "sita":{"score":95,"city":"bkt"},
    "gita":{"score":85,"city":"pkr"},
}

# to access value in nested dict
print(classroom["raj"]["score"])

# to loop through each and every student
for name,info in classroom.items():
    print(f"{name} scored {info['score']} from {info['city']}")
