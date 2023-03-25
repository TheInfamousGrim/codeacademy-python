print("Welcome to the Pig Latin Translator!")

# Start Coding Here

# 1.

# Create a program that will turn any word into pyglatin: For example "python" becomes "nythopay"

# Type a word in the console window and press Enter (or Return).

# Pyg suffix
pyg = "ay"

original = input("Enter a word: ")


if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1 : len(new_word)]
    print(new_word)
else:
    print("empty")