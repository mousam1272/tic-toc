

class Tic_tac_toe_pattern(Tic_tac_toe_base):

    def __init__(self):
      Tic_tac_toe_base.__init__(self):
      self.pattern = {"1st player": 'X', "2nd player":'0'}

    # Handle a turn for an arbitrary player
    def handle_turn(self, player):

      # Get position from player
      print(player + "'s turn.")
      position = int(input("Choose a valid position from 1-9: "))
      while (position not in range(1,10)) and (board[position] == "-"):
        position = int(input("Choose a valid position from 1-9: "))
  
      # Get correct index in our board list
      position = position - 1
      # Put the game piece on the board
      self.board[position] = self.pattern[player]
      # Show the game board
      self.display_board()

    # Check the rows for a win
    def check_rows(self):

      # Check if any of the rows have all the same value (and is not empty)
      row_1 = self.board[0] == self.board[1] == self.board[2] != "-"
      row_2 = self.board[3] == self.board[4] == self.board[5] != "-"
      row_3 = self.board[6] == self.board[7] == self.board[8] != "-"
      # If any row does have a match, flag that there is a win
      if row_1 or row_2 or row_3:
        self.game_still_going = False
        self.winner = True


    # Check the columns for a win
    def check_columns(self):

      # Check if any of the columns have all the same value (and is not empty)
      column_1 = self.board[0] == self.board[3] == self.board[6] != "-"
      column_2 = self.board[1] == self.board[4] == self.board[7] != "-"
      column_3 = self.board[2] == self.board[5] == self.board[8] != "-"
      # If any row does have a match, flag that there is a win
      if column_1 or column_2 or column_3:
        self.game_still_going = False
        self.winner = True

    # Check the diagonals for a win
    def check_diagonals(self):
      # Set global variables

      diagonal_1 = self.board[0] == self.board[4] == self.board[8] != "-"
      diagonal_2 = self.board[2] == self.board[4] == self.board[6] != "-"
      # If any row does have a match, flag that there is a win
      if diagonal_1 or diagonal_2:
        self.game_still_going = False
        self.winner = True

