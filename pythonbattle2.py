# pythonbattle.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# This is the PythonBattle program that runs the AI's against each other.
# It generates the play grid using Pygame and runs the battle.

# v0.1(12.25noon)

import pygame #ASCII/PYGAME
import time
import random
pygame.init() #ASCII/PYGAME

class OutOfTurnError(Exception):
    """ A custom exception describing a state in which a robot moves out of turn"""
    def __init__(self,botname):
        self.botname = botname
    def __str__(self):
        return "Robot "+self.botname+" tried to call function when it wasn't his turn"

class RobotIsDefeatedError(Exception):
    """ A custom exception describing a state in which a robot moves while it
is defeated."""
    def __init__(self,botname):
        self.botname = botname
    def __str__(self):
        return "Robot "+self.botname+" tried to call function while defeated"

class Block: # 障碍
    def __init__(self,position):
        self.position = position

class addATK: # 加攻击力
    def __init__(self,position,dATK):
        self.position = position
        self.dATK = dATK

class addHP: # 加血
    def __init__(self,position,dHP):
        self.position = position
        self.dHP = dHP

class addSPD: # 加速器
    def __init__(self,position):
        self.position = position
        
class Robot:
    """A player in the battle. 
    Rotation values:
    0: Up
    1: Right
    2: Down
    3: Left

    Note: All methods starting with _ are PRIVATE. Do not
    call them under any circumstances.  """
    def __init__(self,name,ai,position,rotation):
        self.name = name
        self.ai = ai
        ai.robot = self
        
        self.position = position
        self.rotation = rotation
        self.health = 100
        self.ATK = 10 #默认攻击力 = 10
        self.speedUP = 0 #加速之后可以每回合走2格
        
    def _spaceInFront(self): # 返回self眼前的position位置
        if self.rotation == 0:
            return (self.position[0],self.position[1]-1)
        elif self.rotation == 1:
            return (self.position[0]+1,self.position[1])
        elif self.rotation == 2:
            return (self.position[0],self.position[1]+1)
        elif self.rotation == 3:
            return (self.position[0]-1,self.position[1])
    
    def _getSpace(self,space): # 看看space位置是什么，返回"me"/"bot"/"wall"/"clear"/"HP"/"ATK"/"SPD"
        global field, BLKs, addHPs, addATKs, addSPDs
        if space == self.position:
            return "me"
        else:
            for i in field:
                if i.position == space:
                    return "bot" #对方
            for i in BLKs:
                if i.position == space:
                    return "wall" # 障碍 or 边界
            for i in addHPs:
                if i.position == space:
                    return "HP" # 加血包
            for i in addATKs:
                if i.position == space:
                    return "ATK" # 加攻击力
            for i in addSPDs:
                if i.position == space:
                    return "SPD"  #加速器
        if space[0]<1:
            return "wall"
        elif space[1]<1:
            return "wall"
        elif space[0]>10:
            return "wall"
        elif space[1]>10:
            return "wall"
        else:
            return "clear"
    
    def _goForth(self):  # 往眼前位置走一格，成功返回"success"/否则返回"wall"/"bot"
        objFront = self._getSpace(self._spaceInFront())
        if objFront == "wall" or objFront == "bot":
            return objFront
        else:
            self.position = self._spaceInFront()
            return "success"

        
    def _goForth2(self):  # 往眼前位置走2格，成功返回“success”/否则返回“wall”/"bot"
        if self.speedUP == 0:
