ch = input("Enter a single alphabet: ")
if len(ch) != 1:
    print("Please enter only one character.")
elif not ch.isalpha():
    print("Entered character is not an alphabet.")
elif ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("It is a Vowel.")
else:
    print("It is a Consonant.")