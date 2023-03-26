# ---------------------------------------------------------------------------- #
#                    Slide to the Left! Slide to the Right!                    #
# ---------------------------------------------------------------------------- #

# The block below shows how these operators work on the bit level. Note that in the diagram, the shift is always a positive integer:

# # Left Bit Shift (<<)  
# 0b000001 << 2 == 0b000100 (1 << 2 = 4)
# 0b000101 << 3 == 0b101000 (5 << 3 = 40)       
 
# # Right Bit Shift (>>)
# 0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
# 0b0000010 >> 2 == 0b000000 (2 >> 2 = 0) 

# 1.

# Shift the variable shift_right to the right twice (>> 2) and shift the variable shift_left to the left twice (<< 2). Try to guess what the printed output will be!

shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2


print(bin(shift_right))
print(bin(shift_left))
