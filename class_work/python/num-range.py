num = float(input("Enter the number to check: "))
lower = float(input("Enter lower limit of range: "))
upper = float(input("Enter upper limit of range: "))
if lower > upper:
    print("Invalid range entered.")
elif lower <= num <= upper:
    print("The number lies within the range.")
else:
    print("The number does NOT lie within the range.")