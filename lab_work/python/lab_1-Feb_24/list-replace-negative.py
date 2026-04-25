numbers = list(map(int, input("Enter list elements separated by space: ").split()))
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
print("Updated list:", numbers)