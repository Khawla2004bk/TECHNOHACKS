# Tic Tac Toe Game

## Introduction
This project is a simple implementation of the classic Tic Tac Toe game in Python. It supports two players playing against each other or playing against a computer opponent.

## Features
- Two game modes: Player vs Player, Player vs Computer.
- Intelligent computer opponent with random moves.
- Clean and modular code structure.

## Directory structure:
- Added `board.py` for board initialization and printing
- Added `computer.py` for computer opponent logic
- Added `game_mode.py` for game mode selection
- Added `user.py` for player moves and switching players
- Added `winner.py` for determining the game winner
- Updated `main.py` to orchestrate the game and handle user input

## Installation
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/your-username/tic-tac-toe.git
2. Navigate to the project directory
3. Run the game using 'python main.py'

## Usage
Choose the game mode and follow the prompts to make your moves. The game board will be displayed after each move. The game continues until there is a winner or it's a tie.

## Game Controls
### Player vs Player
In this mode, two players take turns entering their moves. The game prompts each player to enter the row and column for their move.

For Player vs Player mode:

Enter the row (0, 1, or 2) when prompted.
Enter the column (0, 1, or 2) when prompted.

### Player vs Computer
In this mode, you play against an intelligent computer opponent. The computer will automatically generate its moves based on a random strategy.

For Player vs Computer mode:

The computer will automatically generate its moves.