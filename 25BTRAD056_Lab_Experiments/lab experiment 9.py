students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    students[name] = [marks, grade]

print("\n--- STUDENT RESULTS ---")

for name, result in students.items():
    print("Name:", name)
    print("Marks:", result[0])
    print("Grade:", result[1])
    print()
