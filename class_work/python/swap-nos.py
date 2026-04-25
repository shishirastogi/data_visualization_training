a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("\nBefore Swapping:")
print("a =", a)
print("b =", b)
a = a + b
b = a - b
a = a - b
print("\nAfter Swapping:")
print("a =", a)
print("b =", b)