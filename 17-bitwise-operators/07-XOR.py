# ---------------------------------------------------------------------------- #
#                                This XOR That?                                #
# ---------------------------------------------------------------------------- #

# The XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of the two numbers are 1, but not both.

#     a:  00101010   42
#     b:  00001111   15       
# ================
# a ^ b:  00100101   37

# So remember, for every given bit in a and b:

# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0

# 1.

# For practice, print the result of using ^ on 0b1110 and 0b101 as a binary string. Try to do it on your own without using the ^ operator.

print(bin(0b1110 ^ 0b101))
