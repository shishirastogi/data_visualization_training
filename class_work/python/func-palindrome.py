def is_palindrome(text):
    text = text.lower()
    reversed_text = ""
    for ch in text:
        reversed_text = ch + reversed_text
    if text == reversed_text:
        return True
    else:
        return False
user_input = input("Enter a string: ")
result = is_palindrome(user_input)
if result:
    print("The string is a Palindrome.")
else:
    print("The string is NOT a Palindrome.")