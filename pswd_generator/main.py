import random , string

def main():

    # Get the desired password length from the user
    while True:
        try:
            len = int(input("Enter the desired password length: "))
            if len > 0:
                break
            else:
                print("Enter a positive integer.")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Define the initial set of characters (letters and digits)
    chars = string.ascii_letters + string.digits
    
    # Ask the user whether to include punctuation in the password
    while True:
        choice = input("Do you want to include punctuation in the password? (yes/no): ").lower()
        
        if choice == 'yes':
            # Add punctuation to the character set if the user chooses 'yes'
            chars = chars + string.punctuation
            break
        
        elif choice == 'no':
            # No need to modify the character set if the user chooses 'no'
            break
        
        else:
            # Prompt the user until a valid choice is entered
            print("Invalid choice. Please enter 'yes' or 'no'.")
    
    # Generate the password using the specified length and character set
    pswd = ''.join(random.sample(chars, len))
    
    print(f"Generated Password is: {pswd}")

if __name__ == "__main__":
    main()