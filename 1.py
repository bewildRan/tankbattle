"""
AI Name: Random AI

Made by: Carter

Strategy:
Move around randomly.
Attack any robot in front of you.
"""

import random
def myf():    
    pass
class AI:    
    def __init__(self):
        pass
    def turn(self):        
        if self.robot.lookInFront() is "bot":            
            self.robot.attack()
        elif self.robot.lookInFront() == "wall":            
            random.choice([self.robot.turnLeft,self.robot.turnRight])()
        elif self.robot.lookInFront() == "HP":
            self.robot.goForth()
            return
        elif self.robot.lookInFront() == "SPD" :
            self.robot.goForth()
            return
        elif self.robot.lookInFront() == "ATK" :
            self.robot.goForth()
            return
        else:
            self.robot.goForth()