student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99, 
        "Draco": 74, 
        "Neville": 62
        }

# Don't change the code above

def grade(num):
    grade = ""
    if num <= 70:
        grade = "Fail"
    elif num <= 80:
        grade = "Acceptable"
    elif num <= 90:
        grade = "Exceeds Expectations"
    else:
        grade = "Outstanding"
    return grade

student_grades = {}

for key in student_scores:
    student_grades[key] = grade(student_scores[key])

# Don't change the code below
print(student_grades)
