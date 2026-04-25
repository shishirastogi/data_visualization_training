income=float(input("Enter your annual income: "))
age=int(input("Enter your age: "))
tax=0
if age >= 60:
    exemption_limit=300000
else:
    exemption_limit=250000
if income <= exemption_limit:
    tax=0
elif income <= 500000:
    tax = (income - exemption_limit) * 0.05
elif income <= 1000000:
    tax = (500000 - exemption_limit) * 0.05 + (income - 500000) * 0.2
else:
    tax = (500000 - exemption_limit) * 0.05 + 500000 * 0.2 + (income - 1000000) * 0.3
print("Total Tax Payable: Rs ",tax)
