user_input = input("Enter list elements separated by space: ")
numbers = list(map(int, user_input.split()))
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
print("Sorted list:", numbers)