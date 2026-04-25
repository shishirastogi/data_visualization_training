keys = input("Enter keys separated by space: ").split()
values = list(map(int, input("Enter values separated by space: ").split()))
result = dict(zip(keys, values))
print("Created dictionary:", result)