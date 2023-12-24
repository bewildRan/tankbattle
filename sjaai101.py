# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:38:57 2018

@author: g1826211
"""

import random
import math
import queue

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

        x,y=y,x
        d=AI.bfs(self,x,y,r)
        L = [([0]) for i in range (11)]
        ansx = -100
        ansy = -100
        ansr = -100
        dist0 = 100
        for a in range(1,11):
            for b in range (1,11):
                L[a].append(self.robot.lookAtSpace((b,a)))
                if L[a][b] is "ATK" or L[a][b] is "HP" or (self.robot.speedUP is 0 and L[a][b] is "SPD"):
                    for k in range(4):
                        dist1 = d[a][b][k]
                        if dist1 is None:
                            dist1 = 100
                        if dist1 < dist0:
                            dist0 = d[a][b][k]
                            ansx = a
                            ansy = b
                            ansr = k
        
        if ansx== -100 :
            if (self.robot.speedUP is 0):
                random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goBack])()
                return
            else:
                random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth2,self.robot.goBack2])()
                return

        
        print(ansx,ansy,ansr)
        d=AI.bfs(self,ansx,ansy,ansr)
        xf, yf= AI.calxy(x,y,r)
        xf2, yf2= AI.calxy(xf,yf,r)
        r1 = (r - 1)%4
        r2 = (r + 1)%4
        r3 = (r - 2) % 4
        xB, yB= AI.calxy(x,y,r3)
        xB2, yB2= AI.calxy(xB,yB,r3)
        if d[xf][yf][r] is None:
            d[xf][yf][r] = 100
        if d[xf2][yf2][r] is None or d[xf][yf][r] is 100:
            d[xf2][yf2][r] = 100
        if d[x][y][r1] is None:
            d[x][y][r1] = 100
        if d[x][y][r2] is None:
            d[x][y][r2] = 100
        if d[xB][yB][r] is None:
            d[xB][yB][r] = 100
        if d[xB2][yB2][r] is None or d[xB][yB][r] is 100:
            d[xB2][yB2][r] = 100
        
        if self.robot.speedUP == 1:
            if d[xf][yf][r] <= d[xf2][yf2][r] and d[xf][yf][r] <= d[x][y][r1] and d[xf][yf][r] <= d[x][y][r2] and d[xf][yf][r] <= d[xB][yB][r] and d[xf][yf][r] <= d[xB2][yB2][r]:
                self.robot.goForth()
                print("apple")
                return
            if d[xf2][yf2][r] <= d[xf][yf][r] and d[xf2][yf2][r] <= d[x][y][r1] and d[xf2][yf2][r] <= d[x][y][r2] and d[xf2][yf2][r] <= d[xB][yB][r] and d[xf2][yf2][r] <= d[xB2][yB2][r]:
                self.robot.goForth2()
                print("banana")
                return
            if d[x][y][r1] <= d[xf][yf][r] and d[x][y][r1] <= d[xf2][yf2][r] and d[x][y][r1] <= d[x][y][r2] and d[x][y][r1] <= d[xB][yB][r] and d[x][y][r1] <= d[xB2][yB2][r]:
                self.robot.turnLeft()
                return
            if d[x][y][r2] <= d[xf][yf][r] and d[x][y][r2] <= d[x][y][r1] and d[x][y][r2] <= d[xB][yB][r] and d[x][y][r2] <= d[xf2][yf2][r] and d[x][y][r2] <= d[xB2][yB2][r]:
                self.robot.turnRight()
                return
            if d[xB][yB][r] <= d[xf][yf][r] and d[xB][yB][r] <= d[x][y][r1] and d[xB][yB][r] <= d[x][y][r2] and d[xB][yB][r] <= d[xf2][yf2][r] and d[xB][yB][r] <= d[xB2][yB2][r]:
                self.robot.goBack()
                return
            if d[xB2][yB2][r] <= d[xf][yf][r] and d[xB2][yB2][r] <= d[x][y][r1] and d[xB2][yB2][r] <= d[x][y][r2] and d[xB2][yB2][r] <= d[xf2][yf2][r] and d[xB2][yB2][r] <= d[xB][yB][r]:
                self.robot.goBack2()
                return
        else:
            if d[xf][yf][r] <= d[x][y][r1] and d[xf][yf][r] <= d[x][y][r2] and d[xf][yf][r] <= d[xB][yB][r]:
                self.robot.goForth()
                print("coconut")
                return
            if d[x][y][r1] <= d[xf][yf][r] and d[x][y][r1] <= d[x][y][r2] and d[x][y][r1] <= d[xB][yB][r]:
                self.robot.turnLeft()
                return
            if d[x][y][r2] <= d[xf][yf][r] and d[x][y][r2] <= d[x][y][r1] and d[x][y][r2] <= d[xB][yB][r]:
                self.robot.turnRight()
                return
            if d[xB][yB][r] <= d[xf][yf][r] and d[xB][yB][r] <= d[x][y][r1] and d[xB][yB][r] <= d[x][y][r2]:
                self.robot.goBack()
                return
        print("orange")

    def bfs(self,sx,sy,sr):
        d = [[[(None) for i in range(15)] for j in range(15)] for k in range (15) ] 
        q = queue.Queue() # 队列
        d[sx][sy][sr] = 0
        
        dxF = [-1,0,1,0]
        dyF = [0,1,0,-1]
        dxB = [1,0,-1,0]
        dyB = [0,-1,0,1]
        q.put((sx,sy,sr))
        while(q.empty()==False):
            x,y,r = q.get()
            for k in range(4):
                if k == 0:
                    x1 =x +dxF[r]
                    y1 =y +dyF[r]
                    r1 =r
                if k ==1:
                    x1= x +dxB[r]
                    y1 = y +dyB[r]
                    r1 =r 
                if k ==2:
                    x1 = x
                    y1 = y
                    r1 = (r+1)%4
                if k == 3:
                    x1 =x
                    y1 =y
                    r1 = (r-1)%4
                if x1<1 or x1>10 or y1<1 or y1>10 or self.robot.lookAtSpace((y1,x1))=='wall' or self.robot.lookAtSpace((y1,x1))=='bot':
                    continue
                if d[x1][y1][r1]is not None:
                    continue 
                d[x1][y1][r1] = d[x][y][r] + 1
                q.put((x1,y1,r1))
        return d
    
    
    