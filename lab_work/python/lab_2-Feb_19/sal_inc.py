rating=int(input("Enter performance rating (1-5): "))
experience=int(input("Enter years of experience: "))
attendance=float(input("Enter attendance percentage: "))
increment=0
if rating == 5:
    increment=15
elif rating == 4:
    increment=10
elif rating == 3:
    increment=7
elif rating == 2:
    increment=3
else:
    increment=0
if experience >= 10:
    increment += 5
elif experience >= 5:
    increment += 3
if attendance >= 95:
    increment += 2
elif attendance >= 85:
    increment += 1
print("Total Increment Percentage:",increment, "%")
