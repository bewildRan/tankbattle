# Listing 26-2
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# PythonBattle AI - second attempt to beat CircleAI

# Note that this is not a complete Python program itself,
#   it is a module called by the PythonBattle program.
# Save this as something like "morecomplicatedai.py"
#   and try it in a battle against circleai.

import random
class AI:
    def __init__(self):
        pass
    def turn(self):
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
            return
        elif self.robot.lookInFront() == "HP" :
            self.robot.goForth()
            return
        elif self.robot.lookInFront() == "SPD" :
            self.robot.goForth()
            return
        elif self.robot.lookInFront() == "ATK" :
            self.robot.goForth()
            return
        elif self.robot.lookInFront() == "wall":            
                random.choice([self.robot.turnLeft,self.robot.turnRight])()
                return
        else:
                mylocation=self.robot.position
                HX=[]
                HY=[]
                x=1
                y=1
                for x in range(1,11):
                    for y in range (1,11):
                        if self.robot.lookAtSpace((x,y))=="HP" :
                            HX.append(x)
                            HY.append(y)
                        if self.robot.lookAtSpace((x,y))=="ATK":
                            HX.append(x)
                            HY.append(y)
                        if self.robot.lookAtSpace((x,y))=="SPD":
                            HX.append(x)
                            HY.append(y)
                if len(HX)==0:
                    random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goBack])()
                else:
                    a=HX[0]-mylocation[0]
                    b=HY[0]-mylocation[1]
                    i=1
                    for i in range(1,len(HX)):  
                        c=HX[i]-mylocation[0]
                        d=HY[i]-mylocation[1]
                        if((abs(c)+abs(d))<(abs(a)+abs(b))):
                            a=c
                            b=d
                    HX=[]
                    HY=[]
                    x=1
                    y=1
                    if self.robot.rotation==0 or self.robot.rotation==2:
                            if a>0:
                                self.robot.goForth()
                            if a==0:
                                if b>0:
                                    self.robot.turnRight()
                                else:
                                    self.robot.turnLeft()
                            else:
                                self.robot.goBack()
                    elif self.robot.rotation==1 or self.robot.rotation==3:
                            if b>0:
                                self.robot.goForth()
                            if b==0:
                                if a>0:
                                    self.robot.turnRight()
                                else:
                                    self.robot.turnLeft()
                            else:
                                self.robot.goBack()
