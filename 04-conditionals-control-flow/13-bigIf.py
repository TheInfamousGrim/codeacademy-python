# 1.

# In the workspace to your right, there is the outline of a function called grade_converter().

# The purpose of this function is to take a number grade (1-100), defined by the variable grade, and to return the appropriate letter grade (A, B, C, D, or F).

# Your task is to complete the function by creating appropriate if and elif statements that will compare the input grade with a number and then return a letter grade.

# Your function should return the following letter grades:

#     90 or higher should get an “A”
#     80 - 89 should get a “B”
#     70 - 79 should get a “C”
#     65 - 69 should get a “D”
#     Anything below a 65 should receive an “F”

def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"

print(grade_converter(91))
print(grade_converter(70))
print(grade_converter(61))