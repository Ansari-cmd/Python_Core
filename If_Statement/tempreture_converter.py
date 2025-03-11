# Tempreture Converter

unit = input("Is this tempreture in Celsius or Forenheit (C/F): ")
temp = float(input("Enter the tempreture"))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The tempreture in Forenheit is: {temp}F")
elif unit == "F":
    temp = round((temp - 32 ) * 5 /9, 1)
    print(f"The tempreture in Celsius is: {temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")
    
