import math
import random
import traceback
import time
import datetime
import random

#现在可以加的东西： 1.吃加速
#                  2.卡住之后自动寻路到中心
#                  3.打不过之后有效的逃跑

# 坐标：
 # x 0~9
 # y 0~9
 #       │
 #       │
 #       │
 # ──────┼────────────────→X+
 #       │
 #       │
 #       │
 #       ↓
 #       Y+
 
 
# 旋转：
 # 0 = y-
 # 1 = x+
 # 2 = y+
 # 3 = x-
 # + = 


# potentialBUG1  #movements_back_1必须包括movements_0、movements_1和movements_back_0内容
                 #暂时不会引发问题 只要不乱改movements
                 
# potentialBUG2  #动态障碍可能导致寻路有问题
                 
# potentialBUG3  #因为先扫描场景再开始requireTarget
                 #self.avoidEnemy延迟一回合生效
                 
class AI:
    #数组结构避免了一大堆if
    movements_0 = [[[0,-1,0],[0,0,0],[0,0,3],[0,0,1]],[[1,0,0],[0,0,0],[0,0,-1],[0,0,1]],[[0,1,0],[0,0,0],[0,0,-1],[0,0,1]],[[-1,0,0],[0,0,0],[0,0,-1],[0,0,-3]]] #拒绝开倒车
    movements_1 = [[[0,-1,0],[0,0,0],[0,0,3],[0,0,1],[0,-2,0]],[[1,0,0],[0,0,0],[0,0,-1],[0,0,1],[2,0,0]],[[0,1,0],[0,0,0],[0,0,-1],[0,0,1],[0,2,0]],[[-1,0,0],[0,0,0],[0,0,-1],[0,0,-3],[-2,0,0]]]
    movements = [movements_0, movements_1]
    movements_back_0 = [[[0,-1,0],[0,1,0],[0,0,3],[0,0,1]],[[1,0,0],[-1,0,0],[0,0,-1],[0,0,1]],[[0,1,0],[0,-1,0],[0,0,-1],[0,0,1]],[[-1,0,0],[1,0,0],[0,0,-1],[0,0,-3]]]
    movements_back_1 = [[[0,-1,0],[0,1,0],[0,0,3],[0,0,1],[0,-2,0],[0,2,0]],[[1,0,0],[-1,0,0],[0,0,-1],[0,0,1],[2,0,0],[-2,0,0]],[[0,1,0],[0,-1,0],[0,0,-1],[0,0,1],[0,2,0],[0,-2,0]],[[-1,0,0],[1,0,0],[0,0,-1],[0,0,-3],[-2,0,0],[2,0,0]]]
    movements_back = [movements_back_0, movements_back_1]
    weakpoints = [[[0,1,0],[-1,0,1],[1,0,3]],[[-1,0,1],[0,-1,2],[0,1,0]],[[0,-1,2],[1,0,3],[-1,0,1]],[[1,0,3],[0,1,0],[0,-1,2]]]
    allzone = ["me", "bot", "wall", "clear", "HP", "ATK", "SPD", "avoidzone"]
    accessable = ["me","bot", "clear", "HP", "ATK", "SPD"] #可走的格
    accessable_strict = ["me", "clear", "HP", "ATK", "SPD"] #可走的格
    objectstring_0 = ["HP", "ATK", "SPD"]
    objectstring_1 = ["HP", "ATK"]
    objectstring = [objectstring_0,objectstring_1]
    map_width = 10
    map_height = 10
    
    def __init__(self):
        self.target = None
        self.alpha = 1 #启发函数权重
        #self.avoidEnemy = True
        self.allowBack = False #允许倒着走吗
        self.fitRotation = False #目标有朝向吗
        self.avoidd = 0 #躲开敌人多远, 0=躲开敌人那一格 -1=不躲开
    
    def scanScene(self):
        scene = [([None] * 10) for i in range(10)]
        for x in range(AI.map_width):
            for y in range(AI.map_height):
                scene[x][y] = self.robot.lookAtSpace((x+1, y+1))
        return scene
    def postScanScene(self, scene):
        pass
