"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""

# 1.

# On line 13, assign the variable fifth_letter equal to the fifth letter of the string “MONTY”.

# Remember that the fifth letter is not at index 5. Start counting your indices from zero.

monty_string = "MONTY"


fifth_letter = monty_string[4]

print(fifth_letter)