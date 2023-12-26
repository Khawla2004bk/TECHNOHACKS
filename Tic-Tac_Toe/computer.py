# Contains functions related to computer player moves
import random

def computer_move(b):
    # Generate a random move for the computer player
    empty = [(row, col) for row in range(3) for col in range(3) if b[row][col] == " "]
    return random.choice(empty)