#        for x in range(AI.map_width):
#            for y in range(AI.map_height):
#                if self.avoidEnemy and scene[x][y] == "bot":
#                    for dx in range(-1, 2):
#                        for dy in range(-1, 2):
#                            if dx != 0 or dy != 0:
#                                thisx = x +dx
#                                thisy = y +dy
#                                if thisx>-1 and thisx<AI.map_width and thisy>-1 and thisy <AI.map_height:
#                                    if scene[thisx][thisy] =="clear":
#                                        scene[thisx][thisy] = "clear" #potentialBUG2 we first do something like this to test attacking sequence
#        for x in range(AI.map_width):
#            for y in range(AI.map_height):
#                if self.avoidEnemy and scene[x][y] == "me":
#                    for dx in range(-1, 2):
#                        for dy in range(-1, 2):
#                            if dx != 0 or dy != 0:
#                                thisx = x +dx
#                                thisy = y +dy
#                                if thisx>-1 and thisx<AI.map_width and thisy>-1 and thisy <AI.map_height:
#                                    if scene[thisx][thisy] == "avoidzone":
#                                        scene[thisx][thisy] = "clear" #potentialBUG2
                    
    
    
    #--------------------------------------------------↓ 点相关 ↓-------------
    #-------------点相加-------------
    def addP(P1,P2):
        P3 = [P1[0]+P2[0], P1[1]+P2[1], P1[2]+P2[2]]
        return P3
    def middleP(P1,P2):
        P3 = [round((P1[0]+P2[0])/2), round((P1[1]+P2[1])/2), round((P1[2]+P2[2])/2)]
        return P3
    #-------------点相等-------------
    def pointEqual(P1, P2):
        if P1==None or P2==None:
            return False
        return (P1[0]==P2[0] and P1[1]==P2[1] and P1[2]==P2[2])
    def pointEqual2D(P1, P2):
        if P1==None or P2==None:
            return False
        return (P1[0]==P2[0] and P1[1]==P2[1])
    #-------------曼哈顿距离3D-------------
    def taxiDist3D(P1,P2):
        return abs(P1[0]-P2[0])+abs(P1[1]-P2[1])+abs(P1[2]-P2[2])
    #-------------曼哈顿距离2D-------------
    def taxiDist2D(P1,P2):
        return abs(P1[0]-P2[0])+abs(P1[1]-P2[1])
    #-------------预估对方行动到某格需要的步数-------------
    def estSteps(eP, tP):
        res = AI.taxiDist2D(eP, tP) + 1
        if eP[2] == 0 or eP[2] == 2:
            if eP[0] == tP[0]:
                res -= 1
        elif eP[2] == 1 or eP[2] == 3:
            if eP[1] == tP[1]:
                res -= 1
        return res
            
    #-------------点在范围内-------------
    def isInRange(P):
        return (P[0]>-1 and P[0]<AI.map_width and P[1]>-1 and P[1]<AI.map_height)
    #-------------检查点不是障碍物-------------
    def sampleMap(P, scene, accessable, eP, avoidd):
        #accessable = AI.accessable
        data = scene[P[0]][P[1]]
        if data in accessable:
            if AI.estSteps(eP, P) <= avoidd:
                return False
            else:
                return True
        return False
    #-------------随机点-------------
    def randomPoint(scene, accessable):
        availablepoints = []
        for px in range(2,7):
            for py in range(2,7):
                if AI.sampleMap([px,py,0], scene, accessable, [0,0,0], -1):
                    availablepoints.append([px,py])
        if len(availablepoints)==0:
            return None
        randp = availablepoints[random.randint(0, len(availablepoints)-1)]
        return [randp[0], randp[1], random.randint(0,3)]
    #-------------点的数组里点P的位置 没有则为-1-------------
    def pointIndex(P, L):
        for pindex in range(len(L)):
            if AI.pointEqual(P, L[pindex]):
                return pindex
        return -1
    def pointIndex2D(P, L):
        for pindex in range(len(L)):
            if AI.pointEqual2D(P, L[pindex]):
                return pindex
        return -1
    #--------------------------------------------------↑ 点相关 ↑-------------
    
    #--------------------------------------------------↓ A* 寻路相关 ↓-------------
    #-------------创建节点-------------
    def node(P, parentP, value):
        n = {}
        n["P"] = P
        n["pP"] = parentP
        n["v"] = value
        return n
    
    #-------------close节点-------------
    def closeNode(N, closedList, openList):
        node_i = AI.isInside(N["P"], openList)
        if node_i != -1:#有此项
            del openList[node_i]
            closedList.append(N)#有才加
    #-------------新建或reopen节点-------------
    def openNode(N, closedList, openList):
        node_i = AI.isInside(N["P"], closedList)
        if node_i != -1:#有此项
            del closedList[node_i]
        openList.append(N)#无论有没有都加
    
    #-------------node的数组中有没有点P-------------
    def isInside(P, L):
        for node_i in range(len(L)):
            if AI.pointEqual(P, L[node_i]["P"]):
                return node_i
        return -1
    #-------------下一个该处理的节点-------------
    def minNode(L, tP, alpha):
        minvalue = 2333333333333 #一个很大的数#永远比节点大
        minnode = None
        for node_i in range(len(L)):
            estvalue = L[node_i]["v"] + alpha*AI.h(L[node_i]["P"], tP)
            #print(estvalue)
            if estvalue < minvalue:
                minvalue = estvalue
                minnode = L[node_i]
        return minnode
    #-------------找父节点-------------
    def findParent(N, closedList, openList):
        if N["pP"] == None:
            return None
        inClosed = AI.isInside(N["pP"], closedList)
        inOpen = AI.isInside(N["pP"], openList)
        if inClosed != -1:
            return closedList[inClosed]
        elif inOpen != -1:
            return openList[inOpen]
        return None
        
    #-------------估价-------------
    def h(P,tP):
        return AI.taxiDist2D(P,tP)
        
    #-------------位移转为动作序号-------------
    def stepFromTo(Pfrom, Pto):
        #print(Pfrom)
        possiblemovements = AI.movements_back[1][Pfrom[2]] #potentialBUG1
        for move_i in range(len(possiblemovements)):
            if AI.pointEqual(AI.addP(Pfrom, possiblemovements[move_i]),Pto):
                return str(move_i)
        return "x"#没有这种操作#正常情况不可能走到这
    
    #-------------节点链转为字符串-------------
    def formatOutput(fN, closedList, openList):
        outputstr = ""
        currentN = fN
        parentN = AI.findParent(fN, closedList, openList)
        while parentN != None:
            outputstr = AI.stepFromTo(parentN["P"], currentN["P"]) + outputstr
            currentN = parentN
            parentN = AI.findParent(parentN, closedList, openList)
        return outputstr
    
    #-------------找路-------------
    def findPath(myP, eP, tP, scene, alpha, avoidd, fitRotation, allowBack, boost, printLog):# X,Y∈[0,9]∩N
        print("开始findPath from",myP,"to",tP)
        if myP==None or tP==None or scene==None:
            print("参数为None",myP, tP, scene)
            input()
            return None
        if not(AI.isInRange(tP) and AI.sampleMap(tP, scene, AI.accessable, eP, avoidd)):
            print("target is blocked") #目标是墙 或者需avoid
            #input()
            return None
        if not(AI.isInRange(myP) and AI.sampleMap(myP, scene, AI.accessable, eP, avoidd)):
            print("I am blocked! 设置avoidd的时候应该先检查一下自己是否在avoid范围") #自己是墙 或者需avoid
            input()
            return None
        if AI.pointEqual(myP, tP) or (not(fitRotation) and AI.pointEqual2D(myP, tP)): #已在目标
            print("already at target")
            return ""
        movements = AI.movements[boost]
        if allowBack:
            movements = AI.movements_back[boost]
        starttime = datetime.datetime.now()
        closedList = []
        openList = []
        openList.append(AI.node(myP, None, 0))
        counter = 0
        while True:
            counter += 1
            if counter > 20000:
                print("too much work")
                return None
            thisnode = AI.minNode(openList, tP, alpha)
            if thisnode == None: #已搜索全图找不到结果
                #print(openList)
                print(tP, alpha, counter)
                print("findPath未找到 用时", (datetime.datetime.now()-starttime).microseconds/1000, "ms") #target被墙围住
                #input()
                return None
            if printLog:
                print("checking", thisnode["P"], "from" , thisnode["pP"])
            possiblemove = movements[thisnode["P"][2]]
            if printLog:
                print("possible move ", possiblemove)
            for nextmove in possiblemove:
                nextP = AI.addP(thisnode["P"], nextmove)
                nextvalue = thisnode["v"] + 1
                if printLog:
                    print("next node @ ", nextP, "value=", nextvalue)
                if AI.isInRange(nextP) and AI.sampleMap(nextP, scene, AI.accessable, eP, avoidd):
                    if AI.taxiDist2D(thisnode["P"], nextP)==2 and not(AI.sampleMap(AI.middleP(thisnode["P"], nextP), scene, AI.accessable, eP, 0)):
                        continue
                    isOpen = AI.isInside(nextP, openList)
                    isClosed = AI.isInside(nextP, closedList)
                    if isOpen != -1:
                        opennode = openList[isOpen]
                        if opennode["v"] > nextvalue: #更新open节点
                            opennode["v"] = nextvalue
                            opennode["pP"] = thisnode["P"]
                            if printLog:
                                print("updated open node @ ", nextP, "value=", nextvalue)
                    elif isClosed != -1:
                        closednode = closedList[isClosed]
                        if closednode["v"] > nextvalue:
                            closednode["v"] = nextvalue
                            closednode["pP"] = thisnode["P"]
                            AI.openNode(closednode, closedList, openList) #重新打开节点
                            if printLog:
                                print("reopened node @ ", nextP, "value=", nextvalue)
                    else:
                        AI.openNode(AI.node(nextP, thisnode["P"], nextvalue), closedList, openList) #新节点
                        if printLog:
                            print("opened node @ ", nextP, "value=", nextvalue)
                        if AI.pointEqual(nextP, tP) or (not(fitRotation) and AI.pointEqual2D(nextP, tP)): #路径完成
                            print("完成findPath 用时", (datetime.datetime.now()-starttime).microseconds/1000, "ms")
                            return AI.formatOutput(openList[len(openList)-1], closedList, openList)
            if printLog:
                print("closing node @ ", thisnode["P"], "value=", thisnode["v"], "remaining", len(openList))
            AI.closeNode(thisnode, closedList, openList) #close节点
        return None
    #--------------------------------------------------↑ A* 寻路相关 ↑-------------
              
    #-------------执行路径第一步-------------  
    def executePath(self, myP, eP, path):
        if self.robot.lookInFront is "bot":
            print("Attack")
            self.robot.attack()
        if path == None or len(path) == 0:
            print("no path to excurte")
        elif path[0] is "0":
            aftermove = AI.addP(myP, AI.movements_back[1][myP[2]][0]) #potentialBUG1
            #print(aftermove, myP, eP)
            if AI.pointEqual2D(aftermove, eP):
                print("Attack")
                self.robot.attack()
            else:
                print("Forth")
                self.robot.goForth()
        elif path[0] is "1":
            print("Back")
            self.robot.goBack()
        elif path[0] is "2":
            print("Left")
            self.robot.turnLeft()
        elif path[0] is "3":
            print("Right")
            self.robot.turnRight()
        elif path[0] is "4":
            aftermove = AI.addP(myP, AI.movements_back[1][myP[2]][4]) #potentialBUG1
            if AI.pointEqual2D(aftermove, eP):
                print("Forth")
                self.robot.goForth()
            else:
                print("Forth2")
                self.robot.goForth2()
        elif path[0] is "5":
            print("Back2")
            self.robot.goBack2()
    
    def getMyP(self):
        myPosition = self.robot.position
        myRotation = self.robot.rotation
        myP = [myPosition[0]-1, myPosition[1]-1, myRotation]
        return myP
    def getEP(self):
        (ep, er) = self.robot.locateEnemy()
        eP = [ep[0]-1, ep[1]-1, er]
        return eP
    
    #requireTarget函数
    #只要在这里面写东西就可以控制战术
    #每回合会被调用至少一次
    #在这里根据传入的参数分析，得出要前往的目标，目标必须是一个三个数的数组[x,y,rotation]
    #返回这个数组，坦克会寻路并前往这个目标，如果要保持之前的目标不变就返回self.target
    #返回一个值之后主函数turn会检查这个目标是否可行，如果不可行就加入failed数组，重新调用这个函数，找一个新目标，直到可行为止
    #此外还可以更改三个布尔值self.fitRotation self.avoidEnemy self.allowBack来控制寻路时的具体行为  #potentialBUG3
    #不要直接更改self.target 交给主函数来做
    #
    #参数：
    #myP：一个数组[x,y,rotation]自己的位置和方向
    #eP：一个数组[x,y,rotation]敌人的位置和方向
    #myInfo：一个tuple(HP,ATK,Speed)自己的属性
    #eInfo：一个tuple(HP,ATK,Speed)敌人的属性，当不能得到敌人属性是会是None
    #scene：场景二维数组
    #failed：之前失败的目标[x,y,rotation]构成的数组。返回目标前有必要检查目标是不是之前失败过
    #        AI.pointIndex2D(目标, failed)如果等于-1说明没有失败过
    #        如果失败过就不应该返回，应该在找另一个目标
    #
    #现在这里面写的是一个随机AI（并不是简单的随机移动而是去往随机目标）
    #可以删了重新写正常AI的战术
    def getobjectList(self,scene):
        objectlist = []
        for x in range(AI.map_width):
            for y in range(AI.map_height):
                if self.robot.speedUP is 0:
                    for object in AI.objectstring[0]:
                        if scene[x][y] is object:
                            objectlist.append([x,y])
                if self.robot.speedUP is 1:
                    for object in AI.objectstring[1]:
                        if scene[x][y] is object:
                            objectlist.append([x,y])
        return objectlist

    def getWeakPoint(self, myP, eP, failed):
        #eP = AI.getEP(self)
        if self.robot.lookInFront() is "bot":
            #return [eP[0], eP[1], self.robot.rotation]
            return myP
        nearest = 23333333
        nearestp = None
        allwp = AI.weakpoints[eP[2]];
        for wp in allwp:
            thiswp = AI.addP(eP, wp)
            thiswp[2] = wp[2]
            if AI.isInRange(thiswp) and AI.pointIndex2D(thiswp, failed) == -1:
                tdist = AI.taxiDist2D(myP, thiswp)
                if tdist < nearest:
                    nearest = tdist
                    nearestp = thiswp
        return nearestp
