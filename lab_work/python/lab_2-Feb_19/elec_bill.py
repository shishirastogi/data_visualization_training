units=float(input("Enter number of units consumed: "))
age=int(input("Enter your age: "))
bill=0
if units <= 100:
    bill=units * 5
elif units <= 300:
    bill=100 * 5 + (units - 100) * 7
else:
    bill=100 * 5 + 200 * 7 + (units - 300) * 10
if age >= 60:
    discount_v2=bill * 0.1
    bill=bill - discount_v2
    print("Senior citizen discount_v2 applied (10%)")
print("Total Electricity Bill: Rs ",bill)
