from random import *

bots_number = randint(1, 100)

your_number = int(input("Choose your number (From 1 to 100): "))
if your_number < 1 or your_number > 100:
    if your_number == 100:
        print("You win")
    else:
        print("You lose")
else:
    print("Wrong number")