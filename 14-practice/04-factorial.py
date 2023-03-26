def factorial(x):
    total = 1
    for i in range(x):
        total *= i + 1
    return total

print(factorial(4))