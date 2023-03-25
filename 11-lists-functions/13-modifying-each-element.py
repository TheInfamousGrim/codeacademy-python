# 1.

# Create a function called double_list that takes a single argument x (which will be a list) and multiplies each element by 2 and returns that list. Use the existing code as a scaffold.
n = [3, 5, 7]
n2 = [0, 1]

def double_list(x):
    for i in range(0, len(x)):
        print(i)
        x[i] = x[i] * 2
    return x

# Don't forget to return your new list!

print(double_list(n))
print(double_list(n2))