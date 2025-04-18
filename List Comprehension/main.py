# List comprehension = A consise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable]



doubles = [x*2 for x in range(1,11)]
triples = [y*3 for y in range(1,11)]
squares = [z*z for z in range(1,11)]
print(doubles)
print(triples)
print(squares)

fruits = ["apple", "orange", "banana", "coconut"]
#fruit = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
fruit = [fruit.upper() for fruit in fruits]
fruit_cahrt = [fruit[0] for fruit in fruits]
print(fruit)
print(fruit_cahrt)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_num = [num for num in numbers if num >= 0]
negative_num = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]
print(positive_num)
print(negative_num)
print(even_nums)
print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)

