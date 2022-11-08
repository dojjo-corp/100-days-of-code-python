# Don't change the code below this line
student_height = input("Enter a list of student heights: ").split()
for i in range(len(student_height)):
    student_height[i] = int(student_height[i])
print(student_height)

# Don't change the code above

# Write your code below this line
result = 0
counter = 0
for height in student_height:
    result += height
    counter += 1
average_height = round(result/counter)
print(f"The average height of the {counter} students is {average_height}")
