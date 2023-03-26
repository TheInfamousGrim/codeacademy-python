# 1.

# Fill in the loop condition so the user will be prompted for a choice over and over while choice does not equal 'y' and choice does not equal 'n'.

choice = input('Enjoying the course? (y/n)')

while (choice != "n") and (choice != "y"):  # Fill in the condition (before the colon)
  choice = input("Sorry, I didn't catch that. Enter again: ")
