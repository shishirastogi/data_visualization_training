n = int(input("Enter number: "))

s = 0
digits = len(str(n))

for d in str(n):
    s += int(d) ** digits

if s == n:
    print("True")
else:
    print("False")