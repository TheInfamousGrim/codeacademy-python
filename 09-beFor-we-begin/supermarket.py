# 1.

# Use a for loop to print out all of the elements in the list names.

names = ["Adam","Alex","Mariah","Martine","Columbus"]

# for name in names:
#     print(name)

# 2.

# Use a for loop to go through the webster dictionary and print out all of the definitions.

webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# for word in webster:
#     print(webster[word])

# 3.

# Like step 2 above, loop through each item in the list called a.

# Like step 3 above, if the number is even, print it out. You can test if the item % 2 == 0 to help you out.

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# for number in a:
#     if number % 2 == 0:
#         print(number)
    
# 4.

# Write a function that counts how many times the string "fizz" appears in a list.

#     Write a function called fizz_count that takes a list x as input.
#     Create a variable count to hold the ongoing count. Initialize it to zero.
#     for each item in x:, if that item is equal to the string "fizz" then increment the count variable.
#     After the loop, please return the count variable.

# For example, fizz_count(["fizz","cat","fizz"]) should return 2.

def fizz_count(x):
    count = 0
    for word in x:
        if word == "fizz":
            count += 1
    return count

# print(fizz_count(["fizz", "cat", "fizz"]))

# ---------------------------------------------------------------------------- #
#                                your own store                                #
# ---------------------------------------------------------------------------- #

# 1.

# Create a new dictionary called prices using {} format like the example above.

# Put these values in your prices dictionary, in between the {}:

# py "banana": 4, "apple": 2, "orange": 1.5, "pear": 3

# Yeah, this place is really expensive. (Your supermarket subsidizes the zoo from the last course.)

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# 2.

# Create a stock dictionary with the values below.

# py "banana": 6, "apple": 0, "orange": 32, "pear": 15

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

# 3.

# Loop through each key in prices.

# Like the example above, for each key, print out the key along with its price and stock information.

# Print the answer in EXACTLY the following format:

# apple
# price: 2
# stock: 0

# Like the example above, because you know that the prices and stock dictionary have the same keys, you can access the stock dictionary while you are looping through prices.

# When you’re printing, make sure to use the syntax from the example above, with %s.

# for fruit in prices:
#     print(f'{fruit}')
#     print(f'price: {prices[fruit]}')
#     print(f'stock: {stock[fruit]}')
#     print('------------')

# for fruit in prices:
#     print('%s' % fruit)
#     print('price: %s' % prices[fruit])
#     print('stock: %s' % stock[fruit])


# 4.

# Let’s determine how much money you would make if you sold all of your food.

#     Create a variable called total and set it to zero.
#     Loop through the prices dictionary.
#     For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
#     Finally, outside your loop, print total.
# print()

# total = 0

# for fruit in prices:
#     print(prices[fruit] + stock[fruit])
#     print('-----------')
#     total += prices[fruit] * stock[fruit]

# print()

# print(total)

# -------------------------- Shopping at the Market -------------------------- #

# 5.

# First, make a list called groceries with the values "banana","orange", and "apple".

shopping_list = ["banana", "orange", "apple"]

# 6.

# Define a function compute_bill that takes one argument food as input.

# In the function, create a variable total with an initial value of zero.

# For each item in the food list, add the price of that item to total.

# Finally, return the total.

# Ignore whether or not the item you’re billing for is in stock.Note that your function should work for any food list.

# 7.

# Make the following changes to your compute_bill function:

# While you loop through each item of food, only add the price of the item to total if the item’s stock count is greater than zero.

# if the item is in stock and after you add the price to the total, subtract one from the item’s stock count.


def compute_bill(food):
    total = 0

    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total

print(compute_bill(shopping_list))

