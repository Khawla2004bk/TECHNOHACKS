# Rock, Paper, Scissors Game

## Overview

This is a simple console-based rock, paper, scissors game implemented in Python. The game allows the user to enter their choice (rock, paper, or scissors), generates a random choice for the computer, and then determines the winner based on the game rules.

## Files

- `user.py`: Contains the function `user_choice()` that prompts the user for input and returns their choice. It interacts with the `computer.py` module.

- `computer.py`: Contains the function `computer_choice()` that generates a random choice for the computer.

- `winner.py`: Combines the user and computer choices, determines the winner, and prints the result.

- `main.py`: The main script that welcomes the user and calls the `determineWinner()` function to start the game.

## Usage

1. Run `main.py` to start the game.
2. Enter your choice when prompted.
3. The computer will randomly choose its move.
4. The game will determine the winner and display the result.

## Example

```bash
Welcome to the rock, paper, scissors game!
Enter your choice: rock
Computer's choice is: paper
Computer WINS!
