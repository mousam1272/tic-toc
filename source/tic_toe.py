class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

class Tic_tac_toe_base():

    def __init__(self):
        # Will hold our game board data
        self.player_one = "1st player"
        self.player_two = "2nd player"
        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]

        # Lets us know if the game is over yet
        self.game_still_going = True

        # Tells us who the winner is
        self.winner = None

        # Tells us who the current player is (1st player goes first)
        self.current_player = self.player_one

    # Play a game of tic tac toe
    def play_game(self):

        # Show the initial game board
        self.display_board()

        # Loop until the game stops (winner or tie)
        while self.game_still_going:

            # Handle a turn based on type of game
            self.handle_turn(self.current_player)

            # Check if the game is over
            self.check_if_game_over()

            # Flip to the other player
            if not self.winner:
                self.flip_player()
        
        # Since the game is over, print the winner or tie
        if self.winner:
            print(bcolors.OKGREEN + " " +self.current_player + " Won." + bcolors.ENDC)
        else:
            print(bcolors.WARNING + " TIE" + bcolors.ENDC)


    # Display the game board to the screen
    def display_board(self):
        print("\n")
        print("Game Status" + "      Reference Table")
        print(" " + self.board[0] + " | " + self.board[1] + " | " + self.board[2] + "          1 | 2 | 3")
        print(" " + self.board[3] + " | " + self.board[4] + " | " + self.board[5] + "          4 | 5 | 6")
        print(" " + self.board[6] + " | " + self.board[7] + " | " + self.board[8] + "          7 | 8 | 9")
        print("\n")


    # Handle a turn for an arbitrary player
    def handle_turn(self):
        pass


    # Check if the game is over
    def check_if_game_over(self):
        self.check_for_winner()
        self.check_for_tie()


    # Check to see if somebody has won
    def check_for_winner(self):
        # Check if there was a winner anywhere
        self.check_rows()
        self.check_columns()
        self.check_diagonals()
 
    def check_rows(self):
        pass

    # Check the columns for a win
    def check_columns(self):
        pass

    # Check the diagonals for a win
    def check_diagonals(self):
        pass


    # Check if there is a tie
    def check_for_tie(self):
        # If board is full
        if "-" not in self.board:
            self.game_still_going = False
            self.winner = False
            return True

    # Flip the current player from X to O, or O to X
    def flip_player(self):
        self.current_player = self.player_one if self.current_player == self.player_two else self.player_two





