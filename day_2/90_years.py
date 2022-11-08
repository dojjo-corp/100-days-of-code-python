#program to calculate number of days, weeks and months a person has left until 
# they turn 90

# Don't change the code below
age = input("How old are you now?\n")

#Write your code below this line

years_left = 90 - int(age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {months_left} months, {weeks_left} weeks and {days_left} days until you turn 90")
