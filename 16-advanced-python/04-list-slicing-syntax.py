# 1.

# List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:

# [start:end:stride]

# We’ve generated a list with a list comprehension in the editor to the right, and we’re about to print a selection from the list using list slicing. Can you guess what will be printed out? Click Run when you think you know!

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(l[2:9:2])

# ---------------------------------------------------------------------------- #
#                               Omitting Indices                               #
# ---------------------------------------------------------------------------- #

# If you don’t pass a particular index to the list slice, Python will pick a default.

# to_five = ['A', 'B', 'C', 'D', 'E']
 
# print to_five[3:]
# # prints ['D', 'E'] 
 
# print to_five[:2]
# # prints ['A', 'B']
 
# print to_five[::2]
# # print ['A', 'C', 'E']

# 1.

# Use list slicing to print out every odd element of my_list from start to finish.

# Omit the start and end index. You only need to specify a stride.

# Check the Hint if you need help.

my_list = [x for x in range(1, 11)] # List of numbers 1 - 10

# Add your code below!

print(my_list[::2])