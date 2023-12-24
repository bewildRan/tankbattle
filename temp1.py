# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 12:04:02 2018

@author: 
"""

import random

class AI:
    def __init__(self):
        #Anything the AI needs to do before the game starts goes here.
        pass
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
    def turn(self):
        x=self.robot.position[0]
        y=self.robot.position[1]
        
        
        if self.robot.lookInFront() == "Wall":
            random.choice([self.robot.turnLeft,self.robot.turnRight])()
            return
        
        if self.robot.lookInFront() == "HP":
            self.robot.goForth()
        elif self.robot.lookAtSpace((x+1,y)) == "HP":
            self.goTowards((x+1,y))
            return
        elif self.robot.lookAtSpace((x,y+1)) == "HP":
            self.goTowards((x,y+1))
            return
        elif self.robot.lookAtSpace((x-1,y)) == "HP":
            self.goTowards((x-1,y))
            return
        elif self.robot.lookAtSpace((x+1,y-1)) == "HP":
            self.goTowards((x+1,y-1))
            return
        elif self.robot.lookAtSpace((x+1,y+1)) == "HP":
            self.goTowards((x+1,y+1))
            return
        elif self.robot.lookAtSpace((x-1,y-1)) == "HP":
            self.goTowards((x-1,y-1))
            return
        elif self.robot.lookAtSpace((x-1,y+1)) == "HP":
            self.goTowards((x-1,y+1))
            return


        elif self.robot.lookInFront() == "ATK":
            self.robot.goForth()
        elif self.robot.lookAtSpace((x+1,y)) == "ATK":
            self.goTowards((x+1,y))
            return
        elif self.robot.lookAtSpace((x,y+1)) == "ATK":
            self.goTowards((x,y+1))
            return
        elif self.robot.lookAtSpace((x-1,y)) == "ATK":
            self.goTowards((x-1,y))
            return
        elif self.robot.lookAtSpace((x+1,y-1)) == "ATK":
            self.goTowards((x+1,y-1))
            return
        elif self.robot.lookAtSpace((x+1,y+1)) == "ATK":
            self.goTowards((x+1,y+1))
            return
        elif self.robot.lookAtSpace((x-1,y-1)) == "ATK":
            self.goTowards((x-1,y-1))
            return
        elif self.robot.lookAtSpace((x-1,y+1)) == "ATK":
            self.goTowards((x-1,y+1))
            return
        elif self.robot.lookInFront() == "bot":
            self.robot.attack()
            return
        elif self.robot.lookAtSpace((x+1,y)) == "bot":
            self.robot.turnRight()
            return
        elif self.robot.lookAtSpace((x,y-1)) == "bot":
            self.robot.turnRight()
            return
        elif self.robot.lookAtSpace((x-1,y)) == "bot":
            self.robot.turnLeft()
        else:
            random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goForth2])()
#            random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goForth2])()
        


        
            








