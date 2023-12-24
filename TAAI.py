import math
import random
import traceback
import sys


class AI:
    def __init__(self):
        self.isBoosted = False
        self.mode = 1

    def drawgraph(self):
        allstring = ["me", "bot", "wall", "clear", "HP", "ATK", "SPD"]
        allprintstring = ["me   ", "bot  ", "wall ", "clear", "HP   ", "ATK  ", "SPD  "]
        myList = [([None] * 10) for i in range(10)]
        for i in range(1, 11):
            for k in range(1, 11):
                for num in range(0, 7):
                    now = self.robot.lookAtSpace((i, k))
                    if now == allstring[num]:
                        myList[i - 1][k - 1] = allstring[num]
                        # myList[i - 1][k - 1] = allprintstring[num]
        return myList

    def check(self, test_string, aList):
        # 0 for goForth; 1 for goBack; 2 for turnLeft; 3 for turnRight; 4 for goForth2; 5 for goBack2 currently we have no 4 and 5 for there are problems unsolved now
        length = len(test_string)
        [x,y] = self.robot.position

        testrotation = self.robot.rotation
        if length >0:
            for i in range(0, length):
                if test_string[i] is "0":

                    if testrotation is 0:
                        y -= 1
                    if testrotation is 1:
                        x += 1
                    if testrotation is 2:
                        y += 1
                    if testrotation is 3:
                        x -= 1
                if test_string[i] is "1":
                    if testrotation is 0:
                        y += 1
                    if testrotation is 1:
                        x -= 1
                    if testrotation is 2:
                        y -= 1
                    if testrotation is 3:
                        x += 1
                if test_string[i] is "2":
                    if testrotation is 0:
                        testrotation = 3
                    elif testrotation is 1:
                        testrotation = 0
                    elif testrotation is 2:
                        testrotation = 1
                    elif testrotation is 3:
                        testrotation = 2
                if test_string[i] is "3":
                    if testrotation is 0:
                        testrotation = 1
                    elif testrotation is 1:
                        testrotation = 2
                    elif testrotation is 2:
                        testrotation = 3
                    elif testrotation is 3:
                        testrotation = 1
                if x < 1 or x >10 or y < 1 or y > 10:
                    return False
                if aList[x-1][y-1] is "wall":
                    return False
            if aList[x-1][y-1] is "HP" or aList[x-1][y-1] is "ATK": #or aList[x-1][y-1] is "SPD":
                return True
            else:
                return False
        else:
            return False

    def thestring(self, num, nowString, aList):
        if num == 0:
            #print(nowString)
            if AI.check(self, nowString,aList) is True:
                return nowString
            else:
                return " "
        if num > 0:
            for i in range(0,4):
                returnedString = ""
                if i is 0:
                     returnedString = AI.thestring(self, num - 1, nowString + "0", aList)
                if i is 1:
                     returnedString = AI.thestring(self, num - 1, nowString + "1", aList)
                if i is 2:
                     returnedString = AI.thestring(self, num - 1, nowString + "2", aList)
                if i is 3:
                     returnedString = AI.thestring(self, num - 1, nowString + "3", aList)
                if returnedString != " ":
                     return returnedString
                #把真正的值向上传递
            return " "
