# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in


# string
# word = "APPLE"

# letter = input ("Guess a letter in the secret word: ")

# # in
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

# # not in
# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")


# students = {"Spongebob", "Patrick", "Sandy"}

# student = input("Enter the name of a student:")

# # in 
# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")

# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a student")

# dict

grades = {"sandy": "A", "Squidward": "B", "Spongebob": "C", "Patrick": "D" }

student = input("Enter the name of a student:")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    (f"{student} was not found")

email = "DanishAnsari9648@gmail.com"

if '@' in email and ". in email":
    print("Valid email")
else:
    print("Invalid email")
