# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 10:01:58 2018

@author: g1921231
"""


import random
import math

class AI:
    def __init__(self):
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
    def calD(x0,y0,x1,y1):
        return abs(x1-x0) + abs(y1-y0)    
        
    def turn(self):
        p0 = self.robot.position   
        r0 = self.robot.rotation
        y0 = p0[0]
        x0 = p0[1]
        spd = self.robot.speedUP
        
        
                
        L = [([0]) for i in range(11)]#开11个新空班
        
        ansx = -100
        ansy = -100
        for x in range (1,11):
            for y in range(1,11):
                L[x].append(self.robot.lookAtSpace((y,x)))
                if L[x][y] is  "ATK" or L[x][y] is "HP" or L [x][y] is "SPD":
                    dist1 = abs(x-x0) + abs(y-y0)
                    dist0 = abs(ansx-x0) + abs(ansy-y0)
                    if dist1 < dist0:
                        ansx = x
                        ansy = y
                        
        #print(L)
        #物品位置（ansx，ansy）；自己位置（x0，y0），方向r0；
        print(ansx,ansy)
        print(x0,y0)
        if self.robot.lookInFront() is "bot":
            self.robot.attack()
            return
        
        if ansx == -100 and ansy == -100:
            random.choice([self.robot.turnLeft,self.robot.goForth,self.robot.goBack,self.robot.goForth2,self.robot.goBack2])()
            return
        
        # 前方位置（xf，yf）；
        xf,yf = AI.calxy(x0,y0,r0)
        if AI.calD(xf,yf,ansx,ansy) < AI.calD(x0,y0,ansx,ansy):
            self.robot.goForth()
            return
        
        # r1 左转之后的方向;
        if r0==0:
            r1=3
        else:
            r1=r0-1
            
        # 左转之后往前走一步(xL,yL);  
        xL,yL = AI.calxy(x0,y0,r1)#左边格子位置
        if AI.calD(xL,yL,ansx,ansy) < AI.calD(x0,y0,ansx,ansy):
            self.robot.turnLeft()
            return
        
        # r2 右转之后的方向；
        r2 = (r0+1)%4
        xR,yR = AI.calxy(x0,y0,r2)#右边格子位置
        if AI.calD(xR,yR,ansx,ansy) < AI.calD(x0,y0,ansx,ansy):
            self.robot.turnRight()
            return
        
        # 后方方向
        r3 = (r0+2)%4
        xB,yB = AI.calxy(x0,y0,r3)
        xB2,yB2 = AI.calxy(xB,yB,r3)
        if AI.calD(xB2,yB2,ansx,ansy) < AI.calD(xB,yB,ansx,ansy):
            self.robot.goBack()
            return

                
        
        
       
             
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