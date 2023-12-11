from computer import computer_choice
from user import user_choice

def determineWinner():
    # Get computer and user choices
    computer = computer_choice()
    user = user_choice()
    
    # Print computer's choice
    print("Computer's choice is:", computer)
    
    # Compare choices and determine the winner
    if computer == user :
        return("It's a tie!")

    elif user == 'rock':
        if computer == 'paper':
            return("Computer WINS!")
        else :
            return("You WIN!")

    elif user == 'paper':
        if computer == 'scissors':
            return("Computer WINS!")
        else :
            return("You WIN!")

    elif user == 'scissors':
        if computer == 'rock':
            return("Computer WINS!")
        else :
            return("You WIN!")