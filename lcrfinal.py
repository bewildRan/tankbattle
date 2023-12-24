# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 10:46:32 2018

@author: g1927204
"""

import random
import math
import queue

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
             random.choice([self.robot.turnLeft,self.robot.turnRight])()
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
    
    def bfs(self,sx,sy,sr):
#        print(self.robot.lookAtSpace((sy,sx)))
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        dxF = [-1,0,1,0]
        dyF = [0,1,0,-1]
        
        dxB = [1,0,-1,0]
        dyB = [0,-1,0,1]
        
        d = [[[(None) for i in range(15)] for j in range(15)] for k in range(15)]
        
        
        q = queue.Queue() # 队列
        q.put((sx,sy,sr))
        d[sx][sy][sr] = 0
        
        while(q.empty()==False):
            x,y,r = q.get()
#            print([x,y,r])
            for k in range(4):
                if k==1:
                    #1 前进
                    x1 = x+dxF[r]
                    y1 = y+dyF[r]
                    r1 = r
                elif k==2:
                    #2 后退
                    x1 = x+dxB[r]
                    y1 = y+dyB[r]
                    r1 = r
                elif k==3:
                    #3 左转
                    x1 = x
                    y1 = y
                    r1 = (r - 1)%4
                else:
                    #4 右转
                    x1 = x
                    y1 = y
                    r1 = (r + 1)%4
#                print(self.robot.lookAtSpace((x1,y1)))
                if x1<1 or x1>10 or y1<1 or y1>10 or self.robot.lookAtSpace((y1,x1))=='wall':
                    continue
#                print([x1,y1,r1])
                if d[x1][y1][r1] is not None:
                    continue 
                d[x1][y1][r1] = d[x][y][r] + 1
                q.put((x1,y1,r1))
            
        return d
    def turn(self):
        p0 = self.robot.position   
        r0 = self.robot.rotation
        x0 = p0[0]
        y0 = p0[1]
        
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

    def turn(self):
        p0 = self.robot.position   
        r0 = self.robot.rotation
        x0 = p0[0]
        y0 = p0[1]
        
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


        
