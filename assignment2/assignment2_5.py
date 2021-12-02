import random
dice = random.randint(1,6)
if dice == 6:
    print("Yay!", dice,"!", "you can do it again!")
    dice = random.randint(1,6)
    print(dice)    
else:
    print(dice)