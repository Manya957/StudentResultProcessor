# Student Result Processor

print("===== STUDENT RESULT PROCESSOR =====")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

sub1 = float(input("Enter marks in English: "))
sub2 = float(input("Enter marks in Mathematics: "))
sub3 = float(input("Enter marks in Science: "))
sub4 = float(input("Enter marks in Computer: "))
sub5 = float(input("Enter marks in Hindi: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("\n===== STUDENT REPORT CARD =====")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Total Marks  :", total, "/500")
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("Result       :", result)
