def char_frequency(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq

text = input("Enter a string : ")
result = char_frequency(text)
print(result)