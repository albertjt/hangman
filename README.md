# Hangman

### Table of Contents
* Project Description
* Installation Instructions
* Usage Instructions
* File Structure of the Project
* License Information



### Project Description 
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Within a class, following attribute initialisation, the check_guess method is defined. This checks if the guessed letter is indeed in the word randomly selected by the computer. If so, it adds it to the word_guessed variable; if not, you lose a life and try again.
The ask_for_input method takes in the letter guess, ensures it is a single alphabetic character, and passes it into the check_guess method.

While working on this project, I gained insights into Python's string manipulation, list operations, and control flow structures. Additionally, I improved my skills in handling user input, implementing game logic, and structuring a console-based application.

### Installation Instructions
Use the following link: https://github.com/albertjt/hangman.git

Clone repository using: 
git clone https://github.com/albertjt/hangman.git

Navigate to directory:
cd hangman

Run the game script:
python milestone_5

### Usage Instructions
Launch the game by running the script.
Enter a single letter when prompted.
Continue guessing letters until you either complete the word or run out of lives.
Enjoy the game and have fun!

### File Structure of the Project
This product has a simple file structure.

### License Information
This is licensed under the MIT license.