num = int(input("Enter a number: "))
num = abs(num)
if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        num = num // 10
        count += 1
print("Total number of digits:", count)