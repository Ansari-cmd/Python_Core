# validate user input execise
# 1. user name is no more than 12 character
# 2. user name must not contain spaces
# 3. user name must not contain digits

username = input("Enter a username")


if len(username) > 12:
    print("Your username can't be more than 12 character")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(F"Welcome {username}")
