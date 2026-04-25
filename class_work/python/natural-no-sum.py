n = int(input("Enter a number N: "))
if n <= 0:
    print("Please enter a positive number.")
else:
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    print("Sum of first", n, "natural numbers is:", total_sum)