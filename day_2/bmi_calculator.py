#Don't change the code below
height = float(input("Enter yor height in m: "))
weight = float(input("Enter your weight in kg: "))

#Write your code below
bmi = int(weight)/float(height)**2
bmi_as_int = round(bmi)
print("Your bmi is " + str(bmi_as_int))
bmi_index = ""
