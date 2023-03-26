# 1.

# Create a class called Animal in the editor. For now, in the body of your class, use the pass keyword. (pass doesn’t do anything, but it’s useful as a placeholder in areas of your code where Python expects an expression.)

# 2.

# Remove the pass statement in your class definition, then go ahead and define an __init__() function for your Animal class. Pass it the argument self for now; we’ll explain how this works in greater detail in the next section. Finally, put the pass into the body of the __init__() definition, since it will expect an indented block.

# 3.

# Let’s do two things in the editor:

#     Pass __init__() a second parameter, name.
#     In the body of __init__(), let the function know that name refers to the created object’s name by typing self.name = name. (This will become crystal clear in the next section.)

# 4.

# Outside the Animal class definition, create a variable named zebra and set it equal to Animal("Jeffrey").

# Then print out zebra‘s name

class Animal(object):
    def __init__(self, name):
        self.name = name

zebra = Animal("Jeffrey")

print(zebra.name)