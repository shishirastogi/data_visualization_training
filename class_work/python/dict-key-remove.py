data = {"a": 10, "b": 20, "c": 30}
key_to_remove = input("Enter key to remove: ")
removed_value = data.pop(key_to_remove, None)
if removed_value is None:
    print("Key not found.")
else:
    print("Removed key:", key_to_remove)
print("Updated dictionary:", data)