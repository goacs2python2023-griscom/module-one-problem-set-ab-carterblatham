import random

def die_roll():
    roll = random.randint(1, 6)
    print("You rolled a " + str(roll))
    return roll

sum = die_roll() + die_roll()

if 6 <= sum <= 8:
    print("You win! (You rolled a sum of " + str(sum) + ")")
else:
    print("You lose! (You rolled a sum of " + str(sum) + ")")