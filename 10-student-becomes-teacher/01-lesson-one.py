# 1.

# Create three dictionaries: lloyd, alice, and tyler.

# Give each dictionary the keys "name", "homework", "quizzes", and "tests".

# Have the “name” key be the name of the student (that is, lloyd‘s name should be "Lloyd") and the other keys should be an empty list (We’ll fill in these lists soon!)

# 2.

# Now fill out your lloyd dictionary with the appropriate scores. To save you some time, we’ve filled out the rest for you.

# Homework: 90.0, 97.0, 75.0, 92.0

# Quizzes: 88.0, 40.0, 94.0

# Test Scores: 75.0, 90.0

# Make sure to include the decimal points so your grades are stored as floats! This will be important later.


lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# 3.

# Below your code, create a list called students that contains lloyd, alice, and tyler.

students = [lloyd, alice, tyler]

# 4.

# for each student in your students list, print out that student‘s data, as follows:

#     print the student‘s name
#     print the student‘s homework
#     print the student‘s quizzes
#     print the student‘s tests

# for student in students:
#     print(student["name"])
#     print(student["homework"])
#     print(student["quizzes"])
#     print(student["tests"])
#     print("-------------")

# 5.

# Write a function average that takes a list of numbers and returns the average.

#     Define a function called average that has one argument, numbers.
#     Inside that function, call the built-in sum() function with the numbers list as a parameter. Store the result in a variable called total.
#     Like the example above, use float() to convert total and store the result in total.
#     Divide total by the length of the numbers list. Use the built-in len() function to calculate 

def average(numbers):
    total = float(sum(numbers))
    return total / len(numbers)

# 6.

# Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler) as input and returns his/her weighted average.

#     Define a function called get_average that takes one argument called student.
#     Make a variable homework that stores the average() of student["homework"].
#     Repeat the above step for “quizzes” and “tests”.
#     Multiply the 3 averages by their weights and return the sum of those three. Homework is 10%, quizzes are 30% and tests are 60%.



def get_average(student):
    homework = average(student["homework"]) * 0.1
    quizzes = average(student["quizzes"]) * 0.3
    tests = average(student["tests"]) * 0.6
    return (homework + quizzes + tests) 

# 7.

# Define a new function called get_letter_grade that has one argument called score. Expect score to be a number.

# Inside your function, test score using a chain of if: / elif: / else: statements, like so:

#     If score is 90 or above: return "A"
#     Else if score is 80 or above: return "B"
#     Else if score is 70 or above: return "C"
#     Else if score is 60 or above: return "D"
#     Otherwise: return "F"

# Finally, test your function!

# Print the resulting letter grade with print. Call the get_letter_grade function and pass in get_average(lloyd).


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# print(get_average(lloyd) > 80)
# print()

# print(get_letter_grade(get_average(lloyd)))

# 8.

# Define a function called get_class_average that has one argument class_list. You can expect class_list to be a list containing your three students.

# First, make an empty list called results.

# For each student item in the class_list, calculate get_average(student) and then call results.append() with that result.

# Finally, return the result of calling average() with results.

def get_class_average(class_list):
    results = []
    for student in class_list:
        results.append(get_average(student))
    return average(results)

# 9.

# Find the average grade of the class. Print this numerical grade to the terminal.

print(get_class_average(students))

# 10.

# Finally, determine the letter grade for the class’s average and print it to the terminal.

print()

print(get_letter_grade(get_class_average(students)))

