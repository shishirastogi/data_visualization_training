serial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 6, 14, 15, 16, 8, 18, 19, 20]
number = int(input("Enter the number: "))

if number in serial:
    serial.reverse() 
    
    while serial.count(number) > 1:
        serial.remove(number) 

    serial.reverse() 
    print(serial)
else:
    print("Not found")