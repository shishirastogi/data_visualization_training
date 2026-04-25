n = int(input("Enter a number N: "))
i = 1
sum_even = 0
while i <= n:
    if i % 2 == 0:
        sum_even += i
    i += 1
print("Sum of even numbers up to", n, "is:", sum_even)