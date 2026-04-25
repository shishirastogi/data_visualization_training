user_input = input("Enter list elements separated by space: ")
numbers = list(map(int, user_input.split()))
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print("List after removing duplicates:", unique_list)