def greet():
    print("Hello there! How do you do?")
    print("Isn't the weather nice today?")
greet()

print()
def greet_with_name(name):
    print(f"Hello there {name}!")
    print("How do you do?")
    print("Isn't the weather nice today?")
# greet_with_name(name)

# name = input("What is your name? ")

def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")

greet_with(name = "Martinson", location = "London")
