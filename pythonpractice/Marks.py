m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

total = m1 + m2 + m3
avg = total / 3

print("Total Marks:", total)
print("Average:", avg)

if avg < 35:
    print("Result: Fail")
else:
    print("Result: Pass")

    if avg >= 90:
        print("Rank: 1st Rank")
    elif avg >= 75:
        print("Rank: 2nd Rank")
    elif avg >= 60:
        print("Rank: 3rd Rank")