#        if eP[2] is 0:
#            if eP[1]+1<=10:
#                eP[1] += 1
#                if AI.pointIndex2D(eP, failed) == -1:
#                    return [eP[0],eP[1],0]
#            if eP[0]-1>=1:
#                eP[0] -= 1
#                if AI.pointIndex2D(eP, failed) == -1:
#                    return [eP[0],eP[1],1]
#            if eP[0]+1<=10:
#                eP[0] += 1
#                if AI.pointIndex2D(eP, failed) == -1:
#                    return [eP[0],eP[1],3]
#            return None
#        if eP[2] is 1:
#            if eP[0] - 1 >= 1:
#                eP[0] -= 1
#                if AI.pointIndex2D(eP, failed) == -1:
#                    return [eP[0], eP[1], 1]
#            if eP[1] - 1 >= 1:
#                eP[1] -= 1
#                if AI.pointIndex2D(eP, failed) == -1:
#                    return [eP[0], eP[1], 2]
#            if eP[1] + 1 <= 10:
#                eP[1] += 1
#                if AI.pointIndex2D(eP, failed) == -1:
#                    return [eP[0], eP[1], 0]
#            return None
#        if eP[2] is 2:
#            if eP[1]-1>=1:
#                eP[1] -= 1
#                if AI.pointIndex2D(eP, failed) == -1:
#                    return [eP[0],eP[1],2]
#            if eP[0]-1>=1:
#                eP[0] -= 1
#                if AI.pointIndex2D(eP, failed) == -1:
#                    return [eP[0],eP[1],1]
#            if eP[0]+1<=10:
#                eP[0] += 1
#                if AI.pointIndex2D(eP, failed) == -1:
#                    return [eP[0],eP[1],3]
#            return None
#        if eP[2] is 3:
#            if eP[0] + 1 >= 10:
#                eP[0] += 1
#                if AI.pointIndex2D(eP, failed) == -1:
#                    return [eP[0] , eP[1], 3]
#            if eP[1] - 1 >= 1:
#                eP[1] -= 1
#                if AI.pointIndex2D(eP, failed) == -1:
#                    return [eP[0], eP[1], 2]
#            if eP[1] + 1 <= 10:
#                eP[1] += 1
#                if AI.pointIndex2D(eP, failed) == -1:
#                    return [eP[0], eP[1], 0]
#            return None
    def requireTarget(self, myP, eP, myInfo, eInfo, scene, failed, objectlist):
        #①
        #找东西吃
        Dis = 200
        index = -1
        cindex = 0
        aim = None
        if objectlist != []:
            for object in objectlist:
                self.allowBack = True
                self.fitRotation = False
                if AI.pointIndex2D(object, failed) == -1:
                    dis_ = AI.taxiDist2D(myP, object)
                    if dis_ < Dis:
                        Dis = dis_
                        index = cindex
                cindex += 1
            if index!=-1:
                aim = [objectlist[index][0], objectlist[index][1], 0]
        #有东西就吃
        if aim!= None: 
            self.allowBack = True
            self.fitRotation = False
            self.avoidd = 2 #离敌人远点
            if AI.estSteps(eP, myP) <= 2: #但是如果敌人靠近了我们呢？
                pass #不要去吃东西了，去打他
            else:
                return aim
        
        #②
        #不吃东西时找weakpoint
        weakpoint = self.getWeakPoint(myP, eP, failed)
        if weakpoint != None:
            if AI.pointEqual(myP, weakpoint): # 如果已经到了weakpoint
                #打他
                self.avoidd = -1
                self.allowBack = False
                self.fitRotation = False
                return eP
            else: #如果没到weakpoint
                self.allowBack = False
                self.fitRotation = True
                self.avoidd = 0
                return weakpoint
        
        #③
        #如果没吃的，也没有weakpoint怎么办？
        #随机走
        if self.target==None or AI.pointEqual(self.target, myP): #初始化或到了原目标
            return AI.randomPoint(scene, AI.accessable) #随机下一个目标
        else: #没到原目标
            if AI.pointIndex2D(self.target, failed) == -1: #原目标可行
                return self.target #不变
            else:
                return AI.randomPoint(scene, AI.accessable)
                
            
    def turn(self):
        try:
            #input("input any key to continue")
            #if self.robot.lookInFront() is "bot":
                #self.robot.attack()
                #return
            currentScene = self.scanScene()
            self.postScanScene(currentScene)
            objectList = self.getobjectList(currentScene)
            print(objectList)
            myHP = self.robot.health
            myATK = self.robot.ATK
            mySpeed = self.robot.speedUP
            myInfo = (myHP, myATK, mySpeed)#tuple
            eDetect = self.robot.detectEnemy()
            eInfo = None
            if not(eDetect == None):
                eHP = eDetect[2]
                eATK = eDetect[3]
                eSpeed = eDetect[4]
                eInfo = (eHP, eATK, eSpeed)#tuple
            
            myP = self.getMyP()
            eP = self.getEP()
            
            path_result = None
            failed_targets = []
            attempt = 0
            while True:
                attempt += 1
                if attempt > 300:
                    print("目标失败次数过多")
                    input() #先暂停
                    return #跳过回合
                req = self.requireTarget(myP, eP, myInfo, eInfo, currentScene, failed_targets, objectList)
                if req == None:
                    print("target can't be None")
                else:
                    #self.target = req
                    if not(AI.pointEqual(self.target, req)):
                        print("目标更新", req)
                    path_result = AI.findPath(myP, eP, req, currentScene, self.alpha, self.avoidd, self.fitRotation, self.allowBack, mySpeed, False)
                    if path_result == None or path_result == "":
                        print("目标不可行", req)
                        failed_targets.append(req)
                    else:
                        self.target = req
                        break
            
            print("path_result is ",path_result)
            
            self.executePath(myP, eP, path_result)

            print("----------------turn ended----------------")
            
            #time.sleep(0.5)
        except:
            traceback.print_exc()
