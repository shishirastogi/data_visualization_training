rating=int(input("Enter performance rating (1-5): "))
experience=int(input("Enter years of experience: "))
attendance=float(input("Enter attendance percentage: "))
increment=0
if attendance < 75:
    increment=0
    print("No increment due to low attendance.")
else:
    if rating == 5:
        increment=20
    elif rating == 4:
        increment=15
    elif rating == 3:
        increment=10
    else:
        increment=0
    if experience >= 5:
        increment += 5
    if attendance >= 90:
        increment += 5
    print("Increment Percentage:",increment, "%")