#            self.health -= 1000
            return "wall"
        objFront = self._getSpace(self._spaceInFront())
        if objFront == "wall" or objFront == "bot":
            return objFront
        if self.rotation == 0:
            p2 = (self.position[0],self.position[1]-2)
        elif self.rotation == 1:
            p2 = (self.position[0]+2,self.position[1])
        elif self.rotation == 2:
            p2 = (self.position[0],self.position[1]+2)
        elif self.rotation == 3:
            p2 = (self.position[0]-2,self.position[1])
        
        objFront = self._getSpace(p2)
        if  objFront == "wall" or objFront == "bot":
            return objFront
        else:
            self.position = p2
            return "success"
        
    
    def _goBack(self): # 倒车走一格，方向不变
        if self.rotation == 0:
            p2 = (self.position[0],self.position[1]+1)
        elif self.rotation == 1:
            p2 = (self.position[0]-1,self.position[1])
        elif self.rotation == 2:
            p2 = (self.position[0],self.position[1]-1)
        elif self.rotation == 3:
            p2 = (self.position[0]+1,self.position[1])
        
        objFront = self._getSpace(p2)
        if  objFront == "wall" or objFront == "bot":
            return self._getSpace(p2)
        else:
            self.position = p2
            return "success"

        
    def _goBack2(self):  # 往眼前位置走2格，成功返回“success”/否则返回“wall”/"bot"
        if self.speedUP == 0:
#            self.health -= 1000
            return "wall"
        
        if self.rotation == 0:
            p2 = (self.position[0],self.position[1]+1)
        elif self.rotation == 1:
            p2 = (self.position[0]-1,self.position[1])
        elif self.rotation == 2:
            p2 = (self.position[0],self.position[1]-1)
        elif self.rotation == 3:
            p2 = (self.position[0]+1,self.position[1])
        
        objFront = self._getSpace(p2)
        if  objFront == "wall" or objFront == "bot":
            return self._getSpace(p2) 
        
        if self.rotation == 0:
            p2 = (self.position[0],self.position[1]+2)
        elif self.rotation == 1:
            p2 = (self.position[0]-2,self.position[1])
        elif self.rotation == 2:
            p2 = (self.position[0],self.position[1]-2)
        elif self.rotation == 3:
            p2 = (self.position[0]+2,self.position[1])
        
        objFront = self._getSpace(p2)
        if  objFront == "wall" or objFront == "bot":
            return self._getSpace(p2)
        else:
            self.position = p2
            return "success"
    
        
    def _turnLeft(self):
        self.rotation -= 1
        self.rotation %= 4
        return "success"
    def _turnRight(self):
        self.rotation += 1
        self.rotation %= 4
        return "success"
    def _attack(self):
        global field
        for i in field:
            if i.position == self._spaceInFront():
                i.takeDamage(self.ATK)
                return "success"
        return self._getSpace(self._spaceInFront())
    def _beforeMove(self):
        """Check if the robot is moving out of turn or while defeated."""
        global state
        if (state != self.name) and (state != "win"):
            raise OutOfTurnError(self.name)
        elif state == "win":
            raise RobotIsDefeatedError(self.name)
    def _afterMove(self):
        """When a robot has moved, changes the state of the game so it's the
other robot's turn."""
        global field, state
        if state == self.name:
            for i in field:
                if i.name != self.name:
                    state = i.name
    
    def calculateCoordinates(self,distance=1,direction=None,position=None):
        """Convenience function for calculating positions.
        Returns the coordinates of the position described."""
        if direction == None:
            directionToCheck = self.rotation
        else:
            directionToCheck = direction
        if position == None:
            locationToReturn = self.position
        else:
            locationToReturn = position
        directionToCheck %= 4
        for i in range(distance):
            if directionToCheck == 0:
                locationToReturn= (locationToReturn[0],locationToReturn[1]-1)
            elif directionToCheck == 1:
                locationToReturn= (locationToReturn[0]+1,locationToReturn[1])
            elif directionToCheck == 2:
                locationToReturn= (locationToReturn[0],locationToReturn[1]+1)
            elif directionToCheck == 3:
                locationToReturn= (locationToReturn[0]-1,locationToReturn[1])
        return locationToReturn
    def lookInFront(self):
        "Looks at the space in front of the robot"
        return self.lookAtSpace(self.calculateCoordinates())
    def lookAtSpace(self,space):# 返回string，接受(x,y)
        "Checks a space"
        return self._getSpace(space)
    def takeDamage(self,damage):
        "Don't call. Makes this robot take damage."
        global state, field
        self.health -= damage
        if self.health < 0:
            self.health = 0
        if self.health <= 0:
            state = "win"
    def attack(self):
        "Attacks"
        self._beforeMove()
        result = self._attack()
        self._afterMove()
        return result
    def goBack(self):
        "Moves backwards"
        self._beforeMove()
        result = self._goBack()
        self._afterMove()
        return result
    def goForth(self):
        "Moves forwards"
        self._beforeMove()
        result = self._goForth()
        self._afterMove()
        return result
    
    ##2
    def goBack2(self):
        "Moves backwards"
        self._beforeMove()
        result = self._goBack2()
        self._afterMove()
        return result
    def goForth2(self):
        "Moves forwards"
        self._beforeMove()
        result = self._goForth2()
        self._afterMove()
        return result
    
    def upd(self):
        global addHPs, addATKs, addSPDs
        p1 = self.position
        for i in addHPs:
            if i.position == p1:
                self.health += i.dHP
                addHPs.remove(i)
                return "success"
        for i in addATKs:
            if i.position == p1:
                self.ATK += i.dATK
                addATKs.remove(i)
                return "success"
        for i in addSPDs: 
            if i.position == p1:
                self.speedUP = 1
                addSPDs.remove(i)
                return "success"
        return "success"
    
    def turnLeft(self):
        "turns left"
        self._beforeMove()
        result = self._turnLeft()
        self._afterMove()
        return result
    def doNothing(self):
        "Does nothing, ending the turn"
        self._beforeMove()
        result = "success"
        self._afterMove()
        return result
    def turnRight(self):
        "Turns right"
        self._beforeMove()
        result = self._turnRight()
        self._afterMove()
        return result
    def locateEnemy(self):
        "Returns the coordinates of an enemy"
        global field
        for i in field:
            if i.name != self.name:
                return i.position, i.rotation
    def detectEnemy(self):
        "Returns the HP and ATK of an enemy around"
        global field
        for i in field:
            if i.name != self.name:
                if abs(i.position[0]-self.position[0]) + abs(i.position[1]-self.position[1]) == 1:
                    return i.position, i.rotation, i.health, i.ATK, i.speedUP

