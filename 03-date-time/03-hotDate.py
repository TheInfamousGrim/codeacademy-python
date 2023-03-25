from datetime import datetime
now = datetime.now()

# 1.

# Print the current date in the form of mm/dd/yyyy.

# Change the string used above so that it uses a / character in between the %02d and %04d placeholders instead of a - character.

print(f'{now.month}-{now.day}-{now.year}')

# 1.

# Similar to the last exercise, print the current time in the pretty form of hh:mm:ss.

#     Change the string that you are printing so that you have a : character in between the %02d placeholders.

#     Change the three things that you are printing from month, day, and year to now.hour, now.minute, and now.second.

print(f'{now.hour}:{now.minute}:{now.second}')