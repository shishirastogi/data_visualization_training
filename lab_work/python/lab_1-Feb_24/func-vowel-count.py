def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count
user_input = input("Enter a string: ")
result = count_vowels(user_input)
print("Number of vowels:", result)