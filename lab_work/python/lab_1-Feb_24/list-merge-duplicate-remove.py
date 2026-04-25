list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))
merged_list = list1 + list2
unique_list = []
for item in merged_list:
    if item not in unique_list:
        unique_list.append(item)
print("Merged list without duplicates:", unique_list)