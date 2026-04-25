user_input = input("Enter list elements separated by space: ")
numbers = list(map(int, user_input.split()))
visited = []
for num in numbers:
    if num not in visited:
        count = 0
        for item in numbers:
            if item == num:
                count += 1
        print(num, "appears", count, "times")
        visited.append(num)