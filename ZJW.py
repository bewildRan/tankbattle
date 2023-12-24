import random
class AI:
    def __init__(self):
        self.isFirstTurn = True
    def turn(self):
#        while True:
#            self.robot.lookInFront()
        if self.isFirstTurn:
            self.robot.turnRight()
            self.isFirstTurn = False
        elif self.robot.lookInFront() == "bot":
            self.robot.attack()
            #x,y=self.robot.position
        #if x==1 and y==5:
            #self.robot.turnLeft()
        #if self.isFirstTurn:
            #self.robot.turnRight()#前手右转
            #self.isFirstTurn = False
            #H=self.robot.health
            #A=self.robot.ATK
            #detectEnemy()
            #(p,r,HP,ATK,SPD)=self.robot.detectEnemy()
            #if HP/A<H/ATK:
                #self.robot.attack()
            #else:
                #self.robot.turnLeft()
                #self.robot.goForth()
        elif self.robot.lookInFront()== "wall":
            self.robot.turnRight()
            #random.choice([self.robot.turnLeft,self.robot.turnRight])()
        else:
            random.choice([self.robot.turnLeft,self.robot.goForth,self.robot.goForth])()
            #self.robot.goForth()