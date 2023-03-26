# 1.

# Create a variable, backwards_by_tens, and set it equal to the result of going backwards through to_one_hundred by tens. Go ahead and print backwards_by_tens to the console.

to_one_hundred = [x for x in range(101)]

# Add your code below!

backwards_by_tens = to_one_hundred[::-10]

print(backwards_by_tens)
