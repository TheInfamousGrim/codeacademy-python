# 1.

# First, def a function called distance_from_zero, with one argument (choose any argument name you like).

# If the type of the argument is either int or float, the function should return the absolute value of the function input.

# Otherwise, the function should return "Nope"

def distance_from_zero(argument):
    if type(argument) == int or type(argument) == float:
        return abs(argument)
    else:
        return "Nope"

print(distance_from_zero(-32))
print(distance_from_zero(-1.25))
print(distance_from_zero("Hello"))