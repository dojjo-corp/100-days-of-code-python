import random
from os import system
# list of instagram accounts in a dictionary (different file)
from accounts import accounts
from art import logo, vs

# function to compare two accounts
def compare_accounts(acc_A, acc_B):
    """Takes two account names and compares to find the one which the most followers"""
    if acc_A["follower_count"] > acc_B["follower_count"]:
        return "A"
    else: 
        return "B"

# hold number of correct choices
correct_counts = 0

# put game play in a function to be called again when needed
def game_play(acc_B, acc_A=random.choice(accounts)):
    '''Takes two arguments, but the first account (acc_A) is by default 
    given a random enty from the accounts list. '''
        
    # print("Welcome to the HIGHER-LOWER GAME!")
    print("Choose the account with the most followers on instagram.\n") 

    # display first account
    print(f'Account A: {acc_A["name"]}, {acc_A["description"]} from {acc_A["country"]}')
    print(f"This account has {acc_A['follower_count']}M followers")

    # display versus ascii art
    print(vs)

    # display second account
    print(f'Account B: {acc_B["name"]}, {acc_B["description"]} from {acc_B["country"]}')
    print(f'This account has {acc_B["follower_count"]}M followers')

    # prompt user for guess
    user_guess = input("Make your guess (A/B): ").upper()

    if user_guess == compare_accounts(acc_A, acc_B):
        # count number of right choices 
        global correct_counts
        correct_counts += 1

        # clear screen and start over
        system('clear')
        print(logo)
        print(f'Your current score: {correct_counts}')
        
        # call function again with second account as first account 
        # and find different random account for the second argument
        game_play(acc_A=acc_B, acc_B=random.choice(accounts))
    
    # option to quit game anytime
    elif user_guess.lower() == "quit":
        print(f'Final score: {correct_counts}')
        print("Game Ended!")
        return
    # wrong input
    else:
        system('clear')
        print(logo)
        print("Wrong Choice!")
        print(f"final score: {correct_counts}".upper())
        return

# display first account
system('clear')
print(logo)
game_play(acc_B = random.choice(accounts))

