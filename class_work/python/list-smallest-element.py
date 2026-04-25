user_input = input("Enter list elements separated by space: ")
numbers = list(map(int, user_input.split()))
if len(numbers) == 0:
    print("List is empty.")
else:
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    print("Smallest element is:", smallest)