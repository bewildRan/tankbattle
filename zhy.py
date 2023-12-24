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
        if self.robot.lookInFront() == "bot":            
            self.robot.attack()
        elif self.robot.lookInFront() == "wall":            
                random.choice([self.robot.turnLeft,self.robot.turnRight])()
        elif self.robot.lookInFront() == "HP" :
            self.robot.goForth()
            return
        elif self.robot.lookInFront() == "SPD" :
            self.robot.goForth()
            return
        elif self.robot.lookInFront() == "ATK" :
            self.robot.goForth()
            return
        else:
            if self.robot.speedUP==0:
                self.robot.goForth()
            else:
                mylocation=self.robot.position
                a = self.robot.lookAtSpace((mylocation[0]+2,mylocation[1]))
                b = self.robot.lookAtSpace((mylocation[0]-2,mylocation[1]))
                c = self.robot.lookAtSpace((mylocation[0],mylocation[1]+2))
                d = self.robot.lookAtSpace((mylocation[0],mylocation[1]-2))
#                print(a)
                if a=="wall" or b=="wall" or c=="wall" or d=="wall" or mylocation[0]<=2 or mylocation[0]>=9 or mylocation[1]<=1 or mylocation[1]>=8:
                    self.robot.goForth()
                else:
                    self.robot.goForth2()
            

                
