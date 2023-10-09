import random
#from random import choice

coin = random.choice(["heads" , "tails"])
number = random.randint (1,10)
print(number)

cards = ["jack" , "queen" , "king"]
random.shuffle(cards)
for card in cards:
    print(card)