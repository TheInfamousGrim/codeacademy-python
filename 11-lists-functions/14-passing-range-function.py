# 1.

# On line 6, replace the ____ with a range() that returns a list containing [0, 1, 2].

def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print(my_function(list(range(3)))) # Add your range between the parentheses!
