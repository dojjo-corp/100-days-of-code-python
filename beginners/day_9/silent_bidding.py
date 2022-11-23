from os import system

last_bidder = False

total_bids = {}
highest_bid = 0
highest_bidder = ""
while last_bidder == False:
    bidder = input("What is your name?\n> ")
    bid = int(input("Enter your bid\n> $"))
    if bid > highest_bid:
        highest_bidder = bidder
        highest_bid = bid

    total_bids[bidder] = bid
    response = input("Are you the last bidder (yes/no)?\n> ")
    if response == "yes":
        last_bidder = True
    elif response == "no":
        system('clear')
print(total_bids)
print("The highest bidder is", highest_bidder)
print("Winning with a bid of $" + highest_bid)
