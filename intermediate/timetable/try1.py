'''
A simple program to create a timetable with any number of subjects
'''


# function to assign subjects to days
def alternate_subs(subs, days, num_per_day):
    '''Returns randomly generated time intervals to be used for timetable'''
    pass


# Get number of subjects
num = input('How many subjects will you use?\n')

# create list for subjects and append from standard input
subjects = []
for i in range(int(num)):
    subjects.append(input('Enter name of subject:\n'))

days = input("How many days would you like to work with?\n")
subs_per_day = input('How many times will you like to study in a day? ')

# display subjects
print('These are the subjects you will be working with:')
print(subjects)

alternate_subs(subjects, days, subs_per_day)

