# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
        "+": add, 
        "-": subtract, 
        "*": multiply, 
        "/": divide
       }

def Calculator():
    from os import system
    system('clear')
    # start work
    num1 = float(input("What is the first number: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the list above: ")
    num2 = float((input("What is the second number: ")))

    answer1 = operations[operation_symbol](num1, num2)
    previous_answer = answer1

    print(f"{num1} {operation_symbol} {num2} = {answer1}")

    is_end = False
    while is_end == False:
        response = input(f"Type 'y' to continue calculating with {previous_answer}, or 'n' to start again: ")
        if response == "n":
            is_end = True
            Calculator()
        elif response == "y":
            operation_symbol = input("Pick an operation from the options above to work with: ")
            num3 = int(input("What is the other number: "))
            answer2 = operations[operation_symbol](previous_answer, num3)
            print(f"{previous_answer} {operation_symbol} {num3} = {answer2}")
            previous_answer = answer2
        else:
            print("For once in your miserable life, just enter the right thing and shame the devil in your house.")

Calculator()