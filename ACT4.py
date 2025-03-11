grade = int(input("Indicate your grade:"))

if grade > 100 or grade < 0:
    print("Invalid score! Please enter a value between 0 and 100")
elif grade >= 90:
    print("GRADE: A")
elif grade >= 80:
    print("GRADE: B")
elif grade >= 70:
    print("GRADE: C")
elif grade >= 60:
    print("GRADE: D")
else:
    print("GRADE: F")
