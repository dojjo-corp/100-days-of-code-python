##################*DEBUGGING*##################

# describe the problem
#def my_function():
#    for i in range(1, 20):
#        if i == 20:
#            print("You got it")
#my_function()

# reproduce the bug
#from random import randint
#dice_imgs = ['1', '2', '3', '4', '5', '6']
#dice_num = 6
#print(dice_imgs[dice_num])

#year = int(input("What is your year of birth? "))
#if year > 1980 and year < 1994:
#    print("You are a millenial")
#elif year >= 1994:
#    print("You are a Gen Z")

# print is your friend
#pages = 0
#word_per_page = 0
#pages = int(input("Number of pages: "))
#word_per_page = int(input("Number of words per page: "))
#print(f"Words per page: {word_per_page}")
#total_words = pages * word_per_page
#print(total_words)

# use debugger
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 7])
