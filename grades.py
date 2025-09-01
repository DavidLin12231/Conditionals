gpa = float(input("Enter student's GPA: "))
if gpa > 3.75:
    print("High honor roll")
elif 3.25 <= gpa <= 3.75:
    print("Honor roll")
elif 3.00 <= gpa < 3.25:
    print("Good job")
elif 2.00 <= gpa < 3:
    print("Still passing")
else:
    print("Academic Concern!")
