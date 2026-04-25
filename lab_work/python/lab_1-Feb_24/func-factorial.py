def factorial(n):
    if n < 0:
        return None  # Factorial not defined for negative numbers
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a number: "))
fact = factorial(num)
if fact is None:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", fact)