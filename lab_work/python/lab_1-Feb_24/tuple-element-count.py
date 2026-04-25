numbers = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
element = int(input("Enter element to count: "))
count = 0
for num in numbers:
    if num == element:
        count += 1
print("Element", element, "appears", count, "times")