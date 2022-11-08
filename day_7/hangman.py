# simple hangman game in python3
# hangman will be drawn after four wrong inputs from the user

import random
# list of words to be guessed
from hangman_word_list import word_list

# function to draw hangman
def draw_hangman(num):
    hangman = [' o','/|\\', ' |', '/ \\']
    for i in range(num):
        print(hangman[i])


# word to be guessed
word_to_guess = list(random.choice(word_list))
guess_len = len(word_to_guess)

# "empty" list to be filled with user's correct guesses
new_guess = []
for i in range(guess_len):
    new_guess += "_"

###########################
###### START OF GAME ######
print("GAME OF HANGMAN\n")
print(f"Pssst. The correct word is {''.join(word_to_guess)}")
print(' '.join(new_guess))

# hold number of wrong guesses
wrong_choices = 0
# to hold correct guesses
guessed_letters = []

while wrong_choices < 4 and new_guess != word_to_guess:
    user_guess = input("Enter your guess> ").lower()
    true_char = False

    for j in range(guess_len):

        # check and know the index in word to guess, 
        # if user's guess is in original word to guess
        if word_to_guess[j] == user_guess:
            true_char = True
            # put correct guess at corresponding index in new_guess
            new_guess[j] = user_guess
            
    # add correct guess to guessed list
    if user_guess in guessed_letters:
        print(f"You already guessed {user_guess}, try another letter.\n")
    else:
        guessed_letters.append(user_guess)
   
    # for incorrect guesses
    if true_char == False:
        wrong_choices += 1
        print(f"You guessed '{user_guess}', that's not in the chosen word. You lose a life.")
    draw_hangman(wrong_choices)
    print(' '.join(new_guess))

    # check if user won the game
    if new_guess == word_to_guess:
        print("You win!")
    # check if user lost the game
    if wrong_choices == 4:
        print("You lost the game!")

