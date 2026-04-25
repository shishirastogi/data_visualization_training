user_input = input("Enter list elements separated by space: ")
numbers = list(map(int, user_input.split()))
if len(numbers) == 0:
    print("List is empty.")
else:
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print("Largest element is:", largest)
