def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    if (b == 0):
        print("ERROR: Cannot devide by 0")
        b = float(input("Enter another number: "))
    return a / b
    