import random
class AI:
#定义函数，自己坦克目前做的模式
    def __init__(self):
        self.currentlyDoing=""
        pass
#定义函数，x指自己方向朝上，y指自己方向朝右
    def turn(self):
        x=self.robot.position[0]
        y=self.robot.position[1]
        
#根据自己坦克的朝向以及返回的对手坦克的位置（在自己位置分为上下左右的基础上，如果对手在自己正前方1格攻击）试图绕到对方坦克正后面攻击
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
#得到敌人的位置和方向        
        (p,r) = self.robot.locateEnemy()
        (g,h)=p
#移动到加血包或者是加攻击上        
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
#以random为基础，撞墙就拐        
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
        
        
        
        
        
                
                
                
                
                
                
            