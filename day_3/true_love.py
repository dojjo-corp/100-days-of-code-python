#Don't change the code below
name1 = input("What is your name?> ")
name2 = input("What is their name?> ")

#Write your code beolwo this line

#first get all characters to LOWER their heads in shame
name1 = name1.lower()
name2 = name2.lower()

#number  of "TRUE" characters in names
true_char = 0
#number of "LOVE" characters in names
love_char = 0

#how many characters of "LOVE" did you dare to contain
for i in "love":
    love_char += name1.count(i)
    love_char += name2.count(i)

#hm so you also had some characters of "TRUE" too..Let's get 'em boys!
for j in "true":
    true_char += name1.count(j)
    true_char += name2.count(j)

#concatenate scores for "love" and "true" and convert to intetger
love_score = int(str(true_char) + str(love_char))
print()

#intepretation of love score
if love_score < 10 or love_score > 90:
    print(f"You have a love score of {love_score}! You fit togeter like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"You have a love score of {love_score}! You are alright together.")
else:
    print(f"You have a love score of {love_score}!")


