text = input("Enter a string: ")
text = text.lower()
vowel_count = 0
for ch in text:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1
print("Number of vowels:", vowel_count)