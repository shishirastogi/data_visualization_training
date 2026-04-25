n = int(input("Enter a number: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print("Factorial of", n, "is", factorial)