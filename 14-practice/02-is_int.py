# 1.

# Define a function is_int that takes a number x as an input.

# Have it return True if the number is an integer (as defined above) and False otherwise.

# For example:

# is_int(7.0)   # True    
# is_int(7.5)   # False    
# is_int(-1)    # True      

def is_int(x):
    if x % 1 == 0:
        return True
    else:
        return False

print(is_int(-1))