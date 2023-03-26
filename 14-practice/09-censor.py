# 1.

# Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks. For example:

# censor("this hack is wack hack", "hack") ```
 
# should return: 
 
# ```py
# "this **** is wack ****"

#     Assume your input strings won’t contain punctuation or upper case letters.
#     The number of asterisks you put should correspond to the number of letters in the censored word.

def censor(text, word):
    # blanked out word
    censoredText = ''
    for char in word:
        censoredText += '*'

    # split text into list
    listText = text.split()

    for i, textNode in enumerate(listText):
        if textNode in word:
            listText[i] = censoredText
    
    return ' '.join(listText)

print(censor("hello there", "hello"))
print(censor("fuck this doo doo I'm getting the fuck outta here", "fuck"))
