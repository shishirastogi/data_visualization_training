num = int(input("Enter a number: "))
original = num
if num < 0:
    print("Negative numbers cannot be Armstrong numbers.")
else:
    temp = num
    count = 0
    while temp > 0:
        temp = temp // 10
        count += 1
    if original == 0:
        count = 1
    temp = num
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** count
        temp = temp // 10
    if armstrong_sum == original:
        print(original, "is an Armstrong number.")
    else:
        print(original, "is NOT an Armstrong number.")