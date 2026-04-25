text = input("Enter a string: ")
text = text.lower()
if text == text[::-1]:
    print("String is a Palindrome.")
else:
    print("String is NOT a Palindrome.")