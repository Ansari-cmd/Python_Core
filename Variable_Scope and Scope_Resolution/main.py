# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# local
# def fun1():
#     a =1
#     print(a)

# def fun2():
#     b = 2
#     print(b)

# fun1()
# fun2()

# Enclosed

# def fun1():
#     a =1
#     print(a)

#     def fun2():
#         b = 2
#         print(b)
    
# fun1()


# or 
# def fun1():
#     x = 1

#     def fun2():
#         x = 2
#         print(x)
#     fun2()
# fun1()

# global

# x = 3
# def fun1():
#     print(x)

# def fun2():
#     print(x)

# fun1()
# fun2()

# built-in

from math import e

def fun1():
    print(e)
e = 3

fun1()
