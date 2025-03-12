# format specifiers = {value:flags} format a value based on what
#                              flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center alighn
# :+ = use a plus sign to indicate positive value
# := = place sign to left most position
# :  = insert a space before positive numbers
# :, = comma seperator

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 a is ${price1:+,.2f}") # for 2 decimal places
print(f"Price 2 a is ${price2:+,.2f}")
print(f"Price 3 a is ${price3:+,.2f}")