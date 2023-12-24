"""
AI Name: Random AI

Made by: Carter

Strategy:
Move around randomly.
Attack any robot in front of you.
"""

import math

import random

class AI:
    def citurn(self):
#   
        
        if self.robot.lookInFront()== "wall":
            random.choice([self.robot.turnLeft,self.robot.turnRight])()
            return
        else:
            self.robot.goForth()
            

    def __init__(self):
        pass
    def turn(self):
        
        
        if self.robot.lookInFront() == "bot":
            mess=self.robot.detectEnemy()
        
            
            if mess[2]>140 or mess[3]>15 :
                self.robot.goBack()
            
            else:
                self.robot.attack()
        else:
            if(random.random()<0.5):
                self.citurn()
            else:
                self.goTowards(self.robot.locateEnemy()[0])
            
    def goTowards(self,enemyLocation):
        
        
            myLocation = self.robot.position
            delta = (enemyLocation[0]-myLocation[0],enemyLocation[1]-myLocation[1])
            if abs(delta[0]) > abs(delta[1]):
                if delta[0] < 0:
                    targetOrientation = 3 #face left
                else:
                    targetOrientation = 1 #face right
            else:
                if delta[1] < 0:
                    targetOrientation = 0 #face up
                else:
                    targetOrientation = 2 #face down
            if self.robot.rotation == targetOrientation:
                self.robot.goForth()
            else:
                leftTurnsNeeded = (self.robot.rotation - targetOrientation) % 4
                if leftTurnsNeeded <= 2:
                    self.robot.turnLeft()
                else:
                    self.robot.turnRight()  



