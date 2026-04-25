total_sum = 0
print("Enter numbers (Enter 0 to stop):")
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    total_sum += num
print("Total sum is:", total_sum)