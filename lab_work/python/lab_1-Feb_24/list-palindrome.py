numbers = list(map(int, input("Enter list elements separated by space: ").split()))
reversed_list = numbers[::-1]
if numbers == reversed_list:
    print("The list is a Palindrome.")
else:
    print("The list is NOT a Palindrome.")