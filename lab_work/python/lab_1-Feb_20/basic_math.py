def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if y == 0:
        return "Error: Division by zero"
    return x / y
if __name__ == "__main__":
    x,y = (5, 10)
    print(f'Addition: {add(x,y)}')
    print(f'Subtraction: {sub(x,y)}')
    print(f'Multiplication: {mul(x,y)}')
    print(f'Division: {int(div(x,y))}')
