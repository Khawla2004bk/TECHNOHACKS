# Function that requests input from the user for the target currency, source currency, and amount to be converted.
def get_input():
    
    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError: # If the amount is invalid
        print("Invalid amount. Please enter a valid number.")
        return None    
    
    source_cur = input("Enter the source currency: ").upper()
    target_cur = input("Enter the target currency: ").upper()
    
    return amount, source_cur, target_cur
