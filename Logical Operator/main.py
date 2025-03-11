# logical operator = evaluate multiple condition (or, and, not)
#                    or = at least one condition must be True
#                    and = both condition must be True
#                    not = inverts the condition (not False, not True)

# or
temp = -5
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# and , not

temp = 28
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is Sunny 🫡")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is Sunny 🫡")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 😀")
    print("It is Sunny 🫡")
elif 28 >= temp > 0 and not is_sunny:
    print("It is WARM outside 😀")
    print("It is CLOUDY ☁️")
elif 28 >= temp > 0 and not is_sunny:
    print("It is WARM outside 😀")
    print("It is CLOUDY ☁️")
elif 28 >= temp > 0 and not is_sunny:
    print("It is WARM outside 😀")
    print("It is CLOUDY ☁️")