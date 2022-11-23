#leap year trial test
year = int(input("Enter year> "))

#No year can be Leap, unless I sayeth so!
isLeap = False

#All leap years must divisible by 4
if year%4==0:
    #but if they can also be divisible by 100...
    if year%100==0:
        #then they also have to be divisible by 400 to pass the leap test!
        if year%400==0:
            isLeap = True
    #if they are not divisible by 100 (but divisible by 4...) then they pass the test by Veto-Power!
    else:
        isLeap = True

print(isLeap)