def chk(p1):
    global field, BLKs, addHPs, addATKs, addSPDs
    for i in field:
        if i.position == p1:
            return 1
    for i in BLKs:
        if i.position == p1:
            return 1
    for i in addHPs:
        if i.position == p1:
            return 1
    for i in addATKs:
        if i.position == p1:
            return 1
    for i in addSPDs:
        if i.position == p1:
            return 1
    return 0

def calSqs(redsquares, bluesquares):
    global xgold, ygold
    lred = len(redsquares)
    lblue = len(bluesquares)
    if (xgold,ygold) in redsquares:
        lred += 15
    elif (xgold,ygold) in bluesquares:
        lblue += 15
    return lred,lblue

def drawBattlefieldPygame(bot1, bot2):
    """draws the battlefield with Pygame"""
    global state, redsquares, bluesquares, bot1img, bot2img, addHPimg, addSPDimg, addATKimg
    global namefont, ai1name, ai2name, BLKs, addHPs, addATKs, addSPDs
    global xgold, ygold
    #Get the display surface
    screen = pygame.display.get_surface()
    
    
    #If the Pygame window isn't open, open it.
    if screen == None:
        screen = pygame.display.set_mode((640,600))
    #Clear the screen
    screen.fill((0,0,0))
    # 画红/蓝块、障碍、加血包/加速器/攻击力
    
    
    
    for i in redsquares:
        pygame.draw.rect(screen,(64,0,0),((  (i[0]-1)*48,(i[1]-1)*48  ),(48,48)))
    for i in bluesquares:
        pygame.draw.rect(screen,(0,0,64),(((i[0]-1)*48,(i[1]-1)*48),(48,48)))
    pygame.draw.rect(screen,(120,80,3),(((xgold-1)*48, (ygold-1)*48  ),(48,48)))
    for i in BLKs:
        pygame.draw.rect(screen,(150,150,150),(((i.position[0]-1)*48,(i.position[1]-1)*48),(48,48)))
    for i in addHPs:
        HPpos = ((i.position[0]-1)*48,(i.position[1]-1)*48)
        screen.blit(pygame.transform.rotate(addHPimg,0),HPpos)
    for i in addSPDs:
        SPDpos = ((i.position[0]-1)*48,(i.position[1]-1)*48)
        screen.blit(pygame.transform.rotate(addSPDimg,0),SPDpos)
    for i in addATKs:
        ATKpos = ((i.position[0]-1)*48,(i.position[1]-1)*48)
        screen.blit(pygame.transform.rotate(addATKimg,0),ATKpos)
        
        
    #Get the screen positions of the robots
    bot1pos = ((bot1.position[0]-1)*48,(bot1.position[1]-1)*48)
    bot2pos = ((bot2.position[0]-1)*48,(bot2.position[1]-1)*48)
    #Draw the robots on the screen
    screen.blit(pygame.transform.rotate(bot1img,-90*bot1.rotation),bot1pos)
    screen.blit(pygame.transform.rotate(bot2img,-90*bot2.rotation),bot2pos)
    
    # 金色格子
