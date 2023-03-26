# ---------------------------------------------------------------------------- #
#                             They're Multiplying!                             #
# ---------------------------------------------------------------------------- #

# A class can have any number of member variables. These are variables that are available to all members of a class.

# hippo = Animal("Jake", 12)
# cat = Animal("Boots", 3)
# print hippo.is_alive
# hippo.is_alive = False
# print hippo.is_alive
# print cat.is_alive

# 1.

# After line 3, add a second member variable called health that contains the string "good".

# Then, create two new Animals: sloth and ocelot. (Give them whatever names and ages you like.)

# Finally, on three separate lines, print out the health of your hippo, sloth, and ocelot.

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)

hippo = Animal("Jerry", 21)
sloth = Animal("Jerome", 109)
ocelot = Animal("Miguel", 13)

hippo.description()
print(hippo.health)
print(sloth.health)
print(ocelot.health)