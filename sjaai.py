# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 10:02:40 2018

@author: g1826211
"""

"""
AI Name: Null AI

Made by: Carter

Strategy:
Do nothing.
"""
import random
import math

class AI:
    
    def __init__(self):
        #Anything the AI needs to do before the game starts goes here.
        self.forward = 0
        pass
    def aiCheck(self):
        (p1,r1,HP1,ATK1,SPD1) = self.robot.detectEnemy()
        HP0 = self.robot.health
        ATK0 = self.robot.ATK
        if math.ceil(HP1/ATK0)<=math.ceil(HP0/ATK1):
            return 1
        else:
            return 0

    def turn(self):
        p=self.robot.position
#        print(p)
        x=p[0]
        y=p[1]
        (p1,r1)=self.robot.locateEnemy()
        r=self.robot.rotation
        print(p)
        if (self.forward == 1):
            self.robot.goForth()
            self.forward = 0
            return
        if (self.robot.lookInFront() == "bot"):
            if (self.aiCheck() == 1 ):
                self.robot.attack()
                return
            elif (r is 0):
                if (self.robot.lookAtSpace((x,y+1))is "wall"):
                    self.robot.turnLeft()
                    self.forward = 1
                    return
                else:
                    self.robot.goBack()
                    return
            elif (r is 1):
                if (self.robot.lookAtSpace ((x-1,y))is "wall"):
                    self.robot.turnLeft()
                    self.forward = 1
                    return
                else:
                    self.robot.goBack()
                    return
            elif (r is 2):
                if (self.robot.lookAtSpace ((x,y-1))is "wall"):
                    self.robot.turnLeft()
                    self.forward = 1
                    return
                else:
                    self.robot.goBack()
                    return
            elif (r is 3):
                if (self.robot.lookAtSpace ((x+1,y))is "wall"):
                    self.robot.turnLeft()
                    self.forward = 1
                    return
                else:
                    self.robot.goBack()
                    return
        if (self.robot.lookInFront() is "HP" or self.robot.lookInFront() is "ATK" or (self.robot.speedUP is 0 and self.robot.lookInFront() is "SPD")):
            self.robot.goForth()
            return

        if (self.robot.lookAtSpace((x,y-1)) is "bot" or self.robot.lookAtSpace((x,y-1)) is "ATK" or self.robot.lookAtSpace((x,y-1)) is "HP" or (self.robot.speedUP is 0 and self.robot.lookAtSpace((x,y-1)) is "SPD")):
            if r is 3:
                self.robot.turnRight()
                return
            else:
                self.robot.turnLeft()
                return
        elif (self.robot.lookAtSpace((x,y+1)) is "bot" or self.robot.lookAtSpace((x,y+1)) is "ATK" or self.robot.lookAtSpace((x,y+1)) is "HP" or (self.robot.speedUP is 0 and self.robot.lookAtSpace((x,y+1)) is "SPD")):
            if r is 3:
                self.robot.turnLeft()
                return
            else:
                self.robot.turnRight()
                return
        elif (self.robot.lookAtSpace((x-1,y)) is "bot" or self.robot.lookAtSpace((x-1,y)) is "ATK" or self.robot.lookAtSpace((x-1,y)) is "HP" or (self.robot.speedUP is 0 and self.robot.lookAtSpace((x-1,y)) is "SPD")):
            if r is 2:
                self.robot.turnRight()
                return
            else:
                self.robot.turnLeft()
                return
        elif (self.robot.lookAtSpace((x+1,y)) is "bot" or self.robot.lookAtSpace((x+1,y)) is "ATK" or self.robot.lookAtSpace((x+1,y)) is "HP" or (self.robot.speedUP is 0 and self.robot.lookAtSpace((x+1,y)) is "SPD")):
            if r is 2:
                self.robot.turnLeft()
                return
            else:
                self.robot.turnRight()
                return
        else:
            if (self.robot.lookInFront() is "wall"):
                self.robot.turnLeft()
                return
            if (self.robot.speedUP is 0):
                random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goBack])()
                return
            else:
                random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth2,self.robot.goBack2])()
                return