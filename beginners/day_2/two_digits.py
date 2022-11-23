isTwo = False
while (isTwo==False):
    num = input("Enter a two digit number:\n")
    if len(num) > 2:
        isTwo = False
        print("Please enter numbers with only two digits.")
    else:
        isTwo = True
        print(int(num[0]) + int(num[1]))
