'''
A SIMPLE PROGRAM TO COMPUTE TIPS FOR SERVICE PERSONNELS!
'''
print("Welcome to the Tip Calculator!")

#get total bill
total_bill = float(input("What was the total bill?\n$"))

#get the percentage they'll give as a tip
percentage_tip = float(input("What percentage will you like to give as a tip? 10, 12 or 15.\n"))

#how many people will split the bill
people_to_split = int(input("How many people will split the bill?\n"))

#compute the tip
tip = total_bill * (percentage_tip/100)

#compute how much each will have to pay
amount_for_each = (tip + total_bill)/people_to_split

print(f"Each person will have to pay ${round(amount_for_each, 2)}")