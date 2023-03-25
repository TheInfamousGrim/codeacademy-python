# 1.

# In the editor you’ll see two functions. Don’t worry about anything unfamiliar. We’ll explain soon enough.

#     Replace the underline on line 2 with an expression that returns True.
#     Replace the underline on line 6 with an expression that returns True.

# If you do it successfully, then both "Success #1" and "Success #2" are printed.

def using_control_once():
    if "Mum" == "Mum":
        return "Success #1"

def using_control_again():
    if True or False:
        return "Success #2"

print(using_control_once())
print(using_control_again())
