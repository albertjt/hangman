import random

class Hangman:  # Create a class called Hangman.
    def __init__(self, word_list, num_lives=5):   # Inside the class, create an __init__ method to initialise the attributes of the class.
        self.word_list = word_list  # A list of words
        self.num_lives = num_lives  # The number of lives the player has at the start of the game.
        self.word = random.choice(word_list) # The word to be guessed, picked randomly from the word_list
        self.word_guessed = ["_"] * len(self.word)  # A list of the letters of the word, with _ for each letter not yet guessed
        self.num_letters = len(set(self.word))  # The number of UNIQUE letters in the word that have not been guessed yet
        self.list_of_guesses = []  # A list of the guesses that have already been tried. 

    def check_guess(self, guess):
        guess = guess.lower() # Convert the guess into lower case.
        if guess in self.word.lower():   # Create an if statement that checks if the guess is in the word, and make sure word is in lower case.
            print(f"Good guess! {guess} is in the word.") # In the body of the if statement, print a message saying "Good guess! {guess} is in the word.".
            for index, character in enumerate(self.word):  # loop through every index and character in the word, so that multiple similar characters are treaed individually.
                if character == guess:  # if the character is equal to the guess do...
                    word_guessed[index] = character # replace the _ in word_guessed at the correct index, with the character
        
            self.num_letters = self.num_letters - 1 # reduce number of remaining unique letters by 1

        else:
            self.num_lives = self.num_lives -1
            print(f"Sorry, {guess} is not in the word. Try again.") # Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again."
            print(f"You have {self.num_lives} lives left.")
            
    def ask_for_input(self):
        guess = input("Please enter a single letter: ") # Ask the user to guess a letter and assign this to a variable called guess.
        while True:
            if not guess.isalpha() or len(guess) != 1:   # Check if the guess is not a single alphabetical character. Hint: You can use Python's isalpha method to check if the guess is alphabetical.
                print("Invalid letter. Please, enter a single alphabetical character.") # If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."
            elif guess in self.list_of_guesses:  # Create an elif statement that checks if the guess is already in the list_of_guesses
                print("You already tried that letter!")  
            else:
                self.list_of_guesses.append(guess)  # append the guess to the list_of_guesses
                self.check_guess(guess)  # call the check_guess method
                break # break out of loop after a valid break


hangman_game = Hangman(["apple", "banana", "orange"])
hangman_game.ask_for_input()


