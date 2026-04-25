weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))
if height <= 0:
    print("Invalid height entered.")
else:
    bmi = weight / (height ** 2)
    print("\nYour BMI is:", bmi)
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")