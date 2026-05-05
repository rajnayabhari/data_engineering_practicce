num=[11,22,33,44,55]
total=0
for i in num:

    if i%2==0:
        if i<30:
            print(i,"is even and less than 30")
        else:
            print(i,"is even and greater than 30")
    else:
        if i<30:
            print(i,"is odd and less than 30")
        else:
            print(i,"is odd and greater than 30")
    total+=i
print("The total is:",total)    