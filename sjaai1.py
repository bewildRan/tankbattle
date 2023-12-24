# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:38:57 2018

@author: g1826211
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

    def calD(a,b,x,y):
        return abs(a-x) + abs(b-y)

    def turn(self):
        p=self.robot.position
        r=self.robot.rotation
#        print(p)
        print(p,r)
        x=p[0]
        y=p[1]
        (p1,r1)=self.robot.locateEnemy()
        if (self.forward == 1):
            self.robot.goForth()
            self.forward = 0
            return
        if (self.robot.lookInFront() == "bot"):
            x1=p1[1]
            y1=p1[0]
            if (self.aiCheck() == 1 or AI.calxy(x1,y1,r1) != (y,x)):
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
                return
        x,y=y,x
        L = [([0]) for i in range (11)]
        ansx = -100
        ansy = -100
        for a in range(1,11):
            for b in range (1,11):
                L[a].append(self.robot.lookAtSpace((b,a)))
                if L[a][b] is "ATK" or L[a][b] is "HP" or (self.robot.speedUP is 0 and L[a][b] is "SPD"):
                    dist0 = abs(a-x) + abs(b-y)
                    dist1 = abs(ansx-x) + abs(ansy-y)
                    if dist0 < dist1:
                            ansx = a
                            ansy = b
        
        if ansx== -100 and ansy ==-100:
            if (self.robot.speedUP is 0):
                random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goBack])()
                return
            else:
                random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth2,self.robot.goBack2])()
                return

        print(ansx, ansy)
        xf, yf= AI.calxy(x,y,r)
        xf2, yf2= AI.calxy(xf,yf,r)
        if AI.calD(xf2,yf2,ansx,ansy) < AI.calD(x,y,ansx,ansy) and self.robot.speedUP is 1:
            if self.robot.lookAtSpace((yf,xf))!="wall" and self.robot.lookAtSpace((yf2,xf2))!="wall":
                self.robot.goForth2()
                return
            else:
                random.choice([self.robot.turnLeft,self.robot.turnRight])()
                self.forward = 1
                return
        if AI.calD (xf, yf, ansx, ansy) < AI.calD(x,y,ansx,ansy):
            if self.robot.lookAtSpace((yf,xf))!="wall":
                self.robot.goForth()
                return
            else:
                random.choice([self.robot.turnLeft,self.robot.turnRight])()
                self.forward = 1
                return
    
        r1 = (r - 1)%4
            
        xL,yL = AI.calxy(x,y,r1)
        if AI.calD(xL,yL,ansx,ansy) < AI.calD(x,y,ansx,ansy):
            self.robot.turnLeft()
            return
        
        r2 = (r + 1)%4
        xR, yR = AI.calxy(x,y,r2)
        if AI.calD (xR,yR,ansx,ansy) < AI.calD(x,y,ansx,ansy):
            self.robot.turnRight()
            return
        
        r3 = (r - 2) % 4
        xB, yB= AI.calxy(x,y,r3)
        xB2, yB2= AI.calxy(xB,yB,r3)
        if AI.calD(xB2,yB2,ansx,ansy) < AI.calD(x,y,ansx,ansy) and self.robot.speedUP is 1:
            if self.robot.lookAtSpace((yB,xB))!="wall" and self.robot.lookAtSpace((yB2,xB2))!="wall":
                self.robot.goBack2()
                return
            else:
                random.choice([self.robot.turnLeft,self.robot.turnRight])()
                self.forward = 1
                return
        if AI.calD (xB, yB, ansx, ansy) < AI.calD(x,y,ansx,ansy):
            if self.robot.lookAtSpace((yB,xB))!="wall":
                self.robot.goBack()
                return
            else:
                random.choice([self.robot.turnLeft,self.robot.turnRight])()
                self.forward = 1
                return
        if (self.robot.speedUP is 0):
            random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goBack])()
            return
        else:
            random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth2,self.robot.goBack2])()
            return