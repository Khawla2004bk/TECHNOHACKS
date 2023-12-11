from computer import computer_choice
def user_choice():
    # List of valid choices
    available_choices = ['rock','paper','scissors']
    
    # Allow the user up to 3 attempts to enter a valid choice
    for i in range(3):
        choice = input("Enter your choice: ")
        
        if choice.lower() in available_choices:
            # Return the lowercase version of the valid choice
            return choice.lower()
        else:
            print("Invalid choice. Please choose between \"rock\", \"paper\", or \"scissors\".")
    
    print("You lose. Too many invalid attempts.")
    