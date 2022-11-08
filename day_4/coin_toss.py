import random

print("Welcome to the Coin Toss Game")

#to check if user quits
isQuit = False

while isQuit == False:
    response = input('Enter "Toss" to start the game\n> ').lower()
    print("\n*************")

    #to quit game anytime
    if response == "quit":
        isQuit = True

    #to start game
    if response == "toss":
        #generate random number 
        random_num = random.randint(1, 10)
        if random_num%2 == 0:
            print("You got Heads")
        else:
            print("You got Tails")
        
        #go another round
        response = input("\nWold you like to try again? (y/n)> ")
        if response == "y":
            isQuit=False
        elif response == "n":
            isQuit = True
            print("Enjoy the rest of your boring day!")
        
        #end game if input is wrong, i hate nonsense.
        else:
            isQuit = True
            print("Just type the correct thing for once in your life! smh.")

    else: 
        print("Wrong Entry!")
        print("Try Again")
