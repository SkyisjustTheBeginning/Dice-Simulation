import random
import time
dice_possibilities = [1,2,3,4,5,6]
print("Dice is rolling.....")
time.sleep(2)
random.shuffle(dice_possibilities)
print(random.choice(dice_possibilities))
