n = int(input("Enter number of terms: "))
if n <= 0:
    print("Please enter a positive number.")
else:
    first = 0
    second = 1
    print("Fibonacci Series:")
    for i in range(n):
        print(first)
        next_term = first + second
        first = second
        second = next_term