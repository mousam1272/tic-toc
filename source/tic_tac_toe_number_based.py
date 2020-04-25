

# --------- Global Variables -----------

# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
current_player = "1st player"


# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():

  # Show the initial game board
  display_board()

  # Loop until the game stops (winner or tie)
  while game_still_going:

    # Handle a turn
    handle_turn(current_player)

    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    if not winner:
      flip_player()
  
  # Since the game is over, print the winner or tie
  if winner:
    print(current_player + " won.")
  else:
    print("Tie.")


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")
  number = input("Choose a number from 2-8: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] \
     and number not in ["2", "3", "4", "5", "6", "7", "8"]:
      position = input("Choose a position from 1-9: ")
      number = input("Choose a number from 2-8: ")
    # Get correct index in our board list
    position = int(position) - 1
    number = int(number)

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position] = str(number)

  # Show the game board
  display_board()


# Check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Check to see if somebody has won
def check_for_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner or column_winner or diagonal_winner:
    winner = True
  else:
    winner = False


# Check the rows for a win
def check_rows():
  # Set global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = row_2 = row_3 = False
  if "-" not in (board[0], board[1], board[2]):
    row_1 = (int(board[0])+ int(board[1])+ int(board[2])) >= 15
  if "-" not in (board[3], board[4], board[5]):
    row_2 =(int(board[3])+ int(board[4])+ int(board[5])) >= 15
  if "-" not in (board[6], board[7], board[8]):
     row_3 = (int(board[6])+ int(board[7])+ int(board[8])) >= 15
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
    winner = True
    return True
  else:
    return False


# Check the columns for a win
def check_columns():
  # Set global variables
  global game_still_going
  column_1 = column_2 = column_3 = False
  # Check if any of the columns have all the same value (and is not empty)
  if "-" not in (board[0], board[3], board[6]):
    column_1 = (int(board[0])+ int(board[3])+ int(board[6])) >= 15
  if "-" not in (board[1], board[4], board[7]):
    column_2 = (int(board[1])+ int(board[4])+ int(board[7])) >= 15
  if "-" not in (board[2], board[5], board[8]):
    column_3 = (int(board[2])+ int(board[5])+ int(board[8])) >= 15
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
    winner = True
    return True
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_still_going
  diagonal_1 = diagonal_2 = False
  # Check if any of the columns have all the same value (and is not empty)
  if "-" not in (board[2], board[4], board[6]):
    diagonal_1 = (int(board[2])+ int(board[4])+ int(board[6])) >= 15 
  if "-" not in (board[0], board[4], board[8]):
    diagonal_1 = (int(board[0])+ int(board[4])+ int(board[8])) >= 15

  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
    winner = True
    return True
  else:
    return False


# Check if there is a tie
def check_for_tie():
  # Set global variables
  global game_still_going
  # If board is full
  if "-" not in board:
    game_still_going = False
    return True
  # Else there is no tie
  else:
    return False


# Flip the current player from X to O, or O to X
def flip_player():
  # Global variables we need
  global current_player
  # If the current player was X, make it O
  if current_player == "1st player":
    current_player = "2nd player"
  # Or if the current player was O, make it X
  elif current_player == "2nd player":
    current_player = "1st player"


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()
