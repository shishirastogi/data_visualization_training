set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))
result = set1.difference(set2)
print("Difference (set1 - set2):", result)