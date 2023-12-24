import math
import random
class AI:
    def __init__(self):
        self.isBoosted = True
        self.stepNum = 1

    def drawgraph(self):
        allstring = ["me", "bot", "wall", "clear", "HP", "ATK", "SPD"]
        allprintstring = ["me   ", "bot  ", "wall ", "clear", "HP   ", "ATK  ", "SPD  "]
        myList = [( [None] * 10) for i in range(10)]
        for i in range(1, 11):
            for k in range(1, 11):
                for num in range(0, 7):
                    now = self.robot.lookAtSpace((i, k))
                    if now == allstring[num]:
                        myList[i - 1][k - 1] = allstring[num]
                        #myList[i - 1][k - 1] = allprintstring[num]
        return myList

    def printgraph(self,aList):
        for i in range(0, 10):
            print(aList[0][i],
                  aList[1][i],
                  aList[2][i],
                  aList[3][i],
                  aList[4][i],
                  aList[5][i],
                  aList[6][i],
                  aList[7][i],
                  aList[8][i],
                  aList[9][i])
        return

    def the_nearist(self,item):

        myCurrentPosition = self.robot.position
        self.stepNum = 1
        while self.isBoosted is False:
            print("write the most important thing here")

    def turn(self):
        if self.isBoosted is True:
            self.robot.goForth()
            self.isBoosted = False
        myAtk = self.robot.ATK
        currenthp = self.robot.health
        currentList=AI.drawgraph(self)
        myPosition = self.robot.position
        myRotation = self.robot.rotation
        AI.printgraph(self,currentList)
        if (myPosition[0] is not 1) and (myPosition[0] is not 10) and (myPosition[1] is not 1) and (myPosition[1] is not 10):
            if myRotation is 0:
                if currentList[myPosition[0]-1][myPosition[1]-2] is "HP" or currentList[myPosition[0]-1][myPosition[1]-1] is "ATK" or currentList[myPosition[0]-1][myPosition[1]-1] is "SPD":

                    self.robot.goForth()

                if currentList[myPosition[0] - 1][myPosition[1]] is "HP" or currentList[myPosition[0] - 1][
                    myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":

                    self.robot.goBack()

                if currentList[myPosition[0] - 2][myPosition[1] - 1] is "HP" or currentList[myPosition[0] - 1][
                    myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD" :

                    self.robot.turnLeft()

                if currentList[myPosition[0] ][myPosition[1] - 1] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":

                    self.robot.turnRight()
            if myRotation is 1:
                if currentList[myPosition[0] - 1][myPosition[1] - 2] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":
                    self.robot.turnRight()

                if currentList[myPosition[0] - 1][myPosition[1]] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":
                    self.robot.turnLeft()

                if currentList[myPosition[0] - 2][myPosition[1] - 1] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":
                    self.robot.goBack()

                if currentList[myPosition[0]][myPosition[1] - 1] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":
                    self.robot.goForth()
            if myRotation is 2:
                if currentList[myPosition[0] - 1][myPosition[1] - 2] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":
                    self.robot.goForth()

                if currentList[myPosition[0] - 1][myPosition[1]] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":
                    self.robot.goBack()

                if currentList[myPosition[0] - 2][myPosition[1] - 1] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":
                    self.robot.turnLeft()

                if currentList[myPosition[0]][myPosition[1] - 1] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":
                    self.robot.turnRight()
            if myRotation is 3:
                if currentList[myPosition[0] - 1][myPosition[1] - 2] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":
                    self.robot.turnLeft()

                if currentList[myPosition[0] - 1][myPosition[1]] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":
                    self.robot.turnRight()

                if currentList[myPosition[0] - 2][myPosition[1] - 1] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":
                    self.robot.goForth()

                if currentList[myPosition[0]][myPosition[1] - 1] is "HP" or currentList[myPosition[0] - 1][
                            myPosition[1] - 1] is "ATK" or currentList[myPosition[0] - 1][myPosition[1] - 1] is "SPD":
                    self.robot.goBack()
            if self.robot.lookInFront() == "wall":
                random.choice([self.robot.turnLeft, self.robot.turnRight, self.robot.goBack2,self.robot.goBack])()
            if self.robot.lookInFront() == "bot":
                (p, r, HP, ATK, SPD) = self.robot.detectEnemy()
                if math.ceil(HP/myAtk) >math.ceil(currenthp/ATK):
                    random.choice([self.robot.turnLeft, self.robot.turnRight, self.robot.goBack2, self.robot.goBack])()
                if math.ceil(HP / myAtk) <= math.ceil(currenthp / ATK):
                    self.robot.attack()
            else:
                random.choice(
                    [self.robot.turnLeft, self.robot.turnRight, self.robot.goBack2, self.robot.goBack, self.robot.goForth,
                     self.robot.goForth2])()
        else:
            random.choice([self.robot.turnLeft, self.robot.turnRight, self.robot.goBack2, self.robot.goBack,self.robot.goForth,self.robot.goForth2])()
