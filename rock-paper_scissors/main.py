from Winner import determineWinner

def main():
    
    print("Welcome in rock, paper, scissors game!")
    
    # Call the function to determine the winner and store the result
    result = determineWinner()
    # Print the result of the game
    print(result)

if __name__ == "__main__":
    # Execute the main function when the script is run
    main()