ch = input("Enter a single character: ")
if len(ch) != 1:
    print("Please enter only one character.")
elif ch.isalpha():
    print("It is an Alphabet.")
elif ch.isdigit():
    print("It is a Digit.")
else:
    print("It is a Special Character.")