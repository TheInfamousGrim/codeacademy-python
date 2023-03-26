# 1.

# Define a function called is_prime that takes a number x as input.

# For each number n from 2 to x - 1, test if x is evenly divisible by n.

# If it is, return False.

# If none of them are, then return True.

def is_prime(x):
    if x == 0 or x == 1 or x < 0:
        return False
    for i in range(2, x - 1):
        print(x / i)
        if x / i % 1 == 0:
            return False
    else:
        return True

# print(is_prime(1))
# print(is_prime(3))
# print(is_prime(5))
# print(is_prime(9))
# print(is_prime(15))
print(is_prime(-10))
print(is_prime(-7))