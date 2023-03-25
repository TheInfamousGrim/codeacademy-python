# 1.

# Remove the first item from the list n using either .pop(), .remove(), or del.

n = [1, 3, 5]
# Remove the first item in the list here

# Pop will remove the element at the index specified and return the element removed
# n.pop(0)

# .remove() will remove the specified element
# n.remove(1)

# del(n[1]) will remove the item at the give index but won't return it
del(n[0])

print(n)
