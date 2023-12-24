# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 00:25:40 2018

@author: 飞飞铎
"""
import random
class AI:
    def __init__(self):
        #Anything the AI needs to do before the game starts goes here.
        self.currentlyDoing=""
        pass
    def turn(self):
        x=self.robot.position[0]
        y=self.robot.position[1]
        
        
        if self.robot.rotation ==0:
            if self.robot.lookInFront() == "bot":
                self.robot.attack()
                return
            elif self.robot.lookAtSpace((x+1,y)) == "bot":
                self.robot.turnRight()
                return
            elif self.robot.lookAtSpace((x,y+1)) == "bot":
                self.robot.turnRight()
                return
            elif self.robot.lookAtSpace((x-1,y)) == "bot":
                self.robot.turnLeft()
                return
        elif self.robot.rotation ==1:
            if self.robot.lookInFront() == "bot":
                self.robot.attack()
                return
            elif self.robot.lookAtSpace((x,y+1)) == "bot":
                self.robot.turnRight()
                return
            elif self.robot.lookAtSpace((x-1,y)) == "bot":
                self.robot.turnRight()
                return
            elif self.robot.lookAtSpace((x,y-1)) == "bot":
                self.robot.turnLeft()
                return
        elif self.robot.rotation ==2:
            if self.robot.lookInFront() == "bot":
                self.robot.attack()
                return
            elif self.robot.lookAtSpace((x+1,y)) == "bot":
                self.robot.turnLeft()
                return
            elif self.robot.lookAtSpace((x,y-1)) == "bot":
                self.robot.turnRight()
                return
            elif self.robot.lookAtSpace((x-1,y)) == "bot":
                self.robot.turnRight()
                return
        elif self.robot.rotation ==3:
            if self.robot.lookInFront() == "bot":
                self.robot.attack()
                return
            elif self.robot.lookAtSpace((x,y-1)) == "bot":
                self.robot.turnRight()
                return
            elif self.robot.lookAtSpace((x+1,y)) == "bot":
                self.robot.turnRight()
                return
            elif self.robot.lookAtSpace((x,y+1)) == "bot":
                self.robot.turnLeft()
                return
        
        p=(5,5)
        (g,h)=p
        
        exit_flag=False
        for a in range(0,11):
            for f in range(x-a,x+a+1,1):
                ooo= self.robot.lookAtSpace((f,y+a))
                if ooo =="HP" or "ATK"==ooo:
                    exit_flag=True
                    g=f
                    h=y+a
                    break
            
                ooo= self.robot.lookAtSpace((f,y-a))
                if ooo =="HP" or "ATK"==ooo:
                    exit_flag=True
                    g=f
                    h=y-a
                    break
            
            if exit_flag:
                break
            
            for d in range(y-a,y+a+1,1): 
                ooo= self.robot.lookAtSpace((x-a,d))
                if ooo =="HP" or "ATK"==ooo:
                    exit_flag=True
                    g=x-a
                    h=d
                    break
            
                
            
                ooo= self.robot.lookAtSpace((x+a,d))
                if ooo =="HP" or "ATK"==ooo:
                    exit_flag=True
                    g=x+a
                    h=d
                    break
            if exit_flag:
                break
            
            
        a=g-x
        b=h-y
        print(x,y)
        
        if self.currentlyDoing == "random":
            self.robot.goForth()
            self.currentlyDoing=""
            return
        if self.robot.rotation ==0:
            if b<0:
                if self.robot.lookInFront() == "wall":
                    random.choice([self.robot.turnLeft,self.robot.turnRight])()
                    self.currentlyDoing = "random"
                    return
            if b==0:
                if a>0:
                    self.robot.turnRight()
                    return
                if a<0:
                    self.robot.turnLeft()
                    return
            if a==0:
                if b<0:
                    self.robot.goForth()
                    return
                if b>0:
                    self.robot.turnRight()
                    return
            if b<0:
                self.robot.goForth()
                return
            if b>0:
                random.choice([self.robot.turnLeft,self.robot.turnRight])()
                return

        elif self.robot.rotation ==1: 
            if a>0:
                if self.robot.lookInFront() == "wall":
                    random.choice([self.robot.turnLeft,self.robot.turnRight])()
                    self.currentlyDoing = "random"
                    return
            if b==0:
                if a>0:
                    self.robot.goForth()
                    return
                if a<0:
                    self.robot.turnRight()
                    return
            if a==0:
                if b<0:
                    self.robot.turnLeft()
                    return
                if b>0:
                    self.robot.turnRight()
                    return
            if a>0:
                self.robot.goForth()
                return
            if a<0:
                random.choice([self.robot.turnLeft,self.robot.turnRight])()
                return
        
        elif self.robot.rotation ==2:    
            if b>0:
                if self.robot.lookInFront() == "wall":
                    random.choice([self.robot.turnLeft,self.robot.turnRight])()
                    self.currentlyDoing = "random"
                    return
            if b==0:
                if a>0:
                    self.robot.turnLeft()
                    return
                if a<0:
                    self.robot.turnRight()
                    return
            if a==0:
                if b<0:
                    self.robot.turnRight()
                    return
                if b>0:
                    self.robot.goForth()
                    return
            if b<0:
                random.choice([self.robot.turnLeft,self.robot.turnRight])()
                return
            if b>0:
                self.robot.goForth()
                return
        
        elif self.robot.rotation ==3:
            if a<0:
                if self.robot.lookInFront() == "wall":
                    random.choice([self.robot.turnLeft,self.robot.turnRight])()
                    self.currentlyDoing = "random"
                    return
            if b==0:
                if a>0:
                    self.robot.turnRight()
                    return
                if a<0:
                    self.robot.goForth()
                    return
            if a==0:
                if b<0:
                    self.robot.turnRight()
                    return
                if b>0:
                    self.robot.turnLeft()
                    return
            if a>0:
                random.choice([self.robot.turnLeft,self.robot.turnRight])()
                return
            if a<0:
                self.robot.goForth()
                return
        self.robot.doNothing()
        
        
        
        
        
                
                
                
                
                
                
            