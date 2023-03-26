# 1.

# Define a function called reverse that takes a string textand returns that string in reverse. For example: reverse("abcd") should return "dcba".

# You may not use reversed or [::-1] to help you with this.

# You may get a string containing special characters (for example, !, @, or #).

def reverse(text):
    listString = list(text)
    left = 0
    right = len(text) - 1

    while right > left:
        listString[left], listString[right] = listString[right], listString[left]
        left += 1
        right -= 1
    
    return ''.join(listString)

print(reverse("hello"))
