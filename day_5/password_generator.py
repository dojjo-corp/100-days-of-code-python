#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^', '{', '}', '\'', '<', '>', '/', '_', '=', '`', '~', '|']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
pass_type = int(input("What type of password would you like? 1 for strong 0 for weak\n> "))
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

if pass_type == 0:
  # final password
  easy_password = []
  #Eazy Level - Order not randomised:
  #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
  
  # for letters
  for i in range(nr_letters):
    easy_password.append(random.choice(letters))
  
  # for symbols
  for j in range(nr_symbols):
    easy_password.append(random.choice(symbols))
  
  # for numbers
  for i in range(nr_numbers):
    easy_password.append(random.choice(numbers))
  
  easy_password = ''.join(easy_password)
  print(easy_password)


elif pass_type == 1:
  ######################################################
  #Hard Level - Order of characters randomised:
  #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
  print("STRONG PASSWORD GENERATOR")
  
  strong_password = []
  # for letters
  for i in range(nr_letters):
    strong_password.append(random.choice(letters))
  
  # for symbols
  for j in range(nr_symbols):
    strong_password.append(random.choice(symbols))
  
  # for numbers
  for i in range(nr_numbers):
    strong_password.append(random.choice(numbers))
  
  # mixing up characters of strong password
  final_strong_password = []
  password_len = len(strong_password)
  final_strong_password = []
  random_index = 0
  used_index = []
  
  while len(final_strong_password) != len(strong_password):
    # generate random index for appending to strong password
    random_index = random.choice(range(password_len))
    
    # check for index repetition
    if random_index in used_index:
      continue
    
    # used indeces
    used_index.append(random_index)

    # append unique random character to final password
    final_strong_password.append(strong_password[random_index])
    
  # convert final strong password to string
  final_strong_password = ''.join(final_strong_password)
  print(final_strong_password)
