numbers = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
is_unique = True
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            is_unique = False
            break
    if not is_unique:
        break
if is_unique:
    print("All elements are unique.")
else:
    print("Tuple contains duplicate elements.")