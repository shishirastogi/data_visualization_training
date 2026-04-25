def second_largest(lst):
    if len(lst) < 2:
        return None  

    largest = second_largest = float('-inf')

    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None


# Example
data = [10, 20, 4, 45, 97, 99]
print(second_largest(data))