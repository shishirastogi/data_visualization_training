numbers = list(map(int, input("Enter list elements separated by space: ").split()))
total_sum = 0
for num in numbers:
    total_sum += num
print("Sum of list elements is:", total_sum)