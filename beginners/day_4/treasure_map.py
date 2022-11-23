'''
Apparently the easiest way is to just assign the 'X' character to the indicated 
position instead of popping and inserting it.
'''

#Don't change the code below
row1 = ["ೱ", "ೱ", "ೱ"]
row2 = ["ೱ", "ೱ", "ೱ"]
row3 = ["ೱ", "ೱ", "ೱ"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

response = input("Where would you like to place your treasure?\n> ")

#reduce user input by one to use as list index
i=int(response[0])-1
j=int(response[1])-1

# print empty line
print("")

# the key is to locate the list within the 'map' and work on that particular list
# instead of trying to work on the map itself
# the first index from user input is to locate the particular list to work with
# and the second input is the index of the object to work on

# this locates the list found at index 'i' of 'map' and pops the object at index 'j' 
# within that list (i)
map[i].pop(j)

# locate list at index 'i' of map. Within that list (i), insert the 'X' character 
# before index 'j'
map[i].insert(j,'X')

# print new map
print(f"{row1}\n{row2}\n{row3}")