#    xgold = 5
#    ygold = 5
    
    #draw grid lines
    for i in range(1,10):
        pygame.draw.line(screen,(50,50,50),(0,i*48),(480,i*48),5)
        pygame.draw.line(screen,(50,50,50),(i*48,0),(i*48,480),5)

    (lred, lblue) = calSqs(redsquares, bluesquares)
    
    #Write the names of the robots on the screen
    screen.blit(namefont.render(ai1name+"/HP:"+str(bot1.health),True,(255,0,0),(0,0,0)),(480,0))
    screen.blit(namefont.render("/ATK:"+ str(bot1.ATK)+"/SPD:"+ str(bot1.speedUP),True,(255,0,0),(0,0,0)),(480,20))
    screen.blit(namefont.render("#redSqs"+ str(lred),True,(255,0,0),(0,0,0)),(480,40))
    pygame.draw.rect(screen,(0,255,0),((480,60),(int(bot1.health*160/500.0),10)))
    
    screen.blit(namefont.render(ai2name+"/HP:"+str(bot2.health),True,(0,0,255),(0,0,0)),(480,100))
    screen.blit(namefont.render("/ATK:"+ str(bot2.ATK)+"/SPD:"+ str(bot2.speedUP),True,(0,0,255),(0,0,0)),(480,120))
    screen.blit(namefont.render("#blueSqs"+ str(lblue),True,(0,0,255),(0,0,0)),(480,140))
    pygame.draw.rect(screen,(0,255,0),((480,160),(int(bot2.health*160/500.0),10)))
    
    pygame.display.flip()
    #If the game is over...
    if state == "win":
        running = True
        #wait for the user to close the window
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
    else:
        #Otherwise, add a delay between frames
        time.sleep(0.1)

#
xgold = 5
ygold = 5

#Create Font object
namefont = pygame.font.Font(None,25)
#Get names of competitors
ai1name = input("Enter red AI: ")
ai2name = input("Enter blue AI: ")
#Dynamically import the robots as modules
ai1 = __import__(ai1name) 
ai2 = __import__(ai2name)
#Create the two Robot objects with the two AI objects
field = [Robot("red",ai1.AI(),(10,5),3),Robot("blue",ai2.AI(),(1,5),1)]

BLKs = []
for i in range(10):
    BLKs.append(Block((random.randint(0,10),random.randint(0,10))))
redsquares = []
bluesquares = []
addHPs = []
addATKs = []
addSPDs = []

pc = (random.randint(1,10),random.randint(1,10))
while chk(pc):
    pc = (random.randint(1,10),random.randint(1,10))
addHPs = [addHP(pc,1)]

pc = (random.randint(1,10),random.randint(1,10))
while chk(pc):
    pc = (random.randint(1,10),random.randint(1,10))
addATKs = [addATK(pc,1)]

pc = (random.randint(1,10),random.randint(1,10))
while chk(pc):
    pc = (random.randint(1,10),random.randint(1,10))
