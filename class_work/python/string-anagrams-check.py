str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()
str1 = str1.replace(" ", "")
str2 = str2.replace(" ", "")
if sorted(str1) == sorted(str2):
    print("Strings are Anagrams.")
else:
    print("Strings are NOT Anagrams.")