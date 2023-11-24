def createBoard():
    # Setting the variables that will serve as the dimensions of the game board
    rows = 0
    columns = 0

    # Creating an empty board
    board = []

    #A While loop to ensure only numbers between 8 and 18 are valid, also validates that no letters are input.

    while rows <8 or rows>18:
        try:
            rows=int(input("Please select how many rows you want (Minimum of 8, Maximum of 18)"))
            if rows <8 or rows >18:
                print("Invalid Input, please enter a number between 8 and 18:")
        except ValueError:
            print("Invalid input. Please enter a number.")

    #A While loop to ensure only numbers between 6 and 12 are valid, also validates that no letters are input.

    while columns <6 or columns>12:
        try:
            columns=int(input("Please select how many columns you want (Minimum of 6, Maximum of 12)"))
            if columns <6 or columns >12:
                print("Invalid Input, please enter a number between 6 and 12:")
        except ValueError:
            print("Invalid input. Please enter a number.")


    # Fill the board with empty slots
    # We use space to represent an empty slot
    
    
    for _ in range(rows):
        row = [' '] * columns  # Create a row with 'columns'.
        board.append(row)

    return board

# Testing the function by creating a board and printing it
game_board = createBoard()
for row in game_board:
    print(row)


