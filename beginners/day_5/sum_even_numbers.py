# Don't change the code below
range_of_numbers = input("Enter the range of numbers to sum even numbers from> ").split(" ")
for i in range(len(range_of_numbers)):
    range_of_numbers[i] = int(range_of_numbers[i])
print(f"Range of numbers to work with: {range_of_numbers}\n")

# list of even numbers within range given
even_numbers = []

# to hold sum of numbers
sum_of_even = 0

for num in range(range_of_numbers[0], range_of_numbers[1]):
    if num%2 == 0:
        # add up all even numbers found within range
        sum_of_even += num
        # append even numbers (as strings) to list of even numbers
        even_numbers.append(str(num))

print(f"Even numbers found within given range are {', '.join(even_numbers)}")
print(f"The sum of even numbers between {range_of_numbers[0]} and {range_of_numbers[1]} is " + str(sum_of_even))
