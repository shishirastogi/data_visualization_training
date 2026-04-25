data = {"A": 85, "B": 92, "C": 78, "D": 95}
max_key = max(data, key=data.get)
print("Key with maximum value:", max_key)
print("Maximum value:", data[max_key])