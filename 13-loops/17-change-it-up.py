# 1.

# Modify the code in the editor such that the for loop’s else statement is executed.

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
  if f == 'potato':
    print ('A tomato is not a fruit!') # (It actually is.))
    break
  print ('A', f)
else:
  print ('A fine selection of fruits!')
