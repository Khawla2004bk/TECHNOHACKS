from functions import add, sub, div, mult
from user_input import user_input

def main():
    # Get user input for arithmetic operation and operands
    a, op, b = user_input()
    
    # Perform the selected arithmetic operation
    if (op == '+'):
        r = add(a, b)
    elif (op == '-'):
        r = sub(a, b)
    elif (op == '*'):
        r = mult(a, b)
    elif (op == '/'):
        r = div(a, b)
    else:
        print("Invalid operation")
    
    # Display the result
    print("Result is : ", r)

if __name__ == "__main__":
    main()