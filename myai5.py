# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 11:01:41 2018

@author: g1921231
"""
"""
AI Name: Null AI

Made by: Carter

Strategy:
Move around randomly.
Attack any robot in front of you.
"""

import random

class AI:

    def _init_(self):
        pass
    def turn(self):
        
        if self.robot.lookInFront() is "bot":
            self.robot.attack()
            return
        
        elif self.robot.lookInFront() is "HP" or self.robot.lookInFront() is "ATK" or self.robot.lookInFront() is "SPD":
            self.robot.goForth()
            return
        
        else:
            random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goBack])()
