import random

word_list = ["Blueberry", "Raspberry", "Mango", "Watermelon", "Kiwi"]
word = random.choice(word_list)

# Define a function called check_guess. pass in the guess as a parameter for the function.
def check_guess(guess):
    guess = guess.lower() # Convert the guess into lower case.
    if guess in word:   # Create an if statement that checks if the guess is in the word.
        print(f"Good guess! {guess} is in the word.") # In the body of the if statement, print a message saying "Good guess! {guess} is in the word.".
    else:
        print(f"Sorry, {guess} is not in the word. Try again.") # Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again."
        

# Define a function called ask_for_input.
def ask_for_input():
    guess = input("Please enter a single letter: ") # Ask the user to guess a letter and assign this to a variable called guess.
    while True:
        if len(guess) == 1 and guess.isalpha():   # Check that the guess is a single alphabetical character. Hint: You can use Python's isalpha method to check if the guess is alphabetical.
            print("Good guess!") # print a message that says "Good guess!".
            break  # If the guess passes the checks, break out of the loop.
        else:
            print("Invalid letter. Please, enter a single alphabetical character.") # If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."
    check_guess(guess)   # call the check_guess function to check if the guess is in the word

ask_for_input()







