m=0
j=150
import random
class AI:
    
    def __init__(self):
        #Anything the AI needs to do before the game starts goes here.
        pass
    def turn(self):
        global m
        global j
        x,y=self.robot.position
        mydir=self.robot.rotation
        if  m==0 :
            if self.robot.lookInFront()=="bot":
                self.robot.attack()
            
            elif self.robot.lookAtSpace((x,y-1))=="HP" or self.robot.lookAtSpace((x,y-1))=="ATK" or self.robot.lookAtSpace((x,y-1))=="bot":
                if mydir==0:
                    self.robot.goForth()
                elif mydir==3:
                    self.robot.turnRight()
                elif mydir==2:
                    self.robot.turnLeft()
                else:
                    self.robot.turnLeft()
            elif self.robot.lookAtSpace((x+1,y))=="HP" or self.robot.lookAtSpace((x+1,y))=="ATK" or self.robot.lookAtSpace((x+1,y))=="bot":
                if mydir==0:
                    self.robot.turnRight()
                elif mydir==3:
                    self.robot.turnRight()
                elif mydir==2:
                    self.robot.turnLeft()
                else:
                    self.robot.goForth()
            elif self.robot.lookAtSpace((x,y+1))=="HP" or self.robot.lookAtSpace((x,y+1))=="ATK" or self.robot.lookAtSpace((x,y+1))=="bot":
                if mydir==0:
                    self.robot.turnRight()
                elif mydir==3:
                    self.robot.turnRight()
                elif mydir==2:
                    self.robot.goForth()
                else:
                    self.robot.turnRight()
            elif self.robot.lookAtSpace((x-1,y))=="HP" or self.robot.lookAtSpace((x-1,y))=="ATK" or self.robot.lookAtSpace((x-1,y))=="bot":
                if mydir==0:
                    self.robot.turnLeft()
                elif mydir==3:
                    self.robot.goForth()
                elif mydir==2:
                    self.robot.turnRight()
                else:
                    self.robot.turnRight()
            elif self.robot.lookInFront()=="wall" :
                n=random.randint(1,100)
                if n<=15 :
                    self.robot.turnLeft()
                else :
                    self.robot.turnRight()
            else:
                p=random.randint(1,j)
                j=j-10
                if j<=100:
                    j=100
                if p<=90:    
                    self.robot.goForth()
                elif p<=95:
                    self.robot.turnLeft()
                else:
                    self.robot.turnRight()
        