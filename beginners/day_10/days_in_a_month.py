# function to check for leap years
def is_leap(year):
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
    return isLeap

def days_in_month(year, month):
''' function to get days in month'''
    possible_days = {
            "leap": [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], 
            "non_leap": [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            }
    if is_leap(year):
        number_of_days = possible_days["leap"][month-1]
    else:
        number_of_days = possible_days["non_leap"][month-1]
    return number_of_days

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
