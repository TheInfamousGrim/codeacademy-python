# 1.

# Change the loop so that it counts from 0 up to 9 (inclusive).

# Be careful not to alter or remove the count += 1 statement. If your program has no way to increase count, your loop could go on forever and become an infinite loop which could crash your computer/browser!

count = 0

if count < 5:
  print("Hello, I am an if statement and count is", count)

while count <= 9:
  print("Hello, I am a while and count is", count)
  count += 1
