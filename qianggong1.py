# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:51:48 2018

@author: g1927204
"""
import random
import math

class AI:  
    def __init__(self):
        #Anything the AI needs to do before the game starts goes here.
        pass
    
    def chk(self):
        HP0 = self.robot.health
        ATK0 = self.robot.ATK
        (p1,r1,HP1,SPD1,ATK1) = self.robot.detectEnemy()
#        print(HP0,HP1)
        if math.ceil(HP1/ATK0) <= math.ceil(HP0/ATK1):
            self.robot.attack()
        else:
            self.robot.goBack()
    
    def turn(self):
        p = self.robot.position
        print(p)
        x = p[0]
        y = p[1]
        (p,r)=self.robot.locateEnemy()
        x1 = p[0]
        y1 = p[1]
        print(p)
        r = self.robot.rotation         
        if self.robot.lookInFront()is "HP" or self.robot.lookInFront()is "SPD" or self.robot.lookInFront()is "ATK":
             self.robot.goForth()
             return
        elif self.robot.lookInFront() is "bot":
             self.robot.attack()
             return
        elif self.robot.lookInFront() is "wall":
             random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goForth2])()
        elif (x1 is x and y1 is y-1):
            if r is 0:
                self.robot.turnLeft()
            else:
                self.robot.turnRight()
        elif (x1 is x and y is y1-1):              
            if r is 0:
                self.robot.turnRight()
            else:
                self.robot.turnLeft()
        elif (y1 is y and x1 is x-1):
            if r is 0:
                self.robot.turnLeft()
            else:
                self.robot.turnRight()
        elif (y1 is y and x is x1-1):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            if r is 0:
                self.robot.turnRight()
            else:
                self.robot.turnLeft()
        else:
              self.robot.goForth()
              
    def calxy(x,y,r):
        if r==0:
            xN = x-1
            yN = y
        elif r==1:
            xN = x
            yN = y+1
        elif r==2:
            xN = x+1
            yN = y
        elif r==3:
            xN = x
            yN = y-1
        return xN,yN
    def calD(x0,y0,x1,y1):
        return abs(x1-x0) + abs(y1-y0)    

