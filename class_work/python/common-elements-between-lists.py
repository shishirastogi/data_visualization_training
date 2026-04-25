list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))
common_elements = []
for item in list1:
    if item in list2 and item not in common_elements:
        common_elements.append(item)
print("Common elements:", common_elements)