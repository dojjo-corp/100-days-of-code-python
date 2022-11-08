import random
from art import logo

# Create function to compare guesses with actual answer
def compare_guess(user_guess, computer_guess):
    if user_guess < computer_guess:
        return -1
    elif user_guess > computer_guess:
        return 1
    else:
        return 0

# computer guesses a number between 1 and 100
computer_guess = random.choice(range(101))
print(logo)
print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100. Can you take a guess as to what that number can be?") 
print(f"Pssst. The correct answer is {computer_guess}")

# create difficulty levels
difficulty = {
        "easy": 10, 
        "hard": 5,
        }
level = input("Choose your difficulty level ('easy' or 'hard'): ")

# create boolean flag to track right answers
is_right = False

# loop till flag gets changed to True or lives runs out
attempts_left = difficulty[level]
while is_right == False:
    print(f"Attempts left: {attempts_left}")
    
    # check if number of attempts have ran out. Decrease attempts if not
    if attempts_left == 0:
        print("Sorry, you ran out of attempts.")
        print(f"The correct answer is {computer_guess}")
        break
    else:
        attempts_left -= 1

    # take and compare user's guess with actual answer
    user_guess = int(input("Make a guess: "))
    compare_ans = compare_guess(user_guess, computer_guess)
    if compare_ans == 0:
        is_right = True
        print(f"Nice! {computer_guess} was the correct answer \nYou win!\n")
    elif compare_ans == -1:
        print("Too low.\n")
    else:
        print("Too high.\n")
