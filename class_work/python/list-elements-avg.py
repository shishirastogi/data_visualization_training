numbers = list(map(int, input("Enter list elements separated by space: ").split()))
if len(numbers) == 0:
    print("List is empty. Cannot calculate average.")
else:
    total_sum = 0
    for num in numbers:
        total_sum += num
    average = total_sum / len(numbers)
    print("Average of list elements is:", average)