# 1.

# The string in the editor is garbled in two ways:

#     Our message is backwards.
#     The letter we want is every other letter.

# Use list slicing to extract the message and save it to a variable called message

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]
print(message)