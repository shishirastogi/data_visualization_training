def get_unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
user_input = input("Enter list elements separated by space: ")
numbers = list(map(int, user_input.split()))
result = get_unique_elements(numbers)
print("Unique elements:", result)