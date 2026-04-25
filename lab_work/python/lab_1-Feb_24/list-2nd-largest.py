user_input = input("Enter list elements separated by space: ")
numbers = list(map(int, user_input.split()))
numbers = list(set(numbers))
if len(numbers) < 2:
    print("Second largest element does not exist.")
else:
    largest = numbers[0]
    second_largest = float('-inf')  # Very small number
    for num in numbers:
        if num > largest:
            largest = num
    for num in numbers:
        if num != largest and num > second_largest:
            second_largest = num
    print("Second largest element is:", second_largest)