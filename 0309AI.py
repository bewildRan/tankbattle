"""
AI Name: Random AI

Made by: Carter

Strategy:
Move around randomly.
Attack any robot in front of you.
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
        (p1,r1,HP1,ATK1,SPD1) = self.robot.detectEnemy()
        if math.ceil(HP1/ATK0) <= math.ceil(HP0/ATK1):
            return True
        else:
            return False
        
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
        
    def turn(self):
        p0 = self.robot.position   
        r0 = self.robot.rotation
        y0 = p0[0]
        x0 = p0[1]
        
        
        L = [([0]) for i in range(11)] #开11个新空班
        
        ansx = 5
        ansy = 5
        for x in range(1,11):
            for y in range(1,11):
                L[x].append(self.robot.lookAtSpace((y,x)))
                if L[x][y] is "ATK" or L[x][y] is "HP" or L[x][y] is "SPD":
                    dist1 = abs(x-x0) + abs(y-y0)
                    dist0 = abs(ansx-x0) + abs(ansy-y0)
                    if dist1 < dist0:
                        ansx = x
                        ansy = y
#        print(L)
        print(ansx,ansy)
        print(x0,y0)
        self.robot.doNothing()
        return
        
        x0,y0 = y0,x0
        
        (p1,r1) = self.robot.locateEnemy()
        x1 = p1[0]
        y1 = p1[1]
        
        if self.robot.lookInFront() is "bot":
            (xN,yN) = AI.calxy(x1,y1,r1)
            if xN!=x0 or yN!=y0 or AI.chk(self) is 1: 
                self.robot.attack()
            else:
                (xN,yN) = AI.calxy(x0,y0,r0)
                if xN<1 or xN>10 or yN<1 or yN>10 or self.robot.lookAtSpace((xN,yN)) is "wall":
                    self.robot.turnLeft()
                    return
                else:  
                    self.robot.goBack()
                    return
        #case1
        elif x1 is x0 and y1 is y0-1:
            if r0 is 0 and AI.chk(self):
                self.robot.turnLeft()
            else:
                self.robot.turnRight()
        #case2
        elif x1 is x0 and y1 is y0+1:
            if r0 is 0 and AI.chk(self):
                self.robot.turnRight()
            else:
                self.robot.turnLeft()
        #case3
        elif y1 is y0 and x1 is x0-1:
            if r0 is 1 and AI.chk(self):
                self.robot.turnLeft()
            else:
                self.robot.turnRight()
        #case4
        elif y1 is y0 and x1 is x0+1:
            if r0 is 1 and AI.chk(self):
                self.robot.turnRight()
            else:
                self.robot.turnLeft()     
        elif self.robot.lookInFront() is "HP" or self.robot.lookInFront() is "ATK" or self.robot.lookInFront() is "SPD":
            self.robot.goForth()
            return
        elif self.robot.lookInFront() is "wall":
            self.robot.turnLeft()  
            return
        else:
            SPD = self.robot.speedUP
            if SPD is 1:
                random.choice([self.robot.turnLeft,self.robot.goForth,self.robot.goBack,self.robot.goForth2,self.robot.goBack2])()
                return
            else:
                random.choice([self.robot.turnLeft,self.robot.goForth,self.robot.goBack])()
                return
#            random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goForth2])()
