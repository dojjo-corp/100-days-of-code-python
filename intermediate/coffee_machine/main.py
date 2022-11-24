from prettytable import PrettyTable

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Profit
revenue = 0


# TODO: create function to check transaction
def transaction(order, amount):
    if sum(amount) < MENU[order]["cost"]:
        return False
    else:
        return True


# TODO: create function to check resources available for a coffee
def enough_resources(drink):
    """Returns True if enough resources are available for the drink;
    When lacking, the insufficient ingredient is returned rather"""
    for resource in resources:
        if resources[resource] < MENU[drink]["ingredients"][resource]:
            return resource
        else:
            return True


# TODO: create a function to convert denominations to dollars
def to_dollars(amount, base_currency):
    """Returns the dollar equivalent of the various denominations"""
    final_amount = 0
    if base_currency == "pennies":
        final_amount = amount * 0.01
    elif base_currency == "nickels":
        final_amount = amount * 0.05
    elif base_currency == "dimes":
        final_amount = amount * 0.1
    elif base_currency == "quarters":
        final_amount = amount * 0.25
    else:
        print("unknown denomination")
    return round(final_amount, 2)


# loop-control flag
next_order = True
commands = {
        'menu': 'Display the coffee menu', 
        'report': 'Display a report on resources available', 
        'restock': 'Allow for resources to be restocked', 
        'off': 'Turn off coffee maker machine', 
        'help': 'Display this help menu', 
        }
print("ps.: Type 'help' to display control-commands\n")

while next_order:
    # TODO: prompt user for input (drink initially)
    user_input = input("\nWhat will you like to order today? (espresso/latte/cappuccino): ").lower()

    # TODO: check enough resources and cost
    denominations = ["pennies", "nickels", "dimes", "quarters"]
    payment = []
    if user_input in MENU:
        print(f"\nA cup of {user_input.upper()} costs ${MENU[user_input]['cost']}")

        # make payment if enough ingredients are available
        if enough_resources(user_input) == True:
            print("Please insert coins")
            for deno in denominations:
                payment.append(int(input(f"How many {deno}: ")))

            # convert to dollars
            pay_in_dollars = 0
            for i in range(4):
                pay_in_dollars += to_dollars(payment[i], denominations[i])
            print(f"\nYou paid: ${pay_in_dollars}")

            # TODO: check if payment is enough to cover cost of drink
            if pay_in_dollars < MENU[user_input]["cost"]:
                print(f"Sorry, not enough money for one {user_input}. Money refunded\n")
            elif pay_in_dollars > MENU[user_input]["cost"]:
                print(f"Here's your change: ${round(pay_in_dollars - MENU[user_input]['cost'], 2)}")
                print(f"One cup of {user_input.upper()} ready. Enjoy! ☕\n")
            else:
                print(f"One cup of {user_input.upper()} ready. Enjoy! ☕\n")

            # TODO: reduce resources after serving drink, and add money paid to coffers
            for key in resources:
                resources[key] -= MENU[user_input]["ingredients"][key]
            revenue += MENU[user_input]["cost"]

        else:
            print(f"Sorry not enough {enough_resources(user_input)} to make your {user_input.upper()}.")
            another = input(f"Try another drink? (y/n): ").lower()
            if another == "n":
                next_order = False
    
    
    # TODO: print help menu
    elif user_input == 'help':
        table = PrettyTable()
        table.field_names = ('Commands', 'Description')
        for k, v in commands.items():
            # print(f'"{k}": {v}')
            table.add_row([k, v])
        print(table)

    # TODO: print report of resources when requested
    elif user_input == "report":
        resource_table = PrettyTable()
        resource_table.field_names = ('Resource', 'Amount')
        for entry in resources:
            res_row = [f"{entry}", f"{resources[entry]}"]
            resource_table.add_row(res_row)
        resource_table.add_row([f"Profit", f"${revenue}"])
        print(resource_table)

    # TODO: display entire menu
    elif user_input == "menu":
        menu = PrettyTable()
        menu.field_names = ('Coffee', 'Price')
        for entry in MENU:
            row = [f"{entry.title()}", f"${MENU[entry]['cost']}"]
            menu.add_row(row)
        print(menu)

    # TODO: allow resources to be restocked
    elif user_input == "restock":
        stock = input("What do you want to restock (water/milk/coffee): ")
        amount = int(input("Enter amount: "))
        resources[stock] += amount

    # TODO: quit program at order prompt
    elif user_input == "off":
        print("Thanks for stopping by. Do come back next time!")
        break
