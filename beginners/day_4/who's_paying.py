import random

print("Welcome to the Who's Paying Program!\n")
#get names
response = input("Give me everybody's name with a comma separating them\n> ")
# convert to list
name_list = response.split(", ")

random_index = random.randint(0, len(name_list)-1)

print(f"{name_list[random_index]} is paying the bill today!")