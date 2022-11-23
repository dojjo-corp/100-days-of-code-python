from prettytable import PrettyTable
import random
days = 'monday tuesday wednesday thursday friday saturday sunday'.title().split()


# TODO: 1. create function to generate time intervals
def period_for_each(interval, good_time):
    '''Returns a list of random periods with the constant intervals'''
    possible_time = [i for i in range(24) if i not in range(int(good_time[0]), int(good_time[1])+1)]
    # convert interval minutes to hours
    time_to_use = []
    for i in range(sub_num):

        time_to_use.append(random.choice(possible_time))
    time_to_use.sort()

    return time_to_use


# TODO: 2. create a function to shuffle lists
def list_shuf(subs):
    '''Returns shuffled list. So shuffling is only done when needed'''
    random.shuffle(subs)
    return subs


# TODO: 3. create a function to assign days to work with
def days_to_work():
    '''Returns a list of random days in the week, depending on number preferred by user'''
    num_days = int(input('How many days will you like to work with? '))
    days_to_use = list_shuf(days)[:num_days]
    return days_to_use


# TODO: 4. function to create a table object and assign columns
def create_table():
    '''Prints out a table of days and random subjects assigned to each day. No return value'''
    table = PrettyTable()
    # first add column for time periods
    # table.add_column('time', period_for_each(time_interval, good_time))
    for day in days_to_work():
        table.add_column(day, list_shuf(subjects))
    print(table)


# TODO: 5. get user input
subjects = []
sub_num = int(input('How many subjects will you be working with? '))
for i in range(sub_num):
    subjects.append(input('Enter subject name: '))

# study times
time_interval = int(input('How long will you like to study for? (in minutes) '))

print('What part of the day will you be able to study within (hours in 24hr format separated by a comma)')
print('Example: 4, 18\nThis means anytime the hours of 0400 and 1800 will be a good time to study')
good_time = input('Enter hours: ').strip().split(',')

print(f'time to be used: {period_for_each(time_interval, good_time)}')
create_table()
can_change = True
while can_change:
    to_shuffle = input('Do you want to change the days given? (y/n)')
    if to_shuffle == 'y':
        create_table()
    else:
        can_change = False

