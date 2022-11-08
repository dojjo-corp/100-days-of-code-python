# This is the same higher lower game but done with loops instead of recursion
# The logic still remains the same
# two random accounts get printed, and the user asked to guess the one with the most followers on instagram

# make the necessary imports
import random
from os import system
from art import logo, vs
from accounts import accounts

# function to compare accounts
def compare_accounts(acc_A, acc_B):
    if acc_A["follower_count"] > acc_B["follower_count"]:
        return "A"
    else:
        return "B"

# function to generate random accounts
def rand_account():
    return random.choice(accounts)

# function to clear screen
def cls():
    system('clear')

# flag to control loop flow
should_continue = True

# count number of correct answers
count = 0

# generate random accounts
acc_A = rand_account()
acc_B = rand_account()

while should_continue:
    cls()
    print(logo)
    print("Welcome to the HIGHER-LOWER GAME!")
    print("\nChoose the instagram account with the most followers")
    print(f'Current Score: {count}\n')

    print(f'Account A: {acc_A["name"]}, {acc_A["description"]} from {acc_A["country"]}')
    print(f'Psst. This accont has {acc_A["follower_count"]}M followers.')
    print(vs)
    print(f'Account B: {acc_B["name"]}, {acc_B["description"]} from {acc_B["country"]}')
    print(f'Psst. This accont has {acc_B["follower_count"]}M followers.')

    # take user's guess
    user_guess = input("Make your choice (A/B): ").upper()
    if user_guess != compare_accounts(acc_A, acc_B):
        should_continue = False
        print("You Lost!")
        print(f"Final Score: {count}")
    else:
        count += 1
        acc_A = acc_B
        acc_B = rand_account()