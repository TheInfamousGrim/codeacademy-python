# 1.

# Define a function on line 3 called print_grades with one argument, a list called grades_input.

# Inside the function, iterate through grades_input and print each item on its own line.

# After your function, call print_grades with the grades list as the parameter

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

# def print_grades(grade_scores):
#     for grade in grade_scores:
#         print(grade)

# print_grades(grades)

# 2.

# On line 3, define a function, grades_sum, that does the following:

#     Takes in a list of scores, scores
#     Computes the sum of the scores
#     Returns the computed sum.

# Call the newly created grades_sum function with the list of grades and print the result.

def grades_sum(scores):
    total = 0
    for score in scores:
        total += score

    return total

# 3.

# Define a function, grades_average, below the grades_sum function that does the following:

#     Has one argument, grades_input, a list
#     Calls grades_sum with grades_input
#     Computes the average of the grades by dividing that sum by float(len(grades_input)).
#     Returns the average.

# Call the newly created grades_average function with the list of grades and print the result.


def grades_average(grades_input):
    return grades_sum(grades_input) / float(len(grades_input))

# print(grades_average(grades))

# 4.

# On line 18, define a new function called grades_variance that accepts one argument, scores, a list.

# First, create a variable average and store the result of calling grades_average(scores).

# Next, create another variable variance and set it to zero. We will use this as a rolling sum.

# for each score in scores: Compute its squared difference: (average - score) ** 2 and add that to variance.

# Divide the total variance by the number of scores.

# Then, return that result.

# Finally, after your function code, print grades_variance(grades).

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0

    for score in scores:
        variance += (average - score) ** 2
    
    return variance / len(scores)

# print(grades_variance(grades))

# 5.

# Define a function, grades_std_deviation, that takes one argument called variance.

# return the result of variance ** 0.5

# After the function, create a new variable called variance and store the result of calling grades_variance(grades).

# Finally print the result of calling grades_std_deviation(variance)

def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)

print(grades)

print(grades_sum(grades))

print(grades_average(grades))

print(grades_variance(grades))

print(grades_std_deviation(variance))