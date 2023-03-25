# 1.

# Complete the else statements to the right. Note the indentation for each line!

answer = "'Tis but a scratch!"

def black_knight(answer_input):
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False       # Make sure this returns False

def french_soldier(answer_input):
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False       # Make sure this returns False

print(black_knight(answer))
print(french_soldier(answer))