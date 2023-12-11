def add(a, b):
    # Add two numbers
    return a + b

def mult(a, b):
    # Multiply two numbers
    return a * b

def sub(a, b):
    # Subtract the second number from the first
    return a - b

def div(a, b):
    # Divide the first number by the second (handle division by zero)
    if (b == 0):
        print("ERROR: Cannot devide by 0")
        b = float(input("Enter another number: "))
    return a / b