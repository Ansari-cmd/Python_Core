# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# strings

first_name="Danish"
food="Burger"
email="danishansari9648@gmail.com"
print(f"hello {first_name}")
print(f"you like {food}")
print(f"your email is {email}")

# Integers
age=25
quantity=3
num_of_studennts=30

print(f"You are {age} years old")
print(f"you are buying {quantity} items")
print(f"your class has {num_of_studennts} students")

# Float
price=10.99
gpa=3.2
distance=5.6

print(f"The price is {price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")

# Boolean

is_student=False

print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student ")
else:
    print("you are not a student")

for_sale = True
if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")

is_online = True

if is_online:
    print("You are online")
else:
    print(" You are offline")



# Typecasting = the process of converting a variable from one type to another
#                str(), int(), float(), bool()

name = "Danish Ansari"
age = 25
gpa = 3.5
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa, type(gpa))

age = float(age)
print(age, type(age))


age = str(age)
age+="1"
print(age,type(age))

name = bool(name)
print(name) # True
name = "" 
name = bool(name)
print(name)  # False


# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?:")
age = input("How old are you?:")
#age = age + 1     #TypeError: can only concatenate str (not "int") to str
age = int(age)
# or int(input("How old are you?:"))
age = age + 1

# or int(input("How old are you?:"))
print(f"Hello, {name}!")
print("Happy Birthday!")
print(f"You are {age} old")

