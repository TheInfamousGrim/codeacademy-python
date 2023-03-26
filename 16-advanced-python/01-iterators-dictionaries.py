# 1.

# Create your own Python dictionary, my_dict, in the editor to the right with two or three key/value pairs.

# Then, print the result of calling the my_dict.items().

my_dict = {
    "Name": "GrimFunky",
    "Age": 27,
    "BDE": True
}

# print(my_dict.items())

# 1.

# Remove your call to .items() and replace it with a call to .keys() and a call to .values(), each on its own line. Make sure to print both!

# print(my_dict.keys())
# print(my_dict.values())

# 1.

# For each key in my_dict: print out the key , then a space, then the value stored by that key. (You should use print a, b rather than print a + " " + b.)

for key in my_dict:
    print(key, my_dict[key])
