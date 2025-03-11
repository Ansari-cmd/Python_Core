# string methods 

name = input("Enter yur full name: ")
phone_number = input("Enter your phone number #: ")

# len() to find the length of string
result= len(name)
print (result)

# find()  for first occurence of character

result = name.find("s")
print(result)

# .rfind() for last occurence
result = name.rfind("s")
print(result)


# capitalize() for first letter capitalization

name = name.capitalize()
print(name)

# upper() for all uppercase letter

name = name.upper()
print(name)

# lower() for lowercase letter

name = name.lower()
print(name)

# isdigit() for checking digit or not restult in True or False
result = name.isdigit()
print(result)

# isalpha() checking alphabatical character
result = name.isalpha()
print(result)

# count() count the character
result = phone_number.count("-")
print(result)

# replace() for replacing character
phone_number = phone_number.replace("-"," ")
print(phone_number)

# tree of string methods
print(help(str()))
