# Contains functions related to the game board
def initializeB():
    # Initialize an empty 3x3 board
    return [[" "]*3 for i in range(3)]
    
def printB(b, computermove=None):
    # Print the initial board state
    for row in b:
        print(" |".join(row))
        print("--------")

def update(b, row, col, move):
    # Update the board with the player's move
    b[row][col] = move

def full(b):
    # Check if the board is full
    return all(cell != " " for row in b for cell in row)
