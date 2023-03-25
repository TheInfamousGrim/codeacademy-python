# 1.

# Create a function that returns the sum of a list of numbers.

#     On line 3, define a function called total that accepts one argument called numbers. It will be a list.
#     Inside the function, create a variable called result and set it to zero.
#     Using one of the two methods above, iterate through the numbers list. For each number, add it to result.
#     Finally, return result.

n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(0, len(numbers)):
        result += numbers[i]
    return result

print(total(n))