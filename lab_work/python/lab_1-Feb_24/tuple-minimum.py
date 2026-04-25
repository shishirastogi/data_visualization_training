numbers = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
if len(numbers) == 0:
    print("Tuple is empty.")
else:
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    print("Minimum value:", minimum)