# 1.

# Assign to dog a slice of animals from index 3 up until but not including index 6.

# Assign to frog a slice of animals from index 6 until the end of the string.

animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]

print(cat)
print(dog)
print(frog)