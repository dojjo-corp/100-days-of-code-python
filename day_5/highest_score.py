# Don't change the code below
student_scores = input("Enter a list of student scores: ").split()
for n in range(len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# Don't change the code above

# Write your code below this line

# variable to hold highest score
highest = 0

# get the highest score in list
for score in student_scores:
    if score > highest:
        highest = score

print(f"The highest score in the class is: {highest}")
