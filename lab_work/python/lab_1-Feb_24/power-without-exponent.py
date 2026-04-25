base = int(input("Enter base number: "))
exponent = int(input("Enter exponent: "))
result = 1
if exponent < 0:
    exponent = abs(exponent)
    for i in range(exponent):
        result *= base
    result = 1 / result
else:
    for i in range(exponent):
        result *= base
print("Result:", result)