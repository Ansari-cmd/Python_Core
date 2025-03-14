# random module

import random

low = 1
high = 100

# number = random.randint(low, high)
# number = random.random()
# print(number)

# Rock Paper Scissors
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)


# Cards
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card = random.choice(cards)
print(card)

random.shuffle(cards)
print(cards)

