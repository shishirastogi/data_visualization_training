def find_gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = find_gcd(num1, num2)
print("GCD is:", result)