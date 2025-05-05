# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speek(self):
        print("WOOF!")
class Cat(Animal):
    def speek(self):
        print("MEOW!")
class Mouse(Animal):
    def speek(self):
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Micky")

print(cat.name)
print(cat.is_alive)


cat.eat()
cat.sleep()

dog.speek()
cat.speek()
mouse.speek()