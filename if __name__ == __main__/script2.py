from script1 import *
# print(__name__)

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")
print("This is script2")

def main():
    favorite_food('burger')
    favorite_drink("Mojito")
    print("Goodbye")

if __name__ == '__main__':
    main()