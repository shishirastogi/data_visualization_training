text = input("Enter a string: ")
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
print("Reversed string:", reversed_text)