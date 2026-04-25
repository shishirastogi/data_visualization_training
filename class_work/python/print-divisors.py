num = int(input("Enter a number: "))
num = abs(num)
if num == 0:
    print("Every number divides 0. Divisors are undefined.")
else:
    print("Divisors of", num, "are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)