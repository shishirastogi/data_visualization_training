a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b and b == c:
        print("It is an Equilateral Triangle.")
    elif a == b or b == c or a == c:
        print("It is an Isosceles Triangle.")
    else:
        print("It is a Scalene Triangle.")
else:
    print("The given sides do NOT form a valid triangle.")