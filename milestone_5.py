import random

class Hangman:  
    """
    This class is used to play a game of hangman

    Attributes:
    word_list (list): list of words from which the computer randomly selects one
    num_lives (int): the user starts with five lives
    """
    def __init__(self, word_list, num_lives=5):  
        """
        Initialises the attributes of the class (see class docstring for word_list and num_lives)

        Attributes:
        word (str): The word to be guessed, picked randomly from the word_list
        word_guessed (str): A list of the letters of the word, with _ for each letter not yet guessed
        num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet
        list_of_guesses (list): A list of the guesses that have already been tried. 
        """

        self.word_list = word_list  
        self.num_lives = num_lives 
        self.word = random.choice(word_list) 
        self.word_guessed = ["_"] * len(self.word) 
        self.num_letters = len(set(self.word))  
        self.list_of_guesses = [] 

    def check_guess(self, guess):
        """
        This method is used to check the user's guess.

        It converts the guess into lower case. 
        Uses an if statement, to run through each character of the word, if the character is in the word.
        Replacec the "_" with the letter in the correct positions and prints a message.
        Reduces the number of letter to be guessed by one.
        If the character is not in the word, it prints a message a reduces number of lives by 1.
        """

        guess = guess.lower() 
        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.") 
            for index, character in enumerate(self.word):
                if character == guess:  
                    self.word_guessed[index] = character
                    print(self.word_guessed)
        
            self.num_letters = self.num_letters - 1
            print(f"Number of letters left is {self.num_letters}")

        else:
            self.num_lives = self.num_lives -1
            print(f"Sorry, {guess} is not in the word. Try again.") 
            print(f"You have {self.num_lives} lives left.")
            
    def ask_for_input(self):
        """
        This method is used to take a single alphabetic character as input from the user.

        It takes the character as input from the user.
        Checks if it is alphabetic, a single character and hasn't already been guessed.
        If so, the while loop is broken and the character is passed to the check_guess method.
        """
        guess = input("Please enter a single letter: ") 
        while True:
            if not guess.isalpha() or len(guess) != 1:   
                print("Invalid letter. Please, enter a single alphabetical character.") 
            elif guess in self.list_of_guesses:  
                print("You already tried that letter!")
                break
            else:
                self.list_of_guesses.append(guess) 
                self.check_guess(guess)  
                break 


def play_game(word_list, num_lives=5):
    """
    This method is used to carry out the playing of a hangman game

    game is created as an instance of the Hangman class. 
    A while loop is created to continue game play whilst there are still unique letters in the word to be guessed, or the user has remaining lives. 
    If no lives are remaining, the loop is exited and a message is printed revealing that the player has lost.
    If no unique letters are remaining, the loop is exited and a message is printed revealing that the player has won.
    """
    game = Hangman(word_list)
    while True:
        guess = game.ask_for_input()
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            return 
        elif game.num_letters == 0:
          print(f"Congratulations. You won the game! The word is {game.word}")
          return 
      

word_list = ["blueberry", "raspberry", "mango", "watermelon", "kiwi"]
play_game(word_list)