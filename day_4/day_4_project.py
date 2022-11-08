#rock paper scissors game
import random

rock = '''

'''

paper = '''

'''

scissors = '''

'''

#write your code below this line

# possible choices for the "computer"
possible_choices = ["rock", "paper", "scissors"]

# get user input
user_input = input("rock, paper, scissors\n> ").upper()
print(f"You chose: {user_input}")

# generate random choice for the computer
computer_choice = random.choice(possible_choices)
print(f"Computer chose: {computer_choice.upper()}")

# applying the rules for rock paper scissors

if user_input == "ROCK":
    if computer_choice == "scissors":
        print("You win!")
    elif computer_choice == "rock":
        print("It's a draw")
    else:
        print("You lose")

elif user_input == "PAPER":
    if computer_choice == "rock":
        print("You win!")
    elif computer_choice == "paper":
        print("It's a draw")
    else:
        print("You lose!")

elif user_input == "SCISSORS":
    if computer_choice == "paper":
        print("You win!")
    elif computer_choice == "scissors":
        print("It's a draw")
    else:
        print("You lose!")

else:
    print("Wrong Input!")