# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 11:38:45 2017

@author: ran
"""

"""
AI Name: Random AI

Made by: Carter

Strategy:
Move around randomly.
Attack any robot in front of you.
"""

import random

class AI:
    def __init__(self):
        #Anything the AI needs to do before the game starts goes here.
        pass
    def turn(self):
        self.robot.goForth()
#        if self.robot.lookInFront() == "bot":
#            self.robot.attack()
#            return
#        else:
#            random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goForth2])()
