# 1.

# Use a list comprehension to build a list called even_squares in the editor.

# Your even_squares list should include the squares of the even numbers between 1 to 11. Your list should start [4, 16, 36...] and go from there.

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]

print(even_squares)

# 1.

# Use a list comprehension to create a list, cubes_by_four.

# The comprehension should consist of the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.

# Finally, print that list to the console.

# Note that in this case, the cubed number should be evenly divisible by 4, not the original number.

cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]

print(cubes_by_four)
