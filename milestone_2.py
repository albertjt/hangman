import random #import the random module

# Create a list containing the names of your 5 favorite fruits.
# Assign this list to a variable called word_list.
word_list = ["Blueberry", "Raspberry", "Mango", "Watermelon", "Kiwi"]

# Print out the newly created list to the standard output (screen).
print(word_list)

# Create the random.choice method and pass the word_list variable into the choice method.
# Assign the randomly generated word to a variable called word.
word = random.choice(word_list)

# Print out word to the standard output. Run the code several times and observe the words printed out after each run.
print(word)

# Using the input function, ask the user to enter a single letter.
# Assign the input to a variable called guess.
guess = input("Please enter a single letter: ")

# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    print("Good guess!") # print a message that says "Good guess!".
else:
    print("Oops! That is not a valid input") #Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.

