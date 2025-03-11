# if = Do some code only IF some condition is True
#      Else do something else

#ex1 Age
age  = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't born yet")
else:
    print("You must be 18+ to sign up")

response = input("Would you like food? (Y/N)")
if response == "Y":
    print("Have some food")
else:
    print("No food for you!")

#ex2 Name
name = input("Enter your name")

if name == "":
    print("You did not type in your name")
else:
    print(f"Hello, {name}!")

# Boolean for_sale
for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

# online

online = False

if online:
    print("The user is online")
else:
    print("The user is offline")
