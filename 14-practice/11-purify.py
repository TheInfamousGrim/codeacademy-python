# 1.

# Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result. For example, purify([1,2,3]) should return [2].

# Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.

def purify(sequence):
    purifiedNumbers = []

    for number in sequence:
        if number % 2 == 0:
            purifiedNumbers.append(number)

    return purifiedNumbers

print(purify([1,2,3]))
print(purify([1,2,3,4,5,6,7,8,9]))
