# function = A block of reusable code
#            place () after the function name to invoke it


def happy_birthday(name,age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age}!")
    print(f"Happy birthday to {name}!")
    print()

happy_birthday("John",25)
happy_birthday("Buggu",23)
happy_birthday("Maggu",25)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("John", 120.45, "01/02" )

