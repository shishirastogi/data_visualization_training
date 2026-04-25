data = {"name": "Amit", "age": 22, "city": "Delhi"}
key = input("Enter key to check: ")
if key in data:
    print("Key exists in dictionary.")
else:
    print("Key does NOT exist.")