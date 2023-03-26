# 1.

# Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

# For example: anti_vowel("Hey You!") should return "Hy Y!". Don’t count Y as a vowel. Make sure to remove lowercase and uppercase vowels.

def anti_vowel(text):
    removedVowelList = []
    vowels = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' }



    for char in text:
        if char not in vowels:
            removedVowelList.append(char)

    return "".join(removedVowelList)

print(anti_vowel("Hey You!"))

