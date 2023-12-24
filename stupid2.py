# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 08:04:02 2018

@author: xyy
"""

# Listing 26-2
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# PythonBattle AI - second attempt to beat CircleAI

# Note that this is not a complete Python program itself,
#   it is a module called by the PythonBattle program.
# Save this as something like "morecomplicatedai.py"
#   and try it in a battle against circleai.

import random
class AI:
    def __init__(self):
        pass

    def turn(self):

#纵观全局
            objHPs = []
            objATKs = []
            objSPDs = []
            me = []
            en = []
            

            for i in range(1,11):
                for j in range(1,11):
                    obj = self.robot.lookAtSpace((i,j))
                    if obj == "HP":
                        objHPs.append((i,j))
                    if obj == "ATK":
                        objATKs.append((i,j))
                    if obj == "SPD":
                        objSPDs.append((i,j))
                    if obj == "bot":
                        Xe = i
                        Ye = j
                    if obj == "me":
                        Xm = i
                        Ym = j
#1吃血包                   
            if len(objHPs)>0:
                for i in objHPs:
                    if (abs(Xm-i[0]) + abs(Ym-i[1])) <= (abs(Xe-i[0]) + abs(Ye-i[1])):
                        self.goTowards(i) 
#                        if self.robot.lookInFront()== "wall":
#                            self.robot.turnRight()
#                            return
#                            if self.robot.lookInFront()== "wall": #如果左转后还遇到墙，再左转
#                                self.robot.turnRight()
#                                return
#                        else:
#                            self.robot.goTowards(i)
#                            return
                        
                    #如果血包离我近就去吃否则向前走
#            else:
#                self.robot.goForth()
#                return
#                if self.robot.lookInFront() == "bot": #向前走如果遇到敌人就攻击，遇到墙就左转
#                    self.robot.attack()
#                    return
#                elif self.robot.lookInFront()== "wall":
#                    self.robot.turnRight()
#                    return
#                    
#               
#                    if self.robot.lookInFront()== "wall": #如果左转后还遇到墙，再左转
#                        self.robot.turnRight()
#                        return
#                else:
#                    self.robot.doNothing()
#                    return


            elif len(objATKs)>0:
                for i in objATKs:
                    if (abs(Xm-i[0]) + abs(Ym-i[1])) <= (abs(Xe-i[0]) + abs(Ye-i[1])):
                        self.goTowards(i) 
                        if self.robot.lookInFront()== "wall":
                            random.choice([self.robot.turnRight, self.robot.turnLeft])()
                            return
                    
                        else:
                            self.robot.goTowards(i)
                            return
                        
                    #如果血包离我近就去吃否则向前走
#            else:
#                self.robot.goForth()
#                return
#                if self.robot.lookInFront() == "bot": #向前走如果遇到敌人就攻击，遇到墙就左转
#                    self.robot.attack()
#                    return
#                elif self.robot.lookInFront()== "wall":
#                    self.robot.turnRight()
#                    return
#                    
#               
#                    if self.robot.lookInFront()== "wall": #如果左转后还遇到墙，再左转
#                        self.robot.turnRight()
#                        return
#                else:
#                    self.robot.doNothing()
#                    return


            elif len(objSPDs)>0:
                for i in objSPDs:
                    if (abs(Xm-i[0]) + abs(Ym-i[1])) <= (abs(Xe-i[0]) + abs(Ye-i[1])):
                        self.goTowards(i) 
                        if self.robot.lookInFront()== "wall":
                            random.choice([self.robot.turnRight, self.robot.turnLeft])()
                        else:
                            self.robot.goTowards(i)
                            return
                        
                    #如果血包离我近就去吃否则向前走
            else:
                for i in me:
                    i = 5
                   
                    self.gotowards(i)
                    if self.robot.lookInFront()== "wall":
                            random.choice([self.robot.turnRight, self.robot.turnLeft])()
                    else:
                        self.robot.goTowards(i)
                        return
#                self.robot.goForth()
#                return
#                if self.robot.lookInFront() == "bot": #向前走如果遇到敌人就攻击，遇到墙就左转
#                    self.robot.attack()
#                    return
#                elif self.robot.lookInFront()== "wall":
#                    self.robot.turnRight()
#                    return
#                    
#               
#                    if self.robot.lookInFront()== "wall": #如果左转后还遇到墙，再左转
#                        self.robot.turnRight()
#                        return
#                else:
#                    self.robot.doNothing()
#                    return



    def goTowards(self,enemyLocation):
        myLocation = self.robot.position
        delta = (enemyLocation[0]-myLocation[0],enemyLocation[1]-myLocation[1])
        if abs(delta[0]) > abs(delta[1]):
            if delta[0] < 0:
                targetOrientation = 3 #face left
            else:
                targetOrientation = 1 #face right
        else:
            if delta[1] < 0:
                targetOrientation = 0 #face up
            else:
                targetOrientation = 2 #face down
        if self.robot.rotation == targetOrientation:
            self.robot.goForth()
            
        else:
            leftTurnsNeeded = (self.robot.rotation - targetOrientation) % 4
            if leftTurnsNeeded <= 2:
                self.robot.turnLeft()
                return
            else:
                self.robot.turnRight()
                return
