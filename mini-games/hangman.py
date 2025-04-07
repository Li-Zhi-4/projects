from wonderwords import RandomWord
import string

class Hangman:
    def __init__(self):
        self.__word = "default"
        self.__guesses = []
        self.__guesses_counter = 0
        self.__hangman = {
            1: " ",     # O (head)
            2: " ",     # | (body)
            3: " ",     # / (left arm)
            4: " ",     # \\ (right arm)
            5: " ",     # / (left leg)
            6: " "      # \\ (right leg)
        }
        self.__secret_word = []
        self.__scoreboard = {
            "Wins": 0,
            "Losses": 0
        }

    def generate_word(self, min: int, max: int) -> str:
        """Generates a random word between a specified length."""
        r = RandomWord()
        self.__word = r.word(word_min_length=min, word_max_length=max)
        self.__secret_word = ["_" for letter in self.__word]                # List comprehension: setting _ for every letter in self.__word
    
    def print_board(self):
        """Prints the hangman board."""
        print("  ______")
        print(" |      |")
        print(f" |      {self.__hangman[1]}")
        print(f" |     {self.__hangman[3]}{self.__hangman[2]}{self.__hangman[4]}")
        print(f" |     {self.__hangman[5]} {self.__hangman[6]}")
        print(" |")
        print(f"_|_    {"".join(self.__secret_word)}\tGuesses: {" ".join(self.__guesses)}")

    def print_scoreboard(self):
        """Prints the current scoreboard."""
        print(f"\nScoreboard:\n" \
        f"Player Wins: {self.__scoreboard["Wins"]}\n" \
        f"Player Losses: {self.__scoreboard["Losses"]}\n")

    def update_hangman(self):
        """Updates the hangman visual depending on the number of guesses."""
        body = ["O", "|", "/", "\\", "/", "\\"]
        self.__hangman[self.__guesses_counter] = body[self.__guesses_counter-1]       # Updates the hangman body after every addition to guesses

    def update_secret_word(self):
        """Updates the secret word to reveal all correct guessed letters."""
        for i in range(len(self.__word)):
            if self.__word[i] in self.__guesses:
                self.__secret_word[i] = self.__word[i]

    def guess_letter(self, guess: str):
        """Takes a guess and updates the hangman board."""
        self.__guesses.append(guess)
        if guess in self.__word:                                    # If the letter is in the word, update secret word
            self.update_secret_word()
            if ("".join(self.__secret_word) == self.__word):        # Check if the word has been completely guessed
                    return True
        else:                                                       # Otherwise, add to the hangman
            self.__guesses_counter += 1
            self.update_hangman()
            if (self.__guesses_counter >= 6):                       # Check if the number of incorrect guesses exceeds limit
                    return False
        
    def guess_word(self, guess: str):
        """Checks if the guess word matches the actual word."""
        if guess == self.__word:
            return True
        else:
            return False


    def take_guess(self):
        """Takes input guess and checks for invalid input before updating board."""
        guess = input("Guess a letter or word: ").lower()
        for i in guess: 
            if (i not in string.ascii_lowercase):
                print(f"Error: {guess} is not a letter or word.")
                return -1
        if guess in self.__guesses:
            print(f"Error: {guess} has already been guessed.")
            return -1

        if len(guess) > 1:                              # If the guess was a word
            return self.guess_word(guess)
        else:                                           # Otherwise, the guess is a letter
            return self.guess_letter(guess)
                

    def play_game(self, min: int, max: int):
        """Plays a full game of hangman."""
        self.generate_word(min,max)                 # Generates word
        self.print_board()

        while True:                                 # Loops through repeated guessing until win or loss
            check = self.take_guess()
            if check == -1:
                continue
            elif check == True:
                print("Congrats, you won!")
                self.__scoreboard["Wins"] += 1
                break
            elif check == False:
                print("Wrong guess, you lose!")
                self.__scoreboard["Losses"] += 1
                break
            else:
                self.print_board()

    def print_options(self):
        """Prints hangman gameplay options."""
        print("\nHangman options:\n" \
            "(1) Play game.\n" \
            "(2) Display scoreboard.\n" \
            "(3) Display options.\n" \
            "(4) Exit.\n")

    def hangman(self):
        """Sets up Hangman."""
        self.print_options()
        
        while True:
            choice = input("Select one of the options: ")
            match(choice):
                case "1":
                    self.play_game(5,10)
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
    hangman = Hangman()
    hangman.hangman()
