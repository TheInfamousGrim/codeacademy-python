from random import randint
# 1.

# Create a variable board and set it equal to an empty list.

board = []

# 2.

# Create a 5 x 5 grid initialized to all ‘O’s and store it in board.

#     Use range() to loop 5 times.
#     Inside the loop, .append() a list containing 5 "O"s to board, just like in the example above.

# Note that these are capital letter “O” and not zeros.

for i in range(5):
    board.append(["O"] * 5)

# 3.

# First, delete your existing print statement.

# Then, define a function named print_board with a single argument, board_in.

# Inside the function, write a for loop to iterates through each row in board and print it to the screen.

# Call your function with board to make sure it works.

# Create a for loop inside the print_board function to create visible rows

# Then use the .join function to create a seamless grid

def print_board(board_in):
    for row in board_in:
        print(" ".join(row))

# 4.

# Define two new functions, random_row and random_col, that each take board_in as input.

# These functions should return a random row index and a random column index from your board, respectively. Use randint(0, len(board_in) - 1).

# Call each function on board.

def random_row(board_in):
    return randint(0, len(board_in) - 1)

def random_col(board_id):
    return randint(0, len(board_id) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# 5.

# Create a new variable called guess_row and set it to int(raw_input("Guess Row: ")).

# Create a new variable called guess_col and set it to int(raw_input("Guess Col: ")).

# Click Run and then answer the prompts by typing in a number and pressing Enter (or Return on some computers)

# 666666.

# On line 29, add an if to check if guess_row equals ship_row and guess_col equals ship_col.

# If that is the case, please print out "Congratulations! You sank my battleship!"

# When you run this code, be sure to enter integer guesses in the panel where it asks for “Guess Row” and then “Guess Col”.

# 6.

# Add a new if statement that is nested under the else.

# Like the example above, it should check if guess_row is not in range(5) or guess_col is not in range(5).

# If that is the case, print out "Oops, that's not even in the ocean."

# After your new if statement, add an else that contains your existing handler for an incorrect guess. Don’t forget to indent the code!

# 7.

# Add an if statement that checks to see if the user is out of guesses.

#     Put it under the else that accounts for misses.
#     Put it after the if/elif/else statements that check for the reason the player missed. We want "Game Over" to print regardless of the reason.

# If turn equals 3, print "Game Over".




print(ship_row, ship_col)
print()

for turn in range(4):
    print(f"Turn {turn + 1}")
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) and guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_row] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)
    if turn == 3:
        print("GameOver")
    print()



    


