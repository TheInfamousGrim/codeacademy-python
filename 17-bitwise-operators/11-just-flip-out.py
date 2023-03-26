# ---------------------------------------------------------------------------- #
#                                 Just Flip Out                                #
# ---------------------------------------------------------------------------- #

# Using the XOR (^) operator is very useful for flipping bits. Using ^ on a bit with the number one will return a result where that bit is flipped.

# For example, let’s say I want to flip all of the bits in a. I might do this:

# a = 0b110 # 6
# mask = 0b111 # 7
# desired =  a ^ mask # 0b1

a = 0b11101110

mask = 0b11111111

desired = a ^ mask

print(bin(desired))