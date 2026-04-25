age=int(input("Enter patient's age: "))
heart_rate=int(input("Enter heart rate: "))
severe_injury=input("Is there a severe injury? (yes/no): ")
if heart_rate < 60 or heart_rate > 100 or severe_injury == "yes":
    print("Category: CRITICAL")
elif heart_rate >= 60 and heart_rate <= 100:
    category = "Moderate"
    if age > 65:
        print("Category: CRITICAL (Upgraded due to senior age)")
    else:
        print("Category: MODERATE")
else:
    print("Category: NORMAL")
