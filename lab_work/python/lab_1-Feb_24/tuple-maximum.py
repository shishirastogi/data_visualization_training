numbers = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
if len(numbers) == 0:
    print("Tuple is empty.")
else:
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    print("Maximum value:", maximum)