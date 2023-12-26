# Contains functions related to human player moves

def player_move():
    # Loop until valid input is provided
    while True:
        try:
            # Get user input for row and column
            row = int(input("Choose the row (0, 1, or 2): "))
            col = int(input("Choose the column (0, 1, or 2): "))
            
            # Check if the input is within the valid range
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a valid integer.")

def switch_player(player):
    # Switch the current player ('O' to 'X' and vice versa)
    if player == 'O':
        return 'X'
    else:
        return 'O'
    