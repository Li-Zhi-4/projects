class TicTacToe:

    def __init__(self):
        self.__board = {
            "A1": " ", "A2": " ", "A3": " ",
            "B1": " ", "B2": " ", "B3": " ",
            "C1": " ", "C2": " ", "C3": " "
        }
        self.__scoreboard = {
            "X": 0,
            "O": 0
        }


    def print_board(self):
        """Prints the current state of the tic-tac-toe board."""
        print(f"   1  2  3 \n" +
              f"A [{self.__board["A1"]}][{self.__board["A2"]}][{self.__board["A3"]}]\n" +
              f"B [{self.__board["B1"]}][{self.__board["B2"]}][{self.__board["B3"]}]\n" +
              f"C [{self.__board["C1"]}][{self.__board["C2"]}][{self.__board["C3"]}]")


    def take_turn(self, player):
        """User takes a turn and updates tic-tac-toe board."""
        turn = input(f"Player {player} takes turn: ")
        if (turn in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]):
            self.__board[turn] = player
            return True
        else:
            print(f"Error: {turn} is not a valid move.")
            return False


    def check_board(self):
        """Checks every winning combination and updates scoreboard when appropriate."""
        if (self.__board["A1"] + self.__board["A2"] + self.__board["A3"] == "XXX" or
            self.__board["B1"] + self.__board["B2"] + self.__board["B3"] == "XXX" or
            self.__board["C1"] + self.__board["C2"] + self.__board["C3"] == "XXX" or
            self.__board["A1"] + self.__board["B1"] + self.__board["C1"] == "XXX" or
            self.__board["A2"] + self.__board["B2"] + self.__board["C2"] == "XXX" or
            self.__board["A3"] + self.__board["B3"] + self.__board["C3"] == "XXX" or
            self.__board["A1"] + self.__board["B2"] + self.__board["C3"] == "XXX" or
            self.__board["A3"] + self.__board["B2"] + self.__board["C1"] == "XXX"):
            self.__scoreboard["X"] += 1
            print("Player X wins!")
            return 0

        if (self.__board["A1"] + self.__board["A2"] + self.__board["A3"] == "OOO" or
            self.__board["B1"] + self.__board["B2"] + self.__board["B3"] == "OOO" or
            self.__board["C1"] + self.__board["C2"] + self.__board["C3"] == "OOO" or
            self.__board["A1"] + self.__board["B1"] + self.__board["C1"] == "OOO" or
            self.__board["A2"] + self.__board["B2"] + self.__board["C2"] == "OOO" or
            self.__board["A3"] + self.__board["B3"] + self.__board["C3"] == "OOO" or
            self.__board["A1"] + self.__board["B2"] + self.__board["C3"] == "OOO" or
            self.__board["A3"] + self.__board["B2"] + self.__board["C1"] == "OOO"):
            self.__scoreboard["O"] += 1
            print("Player O wins!")
            return 0
        
        return 1


    def reset_board(self):
        """Resets the tic-tac-toe board."""
        for key in self.__board.keys():
            self.__board[key] = " "

    def print_scoreboard(self):
        """Prints the current scoreboard."""
        print(f"\nScoreboard:\n" \
        f"Player X Wins: {self.__scoreboard["X"]}\n" \
        f"Player O Wins: {self.__scoreboard["O"]}\n")


    def play_game(self):
        """Plays a game of tic-tac-toe to completion."""
        game.print_board()
        turn = "X"

        while True:
            if (turn == "X"):
                if (game.take_turn("X") == True):
                    turn = "O"
            else:
                if (game.take_turn("O") == True):
                    turn = "X"
            game.print_board()
            if (game.check_board() == 0):
                break
        
        print("Game Over!")
        self.reset_board()

    
    def print_options(self):
        """Prints the options for-tic-tac toe."""
        print("\nTic Tac Toe options:\n" \
            "(1) Play game.\n" \
            "(2) Display scoreboard.\n" \
            "(3) Display options.\n" \
            "(4) Exit.\n")

    
    def tic_tac_toe(self):
        """Sets up Tic Tac Toe."""
        self.print_options()
        
        while True:
            choice = input("Select one of the options: ")
            match(choice):
                case "1":
                    self.play_game()
                    self.print_options()
                case "2": 
                    self.print_scoreboard()
                case "3":
                    self.print_options()
                case "4":
                    break
                case _:
                    print(f"Error: {choice} is not one of the options.")


if __name__ == "__main__":
    game = TicTacToe()
    game.tic_tac_toe()