#        else:
#            return "-1"

    def attackenemy(self):
        (x,y) = self.robot.position
        r = self.robot.rotation
        (ep,er) = self.robot.locateEnemy()
        print("ATTACK!")
        if abs(ep[0] - x) + abs(ep[1] - y) == 1:
            if r is 0:
                if ep[0] - x is 1:
                    self.robot.turnRight()
                    return
                if ep[0]-x is -1:
                    self.robot.turnLeft()
                    return
                if ep[1]-y is 1:
                    self.robot.turnRight()
                    return
                if ep[1]-y is -1:
                    self.robot.attack()
                    return
            elif r is 1:
                if ep[0] - x is 1:
                    self.robot.attack()
                    return
                if ep[0]-x is -1:
                    self.robot.turnRight()
                    return
                if ep[1]-y is 1:
                    self.robot.turnRight()
                    return
                if ep[1]-y is -1:
                    self.robot.turnLeft()
                    return
            elif r is 2:
                if ep[0] - x is 1:
                    self.robot.turnLeft()
                    return
                if ep[0]-x is -1:
                    self.robot.turnRight()
                    return
                if ep[1]-y is 1:
                    self.robot.attack()
                    return
                if ep[1]-y is -1:
                    self.robot.turnRight()
                    return
            elif r is 3:
                if ep[0] - x is 1:
                    self.robot.turnRight()
                    return
                if ep[0]-x is -1:
                    self.robot.attack()
                    return
                if ep[1]-y is 1:
                    self.robot.turnLeft()
                    return
                if ep[1]-y is -1:
                    self.robot.turnRight()
                    return
        if ep[0]>x and ep[1]>y:
            if r is 0 or r is 3:
                self.robot.goBack()
                return
            if r is 1 or r is 2:
                self.robot.goForth()
                return
        if ep[0]<x and ep[1]>y:
            if r is 0 or r is 1:
                self.robot.goBack()
                return
            if r is 3 or r is 2:
                self.robot.goForth()
                return
        if ep[0]>x and ep[1]<y:
            if r is 0 or r is 1:
                self.robot.goForth()
                return
            if r is 3 or r is 2:
                self.robot.goBack()
                return
        if ep[0]<x and ep[1]<y:
            if r is 0 or r is 3:
                self.robot.goForth()
                return
            if r is 1 or r is 2:
                self.robot.goBack()
                return
        if ep[0]>x and ep[1]is y:
            if r is 0 :
                self.robot.turnRight()
                return
            if r is 1:
                self.robot.goForth()
                return
            if r is 2:
                self.robot.turnLeft()
                return
            if r is 3:
                self.robot.turnLeft()
                return
        if ep[0]<x and ep[1]is y:
            if r is 0 :
                self.robot.turnLeft()
                return
            if r is 1:
                self.robot.turnLeft()
                return
            if r is 2:
                self.robot.turnRight()
                return
            if r is 3:
                self.robot.goForth()
                return
        if ep[0]is x and ep[1]> y:
            if r is 0 :
                self.robot.turnLeft()
                return
            if r is 1:
                self.robot.turnRight()
                return
            if r is 2:
                self.robot.goForth()
                return
            if r is 3:
                self.robot.turnLeft()
                return
        if ep[0]is x and ep[1]< y:
            if r is 0 :
                self.robot.goForth()
                return
            if r is 1:
                self.robot.turnLeft()
                return
            if r is 2:
                self.robot.turnLeft()
                return
            if r is 3:
                self.robot.turnRight()
                return



    def printgraph(self, aList):
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

    def turn(self):
        stringnow = ""
        myAtk = self.robot.ATK
        currenthp = self.robot.health
        (ep, er) = self.robot.locateEnemy()
        currentList = AI.drawgraph(self)
        myPosition = self.robot.position
        myRotation = self.robot.rotation
        #AI.printgraph(self, currentList)
        the_string_I_want = "-"
        numOfItem = 0
        for i in range(0, 10):
            for k in range(0, 10):
                if currentList[i][k] is "HP" or currentList[i][k] is "ATK": #or currentList[i][k] is "SPD":
                    numOfItem += 1
        if numOfItem is 0:
            if self.mode is 1:
                AI.attackenemy(self)
        if abs(ep[0] - myPosition[0]) + abs(ep[1] - myPosition[1]) == 1:
            AI.attackenemy(self)
            return

        for i in range(0,9):
            the_string_I_might_want = AI.thestring(self, i, stringnow, currentList)
            if the_string_I_might_want != " ":
                the_string_I_want = the_string_I_might_want
                break
        print("string is ",the_string_I_want)
            
        #for i in range(0,len(the_string_I_want)):
#        if the_string_I_want[0] is "-1":
#            self.robot.doNothing()

        #try 就是报错了能打出来
        if the_string_I_want[0] is "0":
            print("Forth")
            self.robot.goForth()
        elif the_string_I_want[0] is "1":
            print("Back")
            self.robot.goBack()
        elif the_string_I_want[0] is "2":
            print("Left")
            self.robot.turnLeft()
        elif the_string_I_want[0] is "3":
            print("Right")
            self.robot.turnRight()
        else:
            AI.attackenemy(self)



