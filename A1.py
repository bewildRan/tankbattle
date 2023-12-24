# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:00:55 2018

@author: g1923128
"""

class AI:
    def _init_(self):
        pass
    def turn(self):
        (p,r)=self.robot.locateEnemy()

        x=p[1]

        y=p[0]

        p1=self.robot.position
        x1=p1[1]
        y1=p1[0]
       
        r1=self.robot.rotation
        print (x,y,x1,y1,r1)

        if self.robot.lookInFront() is "bot":
            self.robot.attack()
            return
        if x-x1>0:
            if r1 is 0:
                self.robot.turnRight()
            elif r1 is 1:
                self.robot.turnRight()
            elif r1 is 2:
                self.robot.goForth()
            elif r1 is 3:
                self.robot.turnLeft()
        elif x-x1<0:
            if r1 is 0:
                self.robot.goForth()
            elif r1 is 1:
                self.robot.turnLeft()
            elif r1 is 2:
                self.robot.turnRight()
            elif r1 is 3:
                self.robot.turnRight()
        elif x-x1 is 0:
            if y-y1>0:
                if r1 is 0:
                    self.robot.turnRight()
                elif r1 is 1:
                    self.robot.goForth()
                elif r1 is 2:
                    self.robot.turnLeft()
                elif r1 is 3:
                    self.robot.turnLeft()
            elif y-y1<0:
                if r1 is 0:
                    self.robot.turnLeft()
                elif r1 is 1:
                    self.robot.turnLeft()
                elif r1 is 2:
                    self.robot.turnRight()
                elif r1 is 3:
                    self.robot.goForth()
                
        