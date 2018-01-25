#Game of Craps
#By Aifric Nolan

import random

def DiceRoll():
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    total = die1 + die2
    print "Player rolled %d + %d = %d" % (die1, die2, total)
    
    return total

#First dice roll    
sum = DiceRoll()

if sum == 7 or sum == 11:
    game_status = "WON"
elif sum == 2 or sum == 3 or sum == 12:
    game_status = "LOST"
else:
    game_status = "Continue"
    point = sum
    print "Point is", point

#Keep rolling    
while game_status == "Continue":
    sum = DiceRoll()
    
    if sum == point:            #Win by 'making point' 
        game_status = "WON" 
    elif sum == 7:                 #Lose by rolling a 7
        game_status = "LOST"
        
if game_status == "WON":
    print "Player wins!"
else:
    print "Player loses...."
        