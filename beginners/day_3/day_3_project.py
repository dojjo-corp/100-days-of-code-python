def cls():
    from os import system
    system('clear')

cls()

print("Welcome to the Treasure Hunt Game!")
print("You have been tasked to search for the treasure in the forest of Agbalaagba.")
print("At the beginning of the forest. You see two paths leading to two differents directions.")
response = input("Make your choice. left or right?> ")
if response == "left":
    # pass
    cls()
    response = input('''This trail looks like it has been treaded on not long ago. You spot a cave. 
Look inside or move along? (look or move)> ''')
    if response == "look":
        cls()
        response = input('''You found the hideout of Agbalaagba! It seems to be asleep 
        but No treasuer in sight. Make your move. Kill it or burn the cave 
        (kill or burn)> 
        ''')

        if response == "kill":
            cls()
            response = input("What to do now? Leave and search for the treasure or Search in cave (leave or search)> ")
            if response == "search":
                # pass
                cls()
                print("YOU FOUND THE TREASURE IN THE BELLY OF AGBALAAGBA! CONGRATS!!!")
            # chose to leave and got lost in the way
            elif response == "leave":
                cls()
                print("You keep searching for the treasure, but get depressed and kill yourself. LEVEL FAILED!!!")
            else:
                cls()
                print("You really should pay attention to details in adventures. Enter the right thing for once in your life!")
        elif response == input("burn"):
            cls()
            print("You burnt down the only place the treasure could have been. YOU FAILED!!!")
        else:
            cls()
            print("In this life you realy have to follow instructions. Type the right thing for once")

    elif response == "move":
        cls()
        print('''Moving along the same path got you in the  midst of an unknown part of the forest. You're dead. LEVEL FAILED!!''')

    else:
        cls()
        print("The treaure is only for those who follow simple instructions. Get Out!")

elif response == "right":
    cls()
    response = input('''Looking ahead you find a genie with all fingers missing except his pinky. It seems to be pointing to the north.
    Follow in the direction or move along? (follow or move)> ''')
    if response == "follow":
        cls()
        response = input("The path leads to a crossroads. (left or right)> ")
    elif response == "move":
        cls()
        print("Yo get lost and die. LEVEL FAILED!!!")
    else:
        cls()
        print("Wrong input!")
    #final path
    response = input('''There! You found the cave. burn it down or go and fight it like a true swordsman 
    (burn or slay)> ''')

#wrong inputs
else:
    print("Adventure is only for those who follow instructions. Leave my sight!")
