# The main script that orchestrates the Tic Tac Toe game

# Import functions from different modules
from board import initializeB, printB, update, full
from computer import computer_move
from game_mode import choose_mode
from user import player_move, switch_player
from winner import winner

def play():
    # Initialize the Tic Tac Toe board
    b = initializeB()
    # Start the game with 'O' player
    player = "O"
    # Choose the game mode
    game_mode = choose_mode()

    while True:
        # Print the current state of the board
        printB(b)

        # Get the next move based on the game mode and current player
        if game_mode == "computer" and player == "X":
            row, col = computer_move(b)
        else:
            row, col = player_move()

        # Check if the selected cell is already taken
        if b[row][col] != " ":
            print("Cell already taken. Try again.")
            continue
        
        # Update the board with the current player's move
        update(b, row, col, player)

        # Check if there's a winner
        win = winner(b)
        if win:
            print(f"Player {win} Wins!")
            return

        # Check if the board is full, resulting in a tie
        if full(b):
            print("It's a tie!")
            break

        player = switch_player(player)

if __name__ == "__main__":
    # Start the game when the script is run
    play()