# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicate

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}
# print(dir(capitals))
# print(help(capitals))

# if capitals.get("Russia"):
#     print("The capital exists")
# else:
#     print("That capital dosen't exist")

# capitals.update({"Germany": "Berlin"})

# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys()
# keys = capitals.keys()
# print(keys)

# for key in capitals.keys():
#     print(key)

# values()
# values = capitals.values()
# print(values)

# for value in capitals.values():
#     print(value)

# items()
# items = capitals.items()
# print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")