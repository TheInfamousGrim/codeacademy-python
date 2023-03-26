# 1.

# Check out the code in the editor. Note that each individual animal gets its own name and age (since they’re all initialized individually), but they all have access to the member variable is_alive, since they’re all members of the Animal class. Click Run to see the output!

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print(zebra.name, zebra.age, zebra.is_alive)
print(giraffe.name, giraffe.age, giraffe.is_alive)
print(panda.name, panda.age, panda.is_alive)
