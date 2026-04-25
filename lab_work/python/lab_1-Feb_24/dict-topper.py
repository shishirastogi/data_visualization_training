n = int(input("Enter number of students: "))
students = {}  # Create empty dictionary
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
topper = max(students, key=students.get)
print("Topper is:", topper)
print("Marks:", students[topper])