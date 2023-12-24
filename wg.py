"""
AI Name: Circle AI

Made by: Carter

Strategy: Drive in circles.  Attack any robot in your path.
"""
import random


class AI:
    def __init__(self):
        #Anything the AI needs to do before the game starts goes here.
        pass
        self.currentlyDoing = "forward"
        self.UpDir=0
        self.RightDir=1
        self.DownDir=2
        self.LeftDir=3

        self.PathList=[]   #Record the available paths
        self.shortestPathLen=20
        self.findPath=0

    #定义goTowards函数
    def goTowards(self,targetLocation):
        myLocation = self.robot.position

        #Select the next right node first
        self.findPath=0
        self.shortestPathLen=20
        iPath = []    #reset the list
        self.PathList.clear()  #reset the list
        iPath.append(myLocation)
        self.PathList.append(iPath)

        # iPath = []    #reset the list
        # self.PathList.clear()  #reset the list
        # iPath.append((7,8))
        # self.PathList.append(iPath)
        # self.calPath2((7,8),(5,5),iPath)

        self.calPath2(myLocation, targetLocation, iPath)

        pathExist=0
        for accessPath in self.PathList:
            if (targetLocation in accessPath):
                pathExist=1
                #print("The target is at: ", targetLocation)
                #print("The path length is ", len(accessPath))
                #print("The path to target is:", accessPath)
                nextNode=accessPath[1]   #second item is the right next node.

        if(not pathExist):
            print("in goTowards(), there is no possible path to the target")
            print("from source:",myLocation,"to target:",targetLocation)
            print("please verify it")
            return

        delta = (nextNode[0]-myLocation[0],nextNode[1]-myLocation[1])
        if (abs(delta[0]) == 0 and abs(delta[1] == 0)):  # robot is at the position of target, stay at this position
            self.robot.doNothing()
            print("in goTowards(), there may be some error, the robot is at the position of target?")

        if abs(delta[0]) > abs(delta[1]):
            if delta[0] < 0:
                targetOrientation = self.LeftDir  # face left
            else:
                targetOrientation = self.RightDir  # face right
        else:
            if delta[1] < 0:
                targetOrientation = self.UpDir  # face up
            else:
                targetOrientation = self.DownDir  # face down

        if self.robot.rotation == targetOrientation:
            self.robot.goForth()
            self.currentlyDoing = "forward"

        else:
            leftTurnsNeeded = (self.robot.rotation - targetOrientation) % 4
            if leftTurnsNeeded <= 2:
                self.robot.turnLeft()
                self.currentlyDoing = "turnLeft"
            else:
                self.robot.turnRight()
                self.currentlyDoing = "turnRight"


    #Judge whether exist interested target that I am closer with it than the enemy.
    #If so, return the position of interested target, if not, return null target.
    def isThereInterestedTarget(self,targetArray,me,enemy):
        for i in targetArray:
          if (abs(me[0] - i[0]) + abs(me[1] - i[1])) <= (abs(enemy[0] - i[0]) + abs(enemy[1] - i[1])):
            return i[0],i[1]  #Return the posistion of interested target
        return 0

    def calPath2(self,sourceLocation,targetLocation,iPath):  #calculate the possible viable path from sourceLocation to the targetLocation
        UpPos = (sourceLocation[0], sourceLocation[1] - 1)
        DownPos = (sourceLocation[0], sourceLocation[1] + 1)
        LeftPos =(sourceLocation[0] - 1, sourceLocation[1])
        RightPos = (sourceLocation[0] + 1, sourceLocation[1])

        viableNodes=[UpPos,LeftPos,DownPos,RightPos]
        for iNode in viableNodes:
            if(self.robot.lookAtSpace(iNode)!="wall"):
                nodePassed=0
                for existPath in self.PathList:
                    if iNode in existPath:   #Only consider the disjoint path
                        nodePassed=1
                        break

                if(not nodePassed):
                    tempPath=[]
                    tempPath=iPath.copy()
                    tempPath.append(iNode)
                    self.PathList.append(tempPath)    #Add all new branches from iPath

        #Delete the main path after adding all of its new branches or it is souranded by three sides wall
        if(iPath in self.PathList):
            self.PathList.remove(iPath)

        #Judege whether exist path reaches the target or not
        for existPath in self.PathList:
            lastNode = existPath[len(existPath) - 1]
            if (abs(lastNode[0] - targetLocation[0]) + abs(lastNode[1] - targetLocation[1]) == 0):
                print("In calPath2(), reach the target at path")
                print("From source", sourceLocation, "to ", targetLocation)
                print("Current shortest path length is", self.shortestPathLen)
                print("The path is ", existPath)
                self.shortestPathLen = len(existPath)
                self.findPath=1
                return

        for existPath in self.PathList:
            if((len(existPath)<self.shortestPathLen) and (self.findPath==0)):
                lastNode = existPath[len(existPath) - 1]
                self.calPath2(lastNode, targetLocation, existPath)


    def turn(self):
        
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
            return

        else:
            #获取战场信息
            objHPs = []
            objSPDs = []
            objATKs = []
            objWalls = []
            for i in range(1,11):
                for j in range(1,11):
                    obj = self.robot.lookAtSpace((i,j))
                    #将获取的信息存入各个对应之中
                    if obj == "HP":
                       objHPs.append((i,j)) 
                    if obj == "SPD":
                       objSPDs.append((i,j))
                    if obj == "ATK":
                       objATKs.append((i,j))
                    if obj == "wall":
                       objWalls.append((i,j))
                    if obj == "me":
                        me = (i,j)
                    if obj == "bot":
                        enemy=(i,j)

            #Judge whether exist the interested target or not"
            target = self.isThereInterestedTarget(objHPs, me, enemy)
            if target:
                print("There is HP at position x=",target[0],"   y=",target[1])
                self.goTowards(target)   #get the interested target

            else:
                target = self.isThereInterestedTarget(objATKs, me, enemy)
                if target:
                    print("There is ATK at position x=", target[0], "   y=", target[1])
                    self.goTowards(target)
                else:
                    target = self.isThereInterestedTarget(objSPDs, me, enemy)

                    if target:
                        print("There is SPD at position x=", target[0], "   y=", target[1])
                        self.goTowards(target)

                    else:   #If can't get the interested target easily, then try to go towards goldGrid
                        goldGrid=(5,5)
                        if(self.robot.lookAtSpace(goldGrid)!="wall"):
                        # print("There is no interested target, the robot will goto the Golden grid")
                        # print("Before moving,robot is at ", self.robot.position[0], ",", self.robot.position[1])
                        # print("robot direction is", self.robot.rotation)
                            self.goTowards(goldGrid)   #if can't get the interested target, then goto the important grid
                        # print("After moving,robot is at ", self.robot.position[0], ",", self.robot.position[1])
                        # print("robot direction is", self.robot.rotation)
                        else:
                            random.choice(
                                [self.robot.turnLeft, self.robot.turnRight, self.robot.goForth, self.robot.goForth2])()
                        return



