numbers = list(map(int, input("Enter list elements separated by space: ").split()))
k = int(input("Enter number of positions to rotate: "))
n = len(numbers)
k = k % n
rotated_list = numbers[-k:] + numbers[:-k]
print("Rotated list:", rotated_list)