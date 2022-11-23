#Don't change the code below
print("Welcome to Python's Pizza Delivery Services!")
print()
size = input("What size of pizza do you want? S, M, L> ").lower()
add_pepperoni = input("Would you like to add pepperoni? Y/N> ").lower()
add_cheese = input("Would you like extra cheese to go with it as well? Y/N> ").lower()
bill = 0

#Write your code below this line

#bill for different sizes
if size == "s":
    bill = 15
    #with pepperoni
    if add_pepperoni == "y":
        bill += 2
elif size == "m":
    bill = 20
    #with pepperoni
    if add_pepperoni == "y":
        bill += 3
elif size == "l":
    bill = 25
    #with pepperoni
    if add_pepperoni =="y":
        bill += 3

#bill for extra cheese for all sizes
if add_cheese == "y":
    bill += 1

print("Your final bill is $" + str(bill))
