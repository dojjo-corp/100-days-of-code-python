import random
import os
from functions import get_value, sum_of_cards

print("WELCOME TO DOJJO'S BLACKJACK GAME!")
if input("Type 'start' to begin game\n>> ").lower() == "start":
    round_no = 0
    limit_reached = False
    card_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


    # to hold card names for user
    user_cards = []
    # to hold actual values associated with cards
    user_values = []
    
    # same for dealer
    dealer_cards = []

    # same for dealer
    dealer_values = []

    # start game with two random cards dealt to both sides
    for i in range(2):
        # generate a random card for user and append to user's card list
        user_cards.append(random.choice(card_list).lower())
        user_values.append(get_value(user_cards[i], side="user"))

        # do same for dealer in first round
        dealer_cards.append(random.choice(card_list).lower())
        dealer_values.append(get_value(dealer_cards[i], side="dealer"))
    

    # to keep track of the number of cards dealt so far (two card already dealt in first rond)
    round_no = 1
    while limit_reached == False:
        # increase round number to corresponf to number of cards dealt
        round_no += 1
        
        # check if limit is reached
        if sum_of_cards(user_values)>= 21 or sum_of_cards(dealer_values) >= 21:
            limit_reached = True
            break
        
        print("Your cards:", user_cards)
        print("Card values:", user_values)
        print("Your total:", sum_of_cards(user_values))
        print("\nComputer's first card:", dealer_cards[0])

        # prompt to continue or not
        to_continue = input("\nEnter 'y' to hit again, or 'n' to pass: ")
        if to_continue == 'y':
            # generate random card for user again
            user_cards.append(random.choice(card_list).lower())
            user_values.append(get_value(user_cards[round_no], side="user"))

            # do same for dealer
            dealer_cards.append(random.choice(card_list).lower())
            dealer_values.append(get_value(dealer_cards[round_no], side="dealer"))
        
        elif to_continue == "n":
            limit_reached = True

    user_sum = sum_of_cards(user_values)
    dealer_sum = sum_of_cards(dealer_values)
    print("Your final hand:", user_cards, "\nSum:", user_sum)
    print("computer's final hand:", dealer_cards, "\nSum:", dealer_sum)
    
    # check win/lose conditions
    # when sum total is within boundaries
    if max(user_sum, dealer_sum) <= 21:
        if max(user_sum, dealer_sum) == user_sum:
            print("You win!")
        else:
            print("Dealer Wins!")

    # when sum total of cards is greater than 21
    else:
        if max(user_sum, dealer_sum) == user_sum:
            print("Busted!")
            print("Dealer Wins!")
        else:
            print("Dealer Busted!")
            print("You win!")

# for wrong start command input
else:
    print("We both know that's not how to write 'start'...")
