text = input("Enter a sentence: ")
words = text.split()   # Split sentence into words
result = ""
for word in words:
    result += word[0].upper() + word[1:].lower() + " "
print("Title Case:", result.strip())
