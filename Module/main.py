# module = a file containing code you want to include in your program 
#          use 'import' to include module (built-in or your own)
#          useful to break up a large program reusable separate files

#print(help("modules"))
#print(help("math"))

import example

result = example.pi
result = example.cube(3)
print(result)
result = example.square(3)
print(result)
result = example.circumference(3)
print(result)
result = example.area(3)
print(result)