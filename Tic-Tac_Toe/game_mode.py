#Implement Game Mode Selection
def choose_mode():
    # Allow the user to choose the game mode
    print("Choose the game mode:")
    print("1. Play against the computer")
    print("2. Play between two players")
    
    mode = input("Enter 1 or 2: ")
    
    if mode == "1":
        return "computer"
    elif mode == "2":
        return "two_players"
    else:
        print("Invalid choice. Defaulting to two players.")
        return "two_players"
    