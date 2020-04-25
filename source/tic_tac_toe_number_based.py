############ Number based Tic Toe ################
from tic_toe import Tic_tac_toe_base, bcolors
class Tic_tac_toe_number_based(Tic_tac_toe_base):
    # Handle a turn for an arbitrary player
    def handle_turn(self, player):

      # Get position from player
      print(player + "'s turn.")
      position = int(input("Choose a position from 1-9: "))
      number = int(input("Choose a number from 2-8: "))

      # Whatever the user inputs, make sure it is a valid input, and the spot is open

      while ((position not in range(1,10)) or 
             (number not in range(2,9)) or 
             (self.board[position-1] != "-")):
        print(bcolors.WARNING + " Please Choose a valid position or Number" + bcolors.ENDC)
        position = int(input("Choose a position from 1-9: "))
        number = int(input("Choose a number from 2-8: "))

      # Put the game piece on the board
      self.board[position-1] = str(number)

      # Show the game board
      self.display_board()



    # Check the rows for a win
    def check_rows(self):

      # Check if any of the rows have sum greater then 15
      row_1 = row_2 = row_3 = False
      if "-" not in (self.board[0], self.board[1], self.board[2]):
        row_1 = (int(self.board[0])+ int(self.board[1])+ int(self.board[2])) >= 15
      if "-" not in (self.board[3], self.board[4], self.board[5]):
        row_2 =(int(self.board[3])+ int(self.board[4])+ int(self.board[5])) >= 15
      if "-" not in (self.board[6], self.board[7], self.board[8]):
        row_3 = (int(self.board[6])+ int(self.board[7])+ int(self.board[8])) >= 15
      # If any row does have a match, flag that there is a win
      if row_1 or row_2 or row_3:
        self.game_still_going = False
        self.winner = True



    # Check the columns for a win
    def check_columns(self):
      column_1 = column_2 = column_3 = None
      # Check if any of the columns have sum greater then 15
      if "-" not in (self.board[0], self.board[3], self.board[6]):
        column_1 = (int(self.board[0])+ int(self.board[3])+ int(self.board[6])) >= 15
      if "-" not in (self.board[1], self.board[4], self.board[7]):
        column_2 = (int(self.board[1])+ int(self.board[4])+ int(self.board[7])) >= 15
      if "-" not in (self.board[2], self.board[5], self.board[8]):
        column_3 = (int(self.board[2])+ int(self.board[5])+ int(self.board[8])) >= 15
      # If any row does have a match, flag that there is a win
      if column_1 or column_2 or column_3:
        self.game_still_going = False
        self.winner = True

    # Check the diagonals for a win
    def check_diagonals(self):
      diagonal_1 = diagonal_2 = None
      # Check if any of the columns have sum greater then 15
      if "-" not in (self.board[2], self.board[4], self.board[6]):
        diagonal_1 = (int(self.board[2])+ int(self.board[4])+ int(self.board[6])) >= 15 
      if "-" not in (self.board[0], self.board[4], self.board[8]):
        diagonal_1 = (int(self.board[0])+ int(self.board[4])+ int(self.board[8])) >= 15

      # If any row does have a match, flag that there is a win
      if diagonal_1 or diagonal_2:
        self.game_still_going = False
        self.winner = True



 
pattern_game = Tic_tac_toe_number_based()
pattern_game.play_game()