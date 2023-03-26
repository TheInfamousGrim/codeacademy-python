# 1.

# The loop in the editor has two problems: it’s missing a colon (a syntax error) and count is never incremented (logical error). The latter will result in an infinite loop, so be sure to fix both before running!

count = 0

while count < 10: # Add a colon
  print(count)
  # Increment count
  count += 1
