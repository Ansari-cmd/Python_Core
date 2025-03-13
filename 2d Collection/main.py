# example 1
fruits = ['apple','orange','banana','coconut']
vegetables = ['celery','carrots', 'potatos']
meats = ['chicken','fish','turkey']

# groceries = [fruits, vegetables, meats] 
# print(fruits)
# print(groceries)
# print(groceries[2])
# print(groceries[0][0])

groceries = [
    ['apple','orange','banana','coconut'],
    ['celery','carrots', 'potatos'],
    ['chicken','fish','turkey']
]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    #print(collection)
    print()




