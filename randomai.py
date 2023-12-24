"""
AI Name: Random AI

Made by: Carter

Strategy:
Move around randomly.
Attack any robot in front of you.
"""

import random

class AI:
    def __init__(self):
        #Anything the AI needs to do before the game starts goes here.
        pass
    def turn(self):
        p = self.robot.position        
#        print(p)
        x = p[0]
        y = p[1]
        (p,r) = self.robot.locateEnemy()
        print(p)
        x1 = p[0]
        y1 = p[1]
        r = self.robot.rotation
        
        if self.robot.lookInFront() is "bot":
            self.robot.attack()

            return
        #case1
        elif x1 is x and y1 is y-1:
            if r is 0:
                self.robot.turnLeft()
            else:
                self.robot.turnRight()
        #case2
        elif x1 is x and y1 is y+1:
            if r is 0:
                self.robot.turnRight()
            else:
                self.robot.turnLeft()
        #case3
        elif y1 is y and x1 is x-1:
            if r is 1:
                self.robot.turnLeft()
            else:
                self.robot.turnRight()
        #case4
        elif y1 is y and x1 is x+1:
            if r is 1:
                self.robot.turnRight()
            else:
                self.robot.turnLeft()     
        elif self.robot.lookInFront() is "HP" or self.robot.lookInFront() is "ATK" or self.robot.lookInFront() is "SPD":
            self.robot.goForth()
            return
        else:
            random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goBack])()
#            random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goForth2])()
