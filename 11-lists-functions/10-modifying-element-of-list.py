# 1.

# Change list_function to:

#     Add 3 to the item at index 1 of the list.
#     Store the result back into index 1.
#     Return the list.

def list_function(x):
    x[1] += 3
    return x

n = [3, 5, 7]
print(list_function(n))

