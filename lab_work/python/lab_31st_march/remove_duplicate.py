lst = list(map(int, input("Enter numbers: ").split(',')))
result = []
for item in lst:
    if item not in result:
        result.append(item)
print(result)