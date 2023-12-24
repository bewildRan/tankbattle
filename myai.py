"""
AI Name: Null AI

Made by: Carter

Strategy:
Do nothing.
"""


class AI:
    def turn(self):
        
        if self.robot.lookInFront() is "wall":
            self.robot.turnLeft()
        elif self.robot.lookInFront() is "bot":
            self.robot.attack()
        else:
            self.robot.goForth()
            