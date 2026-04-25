numbers = list(map(int, input("Enter list elements separated by space: ").split()))
even_list = []
odd_list = []
for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)