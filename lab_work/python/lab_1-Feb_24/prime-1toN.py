n = int(input("Enter a number N: "))
print("Prime numbers between 1 and", n, "are:")
num = 2
while num <= n:
    is_prime = True
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(num)
    num += 1