addSPDs = [addSPD(pc)]

state = "red"

pygame.display.set_mode((640,480))
#Load graphics, draw initial battlefield
bot1img = pygame.image.load("DozerRed.png").convert_alpha()
bot2img = pygame.image.load("DozerBlue.png").convert_alpha()
addHPimg = pygame.image.load("addHP.gif").convert_alpha()
addATKimg = pygame.image.load("addATK.jpg").convert_alpha()
addSPDimg = pygame.image.load("addSPD.gif").convert_alpha()

drawBattlefieldPygame(field[0],field[1]) #ASCII/PYGAME


numberOfTurns = 0

while state != "win":
    #Add specials
    temp = random.uniform(0,1)
    if temp <= 0.02:
        pc = (random.randint(1,10), random.randint(1,10))
        while chk(pc):
            pc = (random.randint(1,10), random.randint(1,10))
        
        c = random.randint(1,100)
        #HP
        if c<=40:
            addHPs.append(addHP(pc,random.randint(0,50)))
        elif c<=80:
            addATKs.append(addATK(pc,random.randint(0,5)))
        else:
            addSPDs.append(addSPD(pc))
            
    
    #color squares
    if not (field[0].position[0],field[0].position[1]) in redsquares:
        redsquares.append((field[0].position[0],field[0].position[1]))
        while (field[0].position[0],field[0].position[1]) in bluesquares:
            bluesquares.remove((field[0].position[0],field[0].position[1]))
    if not (field[1].position[0],field[1].position[1]) in bluesquares:
        bluesquares.append((field[1].position[0],field[1].position[1]))
        while (field[1].position[0],field[1].position[1]) in redsquares:
            redsquares.remove((field[1].position[0],field[1].position[1]))
    
    drawBattlefieldPygame(field[0],field[1]) #ASCII/PYGAME
    for i in field:
        try: # Prevent PythonBattle from crashing when AI code fails
            print([numberOfTurns,i.name])
            i.ai.turn()
            i.upd()
        except(Exception):
            print(i.name,"failed with error:")
#            print(e)
    numberOfTurns += 1
    if numberOfTurns == 1000:
        #If the battle runs longer than ~1.6 min, pull the plug
        state = "stalemate"
        break
#Color squares one last time
if not (field[0].position[0],field[0].position[1]) in redsquares:
    redsquares.append((field[0].position[0],field[0].position[1]))
    while (field[0].position[0],field[0].position[1]) in bluesquares:
        bluesquares.remove((field[0].position[0],field[0].position[1]))
if not (field[1].position[0],field[1].position[1]) in bluesquares:
    bluesquares.append((field[1].position[0],field[1].position[1]))
    while (field[1].position[0],field[1].position[1]) in redsquares:
        redsquares.remove((field[1].position[0],field[1].position[1]))
if state == "stalemate":
    drawBattlefieldPygame(field[0],field[1])#ASCII/PYGAME
    print("Turn limit reached!")
    #If either robot has higher health, it wins
    if field[0].health > field[1].health:
        print("Red wins!")
    elif field[1].health > field[0].health:
        print("Blue wins!")
    else:
        #Otherwise, whoever has the most squares wins
        print("Stalemate detected!")
        print("Counting colored squares...")
        time.sleep(2) #Pause for dramatic effect...

        (lred, lblue) = calSqs(redsquares, bluesquares)
        if  lred> lblue:
            print("The winner is Red with",lred,"squares!")
            print("(Blue had",lblue,"squares)")
        elif lred < len(bluesquares):
            print("The winner is Blue with",lblue,"squares!")
            print("(Red had",lred,"squares)")
        else:
            print("Tie! Both opponents had",lblue,"squares.")
    state = "win"
else:
    #print who wins
    if field[0].health > field[1].health:
        print("Red wins with",field[0].health,"health!")
    if field[1].health > field[0].health:
        print("Blue wins with",field[1].health,"health!")
drawBattlefieldPygame(field[0],field[1])     #ASCII/PYGAME
pygame.quit() #ASCII/PYGAME
