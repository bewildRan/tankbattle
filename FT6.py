"""
AI Name: Random AI

Made by: Carter

Strategy:
Move around randomly.
Attack any robot in front of you.
"""

import random
import math
import queue

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
        y0 = p0[0]
        x0 = p0[1]
        spd = self.robot.speedUP
        pe = self.robot.locateEnemy()
        ye = pe[0][0]
        xe = pe[0][1]
        re = pe[1]
        print(pe)
        d = AI.bfs(self,x0,y0,r0)

#        self.robot.doNothing()
#        return
        L = [([0]) for i in range(11)] #开11个新空班
        
        ansx = -100
        ansy = -100
        ansr = -10
        dist0 = 1000
        for x in range(1,11):
            for y in range(1,11):
                L[x].append(self.robot.lookAtSpace((y,x)))
                if L[x][y] is "ATK" or L[x][y] is "HP" or L[x][y] is "SPD":
                    for r in range(4):                
                        dist1 = d[x][y][r]
                        if dist1 < dist0:
                            dist0 = d[x][y][r]
                            ansx = x
                            ansy = y
                            ansr = r
#        print(L)
#  物品位置(ansx,ansy);自己位置(x0,y0)，方向r0; 
#        print(ansx,ansy)
#        print(x0,y0)
#        self.robot.doNothing()
        
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
        
        xf,yf = AI.calxy(x0,y0,r0)
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
            xR,yR = AI.calxy(x0,y0,r2)
            if AI.calD(xR,yR,xe,ye) < AI.calD(x0,y0,xe,ye):
                    self.robot.turnRight()
                    return
        
        print(ansx,ansy,ansr)
        d = AI.bfs(self,ansx,ansy,ansr)
        print(d[x0][y0][r0])
        
        if d[x0][y0][r0]==None:
            self.robot.doNothing()
            return
        
        #  前方位置(xf,yf);
        xf,yf = AI.calxy(x0,y0,r0)
        xf2,yf2 = AI.calxy(xf,yf,r0)
        print(['f',d[xf][yf][r0]])
#        if d[xf][yf][r0]!=None and d[xf][yf][r0] < d[x0][y0][r0]:
#            self.robot.goForth()
#            return
        
        # r1 左转之后的方向
        r1 = (r0-1)%4  
        #  左转之后往前走一步(xL,yL);  
        xL,yL = AI.calxy(x0,y0,r1) #左边格子位置
        print(['l',d[xL][yL][r1]])
#        if d[xL][yL][r1]!=None and d[xL][yL][r1] < d[x0][y0][r0]:
#            self.robot.turnLeft()
#            return
        
        # r2 右转之后的方向
        r2 = (r0+1)%4
        xR,yR = AI.calxy(x0,y0,r2) #右边格子位置
        print(['r',d[xR][yR][r2]])
#        if d[xR][yR][r2]!=None and d[xR][yR][r2] < d[x0][y0][r0]:
#            self.robot.turnRight()
#            return
        
        
        # 后方方向
        r3 = (r0+2)%4
        xB,yB = AI.calxy(x0,y0,r3) #后方格子位置
        print(['b',d[xB][yB][r0]])
#        if d[xB][yB][r0]!=None and d[xB][yB][r0] < d[x0][y0][r0]:
#            if self.robot.lookAtSpace((yB,xB)) is "bot" or "wall":
#                random.choice([self.robot.turnLeft,self.robot.goForth,self.robot.goBack,self.robot.goForth2,self.robot.goBack2])()
#                return
#            self.robot.goBack()
#            return
        
        if d[xf][yf][r0] is None:
            d[xf][yf][r0] = 100
        if d[xL][yL][r1] is None:
            d[xL][yL][r1] = 100
        if d[xR][yR][r2] is None:
            d[xR][yR][r2] = 100
        if d[xB][yB][r0] is None:
            d[xB][yB][r0] = 100
        
        if d[xf][yf][r0] <= d[xL][yL][r1] and d[xf][yf][r0] <= d[xR][yR][r2] and d[xf][yf][r0] <= d[xB][yB][r0]:
            self.robot.goForth()
            return
        if d[xL][yL][r1] <= d[xf][yf][r0] and d[xL][yL][r1] <= d[xR][yR][r2] and d[xL][yL][r1] <= d[xB][yB][r0]:
            self.robot.turnLeft()
            return
        if d[xR][yR][r2] <= d[xf][yf][r0] and d[xR][yR][r2] <= d[xL][yL][r1] and d[xR][yR][r2] <= d[xB][yB][r0]:
            self.robot.turnLeft()
            return
        if d[xB][yB][r0] <= d[xf][yf][r0] and d[xB][yB][r0] <= d[xL][yL][r1] and d[xB][yB][r0] <= d[xR][yR][r2]:
            if self.robot.lookAtSpace((yB,xB)) is "bot" or "wall":
                random.choice([self.robot.turnLeft,self.robot.goForth,self.robot.goBack,self.robot.goForth2,self.robot.goBack2])()
                return
            self.robot.goBack()
            return
        random.choice([self.robot.turnLeft,self.robot.goForth,self.robot.goBack,self.robot.goForth2,self.robot.goBack2])()
        return