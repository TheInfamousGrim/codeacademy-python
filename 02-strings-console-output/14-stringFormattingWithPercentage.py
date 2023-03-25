# 1.

# Take a look at the code in the editor. What do you think it’ll do? Click Run when you think you know.

string_1 = "Camelot"
string_2 = "place"

print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

# USE STRING INTERPOLATION IT"S SO MUCH BETTER

# 2.

# Now it’s your turn! We have ___ in the code to show you what you need to change!

#     Inside the string, replace the three ___ with %s.
#     After the string but before the three variables, replace the final ___ with a %.
#     Hit Run.

name = "Alex"
quest = "Teaching Python"
color = "Blue"

print("Ah, so your name is %s, your quest is %s, and your favorite color is %s." % (name, quest, color))

template_string = f"Ah, so your name is {name}, your quest is {quest}, and your favorite color is {color}."

print(template_string)