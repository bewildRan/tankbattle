# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:07:38 2018

@author: xiaoran
"""

"""
AI Name:bdzy

Made by: Carter


"""
import random


class AI:
    
    def __init__(self):
        pass# self.isFirstTurn = True
   # def hp(self):
    #    self.robot.hp=True
     #   if self.robot.lookInFront() == "HP"or"ATK"or"SPD":
      #      self.robot.goForth()
            
            
    def turn(self):
         if self.robot.lookInFront() == "bot":
            self.robot.attack()
            return
      #   elif self.robot.hp:
       #     random.choice([self.robot.turnRight, self.robot.turnLeft])()
        #    self.robot.hp = False
        # elif self.isFirstTurn:
         #   self.robot.turnRight()
          #  self.isFirstTurn = False
         
         elif self.robot.lookInFront() == "wall":
             random.choice([self.robot.turnRight, self.robot.turnLeft])()
             return
                
         elif self.robot.lookInFront() == "HP" or  self.robot.lookInFront() == "ATK" or self.robot.lookInFront() == "SPD":
             self.robot.goForth()
             return
     
               # if self.robot.health()>100 or self.robot.ATK()>10 or self.robot.speedUP>1:
                #    random.choice([self.robot.turnRight, self.robot.turnLeft,self.robot.goBack])()
                 #   return
            
            
            
         while self.robot.lookInFront() == "clear":
                #if self.robot.health>=100:
                 #   self.robot.goForth()
                self.robot.goForth()