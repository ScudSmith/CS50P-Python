# Will import all of random module
import random

# Will only import choice function
# from random import choice

# If importing whole module, have to fully
# qualify function call
coin = random.choice(["heads", "tails"])

# if importing only the function, can streamline
# function call
# coin = choice(["heads", "tails"])

print(coin)

# Generate random number between the two
# parameters, inclusive
number = random.randint(1, 10)
print(number)

# shuffle changes the order of the items
# in the list
cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card)
