from functions import add, sub, div, mult
from user_input import user_input

def main():
    a, op, b = user_input()
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
    print("Result is : ", r)

if __name__ == "__main__":
    main()