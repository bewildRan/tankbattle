# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 10:22:38 2018

@author: g1826211
"""
import random

class AI:
    def __init__(self):
        #Anything the AI needs to do before the game starts goes here.
        pass
        
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
        y0 = p0[0]
        x0 = p0[1]
        p = self.robot.position
        print(p)
        x = p[0]
        y = p[1]
        (p,r)=self.robot.locateEnemy()
        print(p)
        x1 = p[0]
        y1 = p[1]
        

        r = self.robot.rotation         
        if (x1 is x and y1 is y-1):
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
              
        l = [([]) for i in range(10)]
        for x in range(10):
            for y in range(10):
                l[x].append(self.robot.lookAtSpace([x,y]))
        print(l)
     
          
        p0 = self.robot.position   
        r0 = self.robot.rotation
        y0 = p0[0]
        x0 = p0[1]
        spd = self.robot.speedUP
        
        
        L = [([0]) for i in range(11)] #开11个新空班
        
        ansx = -100
        ansy = -100
        for x in range(1,11):
            for y in range(1,11):
                L[x].append(self.robot.lookAtSpace((y,x)))
                if L[x][y] is "ATK" or L[x][y] is "HP" or L[x][y] is "SPD":
                    dist1 = AI.calD(x0,y0,x,y)
                    dist0 = AI.calD(x0,y0,ansx,ansy)
                    if dist1 < dist0:
                        ansx = x
                        ansy = y
#        print(L)
#  物品位置(ansx,ansy);自己位置(x0,y0)，方向r0; 
        print(ansx,ansy)
        print(x0,y0)
             
        if self.robot.lookInFront() is "bot":
            self.robot.attack()
            return
        
        
        if ansx==-100 and ansy==-100:
            random.choice([self.robot.turnLeft,self.robot.goForth,self.robot.goBack,self.robot.goForth2,self.robot.goBack2])()
            return

        #  前方位置(xf,yf);
        xf,yf = AI.calxy(x0,y0,r0)
        xf2,yf2 = AI.calxy(xf,yf,r0)
        if AI.calD(xf,yf,ansx,ansy) < AI.calD(x0,y0,ansx,ansy):
            if spd and AI.calD(xf2,yf2,ansx,ansy) < AI.calD(xf,yf,ansx,ansy):
                self.robot.goForth2()
            else:
                self.robot.goForth()
            return
        
        # r1 左转之后的方向
        if r0==0:
            r1=3
        else:
            r1=r0-1
            
        #  左转之后往前走一步(xL,yL);  
        xL,yL = AI.calxy(x0,y0,r1) #左边格子位置
        if AI.calD(xL,yL,ansx,ansy) < AI.calD(x0,y0,ansx,ansy):
            self.robot.turnLeft()
            return
        
        # r2 右转之后的方向
        r2 = (r0+1)%4
        xR,yR = AI.calxy(x0,y0,r2) #右边格子位置
        if AI.calD(xR,yR,ansx,ansy) < AI.calD(x0,y0,ansx,ansy):
            self.robot.turnRight()
            return