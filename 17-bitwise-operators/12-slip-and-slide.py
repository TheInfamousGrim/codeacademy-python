# ---------------------------------------------------------------------------- #
#                                Slip and Slide                                #
# ---------------------------------------------------------------------------- #

# Finally, you can also use the left shift (<<) and right shift (>>) operators to slide masks into place.

# a = 0b101 
# # Tenth bit mask
# mask = (0b1 << 9)  # One less than ten 
# desired = a ^ mask

# 1.

# Define a function called flip_bit that takes the inputs (number, n).

# Flip the nth bit (with the ones bit being the first bit) and store it in result.

# Return the result of calling bin(result).

def flip_bit(number, n):
    mask = (0b1 << n - 1)
    return bin(number ^ mask)

print(flip_bit(0b101, 10))