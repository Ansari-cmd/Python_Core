# # arbitary arguments
# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITARY


# *args 
#============================
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1,2,3,4))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
# display_name("danish","ansari","john","ben")

#  **kwargs
#=============================================

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="ward no 5 sinha road", city="Ghosiya", state="Uttar Pradesh", zip="221301")

