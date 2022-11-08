import random

def sum_of_cards(cards):
    sum = 0
    for i in cards:
        sum += int(i)
    return sum

def get_value(cards, side):

    values = 0
    if cards == 'jack' or cards == 'queen' or cards == 'king':
            values = 10
    elif cards =="ace": 
        if side == "user":
            ace_value = int(input("You got an ace, choose the value you want (1/11): "))
            values = ace_value
        elif side == "dealer":
            ace_value = random.choice([1, 11])
            values= ace_value
    else:
        values = int(cards)
    return values

