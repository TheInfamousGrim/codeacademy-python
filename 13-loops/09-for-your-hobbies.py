# 1.

# Create a for loop that prompts the user for a hobby 3 times.

# Save the result of each prompt in a hobby variable

# append each one to hobbies.

# print hobbies after your for loop

# Make sure to answer the prompts in the terminal when testing your code!

hobbies = []

# Add your code below!
for i in range(3):
    hobby = str(input("Name one hobby you enjoy: "))
    hobbies.append(hobby)

print(hobbies)