# Create a game of dice throw, where user plays with computer
# Implement function throw_die, for random throw 1,2,3,4,5 or 6
# Throw once for user, Throw once for computer
# If user threw more print "YOU WIN!"
# If user threw les print "YOU LOST!"
# If user and computer threw the same print "IT'S A DRAW!"

import random

def dice():
    dice_me = random.randint(1,6)
    dice_computer = random.randint(1,6)
    if dice_me > dice_computer:
        return "You won"
    elif dice_me == dice_computer:
        return "It's a draw"
    else:
        return "You lost"

print(dice())


