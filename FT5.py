# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 09:53:34 2018

@author: g1923128
"""
import random
import math
import traceback

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
        try:
            p0 = self.robot.position   
            r0 = self.robot.rotation
            y0 = p0[0]
            x0 = p0[1]
            pe = self.robot.locateEnemy()
            ye = pe[0][0]
            xe = pe[0][1]
            re = pe[1]
            print(pe)
            L = [([0]) for i in range(11)] #开11个新空班
            
            ansx = -100
            ansy = -100
            
            if self.robot.detectEnemy() != None:
                E = self.robot.detectEnemy()
                print(E)
                HP = E[2]
                
                H = self.robot.health
                
                
                
                if self.robot.lookInFront() is "bot" :
                    if HP < H:
                        self.robot.attack()
                        return
                    if abs(r0-re) != 2:
                        self.robot.attack()
                        return
                if self.robot.lookInFront() is "bot":
                    if HP > H:
                        self.robot.goBack()
                        return
            
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
            xf,yf = AI.calxy(x0,y0,r0)
            print(xf)
            if ansx==-100 and ansy==-100:
                if (AI.calD(xf,yf,xe,ye) - AI.calD(x0,y0,xe,ye) >= 2) and (self.robot.speedUp == 1):
                    self.robot.goForth2()
                
                    return
                if AI.calD(xf,yf,xe,ye) < AI.calD(x0,y0,xe,ye):
                    self.robot.goForth()
                    return
                if r0==0:
                    r1=3
                else:
                    r1=r0-1
                xL,yL = AI.calxy(x0,y0,r1)
                if AI.calD(xL,yL,xe,ye) < AI.calD(x0,y0,xe,ye):
                    self.robot.turnLeft()
                    return
                r2 = (r0+1)%4
                xL,yL = AI.calxy(x0,y0,r2)
                if AI.calD(xL,yL,xe,ye) < AI.calD(x0,y0,xe,ye):
                    self.robot.turnRight()
                    return
            
          
           
            if AI.calD(xf,yf,ansx,ansy) - AI.calD(x0,y0,ansx,ansy) >= 2 and self.robot.speedUp == 1:
                self.robot.goForth2()
                return
            if AI.calD(xf,yf,ansx,ansy) < AI.calD(x0,y0,ansx,ansy):
                self.robot.goForth()
                return
            
            # r1 左转之后的方向
            if r0==0:
                r1=3
            else:
                r1=r0-1
                
            #  左转之后往前走一步(xL,yL);  
            xL,yL = AI.calxy(x0,y0,r1)
            if AI.calD(xL,yL,ansx,ansy) < AI.calD(x0,y0,ansx,ansy):
                self.robot.turnLeft()
                return
            r2 = (r0+1)%4
            xL,yL = AI.calxy(x0,y0,r2)
            if AI.calD(xL,yL,ansx,ansy) < AI.calD(x0,y0,ansx,ansy):
                self.robot.turnRight()
                return
            
            
            self.robot.goBack()
            return
        except:
            traceback.print_exc()
        
                                                                           