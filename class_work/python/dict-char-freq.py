text = input("Enter a string: ")
frequency = {}  # Empty dictionary
for ch in text:
    if ch in frequency:
        frequency[ch] += 1  # Increase count
    else:
        frequency[ch] = 1   # Add new character
for key, value in frequency.items():
    print(key, ":", value)