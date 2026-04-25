def sum_of_digits(num):
    num = abs(num)
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("Sum of digits is:", result)