import random
class AI:
    def __init__(self):
        self.isFirstTurn = True
    def turn(self):
        global p,r,HP,ATK,SPD
        if(self.robot.detectEnemy()!=None):
            p,r,HP,ATK,SPD = self.robot.detectEnemy()
        mydir = self.robot.rotation
        x,y=self.robot.position
       
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
        elif self.robot.lookInFront() == "wall":
            
            random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goBack])()
        elif self.robot.lookInFront() == "clear":
            if self.robot.detectEnemy():
                self.robot.goForth()
            else:
                random.choice([self.robot.goForth,self.robot.turnLeft])()
        elif self.robot.detectEnemy()!=None:
            
            if self.robot.detectEnemy()[2]/self.robot.ATK>self.robot.health/self.robot.detectEnemy()[3]:
                if(p[0]>x and p[1]>y and mydir!=1):
                    self.robot.turnRight()
                elif(p[0]>x and p[1]>y and mydir==1):
                    self.robot.goForth()
                elif(p[0]<=x and p[1]>y and mydir!=0):
                    self.robot.turnRight()
                elif(p[0]<=x and p[1]>y and mydir==0):
                    self.robot.goForth()
                elif(p[0]>x and p[1]<y and mydir!=1):
                    self.robot.turnRight()
                elif(p[0]>x and p[1]<y and mydir==1):
                    self.robot.goForth()
                elif(p[0]<=x and p[1]<y and mydir!=2):
                    self.robot.turnRight()
                elif(p[0]<=x and p[1]<y and mydir==2):
                    self.robot.goForth()
                elif(p[0]<x and p[1]==y and mydir!=3):
                    self.robot.turnLeft()
                elif(p[0]<x and p[1]==y and mydir==3):
                    self.robot.goForth()
                elif(p[0]>x and p[1]==y and mydir!=1):
                    self.robot.turnLeft()
                elif(p[0]>x and p[1]==y and mydir==1):
                    self.robot.goForth()
                else:
                    self.robot.goForth
            else:
                self.robot.goForth()
        else:
            self.robot.goForth()
                
            

               

                
                     
                
