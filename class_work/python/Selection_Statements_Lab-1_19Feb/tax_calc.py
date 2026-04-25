income=int(input("Enter the income: "))
age=int(input("Enter the age: "))
if age >= 60:
    exemption=300000
else:
    exemption=0
tax=0
if income <= exemption:
    tax=0
elif income <= 250000:
    tax=0
elif income > 250000 and income <= 500000:
    tax = (income - exemption) * 0.05
elif income > 500000 and income <= 1000000:
    tax = (income - exemption) * 0.05
    tax += (income - 500000) * 0.2
elif income > 1000000:
    tax = (income - exemption) * 0.05
    tax += (1000000 - 500000) * 0.2
    tax += (income - 1000000) * 0.3
print("Income tax to be paid is Rupees : ",tax)
