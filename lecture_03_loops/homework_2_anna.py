# Write a program, that will simulate die throwing in Monopoly
# You will repeatedly throw 2 dies until you get 3 doubles (the same numbers on both dies) in the row.
# If you will get 3 doubles in the row, you end the program and print ("You go to jail!")

import random

dice_1 = random.randint(1,6)
dice_2 = random.randint(1,6)
i = 0
while dice_1 != dice_2:
    print (dice_1,dice_2)
    i += 1
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    if i == 3:
        print("You go to jail!")
        break
if i < 3:
    print(dice_1,dice_2)