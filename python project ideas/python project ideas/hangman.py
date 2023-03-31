import random

# Define a list of words to choose from
word_list = ["python", "programming", "code", "algorithm"]

# Choose a random word from the list
secret_word = random.choice(word_list)

# Create a list to store the letters the user has guessed
guesses = []

# Set the number of turns the user has to guess the word
max_turns = 10

# Main game loop
while max_turns > 0:
    # Print the current status of the word (showing only correctly guessed letters)
    word_status = ""
    for letter in secret_word:
        if letter in guesses:
            word_status += letter
        else:
            word_status += "_"
    print(word_status)

    # Ask the user for their guess
    guess = input("Guess a letter: ")
    
    # Check if the guess is correct and add it to the list of guesses
    if guess in secret_word:
        print("Correct!")
        guesses.append(guess)
    else:
        print("Wrong!")
    
    # Decrement the number of turns remaining
    max_turns -= 1
    
    # Check if the user has guessed all the letters in the word
    if all(letter in guesses for letter in secret_word):
        print(f"Congratulations! You guessed the word '{secret_word}'")
        break

# If the user has used up all their turns without guessing the word, they lose
if max_turns == 0:
    print(f"Sorry, you have used up all your turns. The word was '{secret_word}'")
