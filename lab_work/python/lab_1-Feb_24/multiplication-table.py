num = int(input("Enter a number to print its multiplication table: "))
i = 1
print("Multiplication Table of", num)
while i <= 10:
    result = num * i
    print(num, "x", i, "=", result)
    i += 1