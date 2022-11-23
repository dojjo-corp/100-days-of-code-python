print("Welcome to the rollercoster!")
height = int(input("What is your height please? "))

#check height against criteria given
if height >= 120:
    print("You can ride the rollercoster!\n")
    age = int(input("How old are you please? "))
    if age < 12:
        print("Please pay $5 for the ticket")
    elif age <= 18:
        print("Please pay $7 for the ticket")
    else:
        print("Please pay $12 for the ticket")
    print("\nEnjoy the ride! Make sure not to fall")
else:
    print("Sorry, you have to grow a little taller to ride the rollercoster.")
