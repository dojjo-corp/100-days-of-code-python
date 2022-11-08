'''
UPGRADED BMI CALCULATOR!
'''

print("Welcome to the BMI calculator!")
weight = int(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in m: "))
bmi = round(weight/(height**2))
#comment per bmi index
comment = ""

if bmi < 18.5:
    comment = "Under Weight"
elif bmi < 25:
    comment = "Normal Weight"
elif bmi < 30:
    comment = "Over Weight"
elif bmi < 35:
    comment = "Obese"
else:
    comment = "Clinically Obese"
    print("You better start reducing your intake of yoghurt if you want to still have any hope of being called granny!\n")

print("Your bmi is", bmi)
print("This means you are", comment)
