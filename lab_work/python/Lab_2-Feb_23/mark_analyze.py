marks = [80, 90, 70, 101, 60, 50, 40, 30, 20, 10, 0]

valid_marks = [x for x in marks if 0 <= x <= 100]
avg = sum(valid_marks) / len(valid_marks)
topper = max(valid_marks)

print(f"Valid Marks: {valid_marks}")
print(f"Average: {avg:.2f}")
print(f"Topper: {topper}")

if avg >= 90:
    grade = "O"
elif avg >= 80:
    grade = "A+"
elif avg >= 70:
    grade = "A"
elif avg >= 60:
    grade = "B"
elif avg >= 50:
    grade = "C"
elif avg >= 40:
    grade = "D"
else:
    grade = "F"

print(f"Final Grade: {grade}")

# for m in valid_marks:
#     if m >= 90:
#         grade = "O"
#     elif m >= 80:
#         grade = "A+"
#     elif m >= 70:
#         grade = "A"
#     elif m >= 60:
#         grade = "B"
#     elif m >= 50:
#         grade = "C"
#     elif m >= 40:
#         grade = "D"
#     else:
#         grade = "F"
#     print(f"Mark: {m}, Grade: {grade}")