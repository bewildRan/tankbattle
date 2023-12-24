# -*- coding: utf-8 -*-
import random
class AI:
    def __init__(self):
        #Anything the AI needs to do before the game starts goes here.
        pass
    
    def enemyLocated(self):
        global enemyNear
        global selfx
        global selfy
        obj1=self.robot.lookAtSpace((selfx,selfy+1))
        obj2=self.robot.lookAtSpace((selfx+1,selfy))
        obj3=self.robot.lookAtSpace((selfx-1,selfy))
        obj4=self.robot.lookAtSpace((selfx,selfy-1))
        obj5=self.robot.lookAtSpace((selfx+1,selfy+1))
        obj6=self.robot.lookAtSpace((selfx+1,selfy-1))
        obj7=self.robot.lookAtSpace((selfx-1,selfy+1))
        if obj1=='bot' or obj2=='bot' or obj3=='bot' or obj4=='bot':
            enemyNear=1
        if obj5=='bot' or obj6=='bot' or obj7=='bot' or self.robot.lookAtSpace((selfx-1,selfy-1))=='bot':
            enemyNear=3
        else:
            enemyNear=0
        return
    
    def propLocated(self):
        if self.robot.lookInFront()!='bot' and self.robot.lookInFront()!='clear' and self.robot.lookInFront()!='wall':
            return True
    def turn(self):
        
        global speed
        speed=1
        global side                  #red
        side=1
        global attack
        attack=10
        global face
        face=3
        
        global selfx
        selfx=10
        global selfy
        selfy=5
        
        global spdx
        spdx=0
        global spdy
        spdy=0
        
        global enemyx
        enemyx=1
        global enemyy
        enemyy=5
        
        global lasx
        global lasy
        
        global prex
        global prey

        global enemyNear       #not near
        enemyNear=0
        global wallLocated
        wallLocated=0
        global reachedcorner
        
        global speedturn
        global speedyturn
        global speeedyturn
        global attackturn
        attackturn=0
        global goForthtick
        
        #self.robot.health+=0.001
        #self.robot.ATK+=0.01
        
        Map=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        
        lasx=spdx
        lasy=spdy
            
        for i in range(1,10):
            for j in range(1,10):
                Map[i][j]=self.robot.lookAtSpace((i,j))
                if self.robot.lookAtSpace((i,j))=='SPD':
                    spdx=i
                    spdy=j
                elif self.robot.lookAtSpace((i,j))=='me':
                    selfx=i
                    selfy=j
                elif self.robot.lookAtSpace((i,j))=='enemy':
                    enemyx=i
                    enemyy=j
        
        if selfx==lasx and selfy==lasy:
            speed=2
        
        if self.robot.lookAtSpace((selfx,selfy))=='attack':
            attack*=2
        if self.robot.lookInFront()=='wall':
            wallLocated=1
        
        self.enemyLocated()
        
        goForthtick=0
        
        if self.robot.lookInFront() == "bot" and  self.robot.health*10>=self.robot.detectEnemy()[2]*self.robot.detectEnemy()[3]:
            self.robot.attack()
            return
        elif enemyNear!=0 and self.robot.lookInFront()=='bot' and self.robot.detectEnemy()[1]!=(face+2)%4 and self.robot.health*10<self.robot.detectEnemy()[2]*self.robot.detectEnemy()[3]:
            self.robot.goBack()
        elif enemyNear!=0 and self.robot.lookInFront()!='bot':
            if enemyx==selfx+1 and enemyy==selfy and self.robot.locateEnemy()[1]==(face+2)%4 and face==1 and attackturn==0:
                self.robot.goBack()
            elif enemyx==selfx+1 and enemyy==selfy and self.robot.locateEnemy()[1]==3 and face!=1 and attackturn==0:
                self.robot.goBack()
            elif enemyx==selfx+1 and enemyy==selfy and self.robot.locateEnemy()[1]!=3 and face!=1 and attackturn==0:
                self.robot.goBack()
            elif enemyx==selfx-1 and enemyy==selfy and self.robot.locateEnemy()[1]==1 and face==3 and attackturn==0:
                self.robot.goBack()
            elif enemyx==selfx-1 and enemyy==selfy and self.robot.locateEnemy()[1]==1 and face!=3 and attackturn==0:
                self.robot.goBack()
            elif enemyx==selfx-1 and enemyy==selfy and self.robot.locateEnemy()[1]!=1 and face!=3 and attackturn==0:
                self.robot.goBack()
            elif enemyx==selfx and enemyy==selfy+1 and self.robot.locateEnemy()[1]==0 and face==2 and attackturn==0:
                self.robot.goBack()
            elif enemyx==selfx and enemyy==selfy+1 and self.robot.locateEnemy()[1]==0 and face!=2 and attackturn==0:
                self.robot.goBack()
            elif enemyx==selfx and enemyy==selfy+1 and self.robot.locateEnemy()[1]!=0 and face!=2 and attackturn==0:
                self.robot.goBack()
            elif enemyx==selfx and enemyy==selfy-1 and self.robot.locateEnemy()[1]==2 and face==0 and attackturn==0:
                self.robot.goBack()
            elif enemyx==selfx and enemyy==selfy-1 and self.robot.locateEnemy()[1]==2 and face!=0 and attackturn==0:
                self.robot.goBack()
            elif enemyx==selfx and enemyy==selfy-1 and self.robot.locateEnemy()[1]!=2 and face!=0 and attackturn==0:
                self.robot.goBack()
            elif enemyx==selfx+1 and enemyy==selfy+1:
                self.robot.doNothing()
            elif enemyx==selfx+1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==3 and face==0 and attackturn==0:
                self.robot.goForth()
            elif enemyx==selfx+1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==3 and face==3 and attackturn==0:
                self.robot.goForth()
            elif enemyx==selfx+1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==2 and face==1 and attackturn==0:
                self.robot.goForth()
            elif enemyx==selfx+1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==2 and face==0 and attackturn==0:
                self.robot.goForth()
            elif enemyx==selfx+1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==2 and face==3 and attackturn==0:
                self.robot.goForth()
            elif enemyx==selfx+1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==2 and face==2 and attackturn==0:
                self.robot.goForth()
            elif enemyx==selfx+1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==1 and attackturn==0:
                self.robot.goForth()
            elif enemyx==selfx+1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==0 and face==2 and attackturn==0:
                self.robot.goForth()
            elif enemyx==selfx+1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==0 and face==3 and attackturn==0:
                self.robot.goForth()
            elif enemyx==selfx-1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==3:
                self.robot.goForth()
            elif enemyx==selfx-1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==2:
                self.robot.goForth()
            elif enemyx==selfx-1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==1 and face!=2:
                self.robot.goForth()
            elif enemyx==selfx-1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==1 and face==2:
                self.robot.doNothing()
            elif enemyx==selfx-1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==0 and face!=3:
                self.robot.goForth()
            elif enemyx==selfx-1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==0 and face==3:
                self.robot.doNothing()
            elif enemyx==selfx+1 and enemyy==selfy-1 and self.robot.locateEnemy()[1]==3 and face!=0:
                self.robot.goForth()
            elif enemyx==selfx+1 and enemyy==selfy-1 and self.robot.locateEnemy()[1]==3 and face==0:
                self.robot.doNothing()
            elif enemyx==selfx+1 and enemyy==selfy-1 and self.robot.locateEnemy()[1]==2 and face!=1:
                self.robot.goForth()
            elif enemyx==selfx+1 and enemyy==selfy-1 and self.robot.locateEnemy()[1]==2 and face==1:
                self.robot.doNothing()
            elif enemyx==selfx+1 and enemyy==selfy-1 and self.robot.locateEnemy()[1]==1:
                self.robot.goForth()
            elif enemyx==selfx+1 and enemyy==selfy+1 and self.robot.locateEnemy()[1]==0:
                self.robot.goForth()
            elif enemyx==selfx-1 and enemyy==selfy-1 and self.robot.locateEnemy()[1]==3:
                self.robot.goForth()
            elif enemyx==selfx-1 and enemyy==selfy-1 and self.robot.locateEnemy()[1]==2 and face!=3:
                self.robot.goForth()
            elif enemyx==selfx-1 and enemyy==selfy-1 and self.robot.locateEnemy()[1]==2 and face==3:
                self.robot.doNothing()
            elif enemyx==selfx-1 and enemyy==selfy-1 and self.robot.locateEnemy()[1]==1 and face!=0:
                self.robot.goForth()
            elif enemyx==selfx-1 and enemyy==selfy-1 and self.robot.locateEnemy()[1]==1 and face==0:
                self.robot.doNothing()
            elif enemyx==selfx-1 and enemyy==selfy-1 and self.robot.locateEnemy()[1]==0:
                self.robot.goForth()
            elif self.robot.lookInFront()=='wall':
                self.robot.turnLeft()
            else:
                self.robot.doNothing()
        elif enemyNear==0 and self.robot.lookInFront()!='wall' and self.propLocated()==True and goForthtick<=random.choice([4,5,6,7,8,9,10]):
            self.robot.goForth()
            goForthtick+=1
        elif enemyNear==0 and self.robot.lookInFront()!='wall' and self.propLocated()!=True and goForthtick<=random.choice([4,5,6,7,8,9,10]):
            self.robot.goForth()
            goForthtick+=1
        elif enemyNear==0 and self.robot.lookInFront()!='wall' and goForthtick>=random.choice([4,5,6,7,8,9,10]):
            random.choice([self.robot.turnLeft,self.robot.turnRight])()
        elif self.robot.lookInFront()=='wall':
            random.choice([self.robot.turnLeft,self.robot.turnRight])()
        return