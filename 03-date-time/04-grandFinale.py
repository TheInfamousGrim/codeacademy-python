# 1.

# Print the date and time together in the form: mm/dd/yyyy hh:mm:ss.

# To start, change the format string to the left of the % operator.

#     Ensure that it has five %02d and one %04d placeholder.
#     Put slashes and colons and a space between the placeholders so that they fit the format above.Then, change the variables in the parentheses to the right of the % operator.
#     Place the variables so that now.month, now.day, now.year are before now.hour, now.minute, now.second. Make sure that there is a ( before the six placeholders and a ) after them.

from datetime import datetime
now = datetime.now()

print(f'{now.month}/{now.day}/{now.year} {now.hour}:{now.minute}:{now.second}')