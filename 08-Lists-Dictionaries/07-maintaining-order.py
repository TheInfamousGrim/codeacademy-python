# 1.

# Use the .index() method to find the index of "duck". Assign that result to a variable called duck_index.

# Then use the .insert() method with duck_index as the first argument and the string "cobra" as the second argument.

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")

# Your code here!
animals.insert(duck_index, "cobra")


print(animals) # Observe what prints after the insert operation