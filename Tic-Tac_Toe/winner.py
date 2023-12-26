# Contains the function to check for a winner
def winner(b):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != " ":
            return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != " ":
            return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] != " ":
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != " ":
        return b[0][2]
    # Return None if no winner is found
    return None
