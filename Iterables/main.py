# Iterables = An object/collection that can return its element one at a time
#             allowing it to be iterated over in a loop

#numbers = [1,2,3,4,5]
# numbers = (1,2,3,4,5)

# for number in reversed(numbers):
#     print(number, end=" ")

#fruits = {"aplle", "orange", "banana","coconut"}

#for fruit in reversed(fruits):  # TypeError: 'set' object is not reversible
# for fruit in fruits:
#     print(fruit)

# name = "Danish Ansari"

# for character in name:
#     print(character, end=" ")

my_dictionary = {"A": 1, "B": 2, "C": 3}  
# for key in my_dictionary:   # for key
#     print(key)


for value in my_dictionary.values():  # for value
    print(value)

for key, value in my_dictionary.items():  # for key, value
    print(f"{key} = {value}")
