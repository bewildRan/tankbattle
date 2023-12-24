import random

#坦克参数
class BOTPARAMETER:
    name=""     #名字
    p = (0,0)   #当前位置
    r = -1      #当前方向
    HP = -1     #当前血量
    ATK = -1    #当前攻击力
    SPD = -1    #加速器
    GridScore = 0   #当前格子分数
    GainHP = 0  #捡到HP次数
    GainATK = 0 #捡到ATK次数
    def __init__(self,p=(1,1),r=0,HP=100,ATK=10,SPD=0,GridScore=0,GainHP=0,GainATK=0):
        self.name = ""
        self.p = p
        self.r = r
        self.HP = HP
        self.ATK = ATK
        self.SPD = SPD
        self.GridScore = GridScore
        self.GainHP = GainHP
        self.GainATK = GainATK

    def debugPrintCurState(self,pre=""):
        print(pre+"name:"+str(self.name),"p:"+str(self.p),"r:"+str(self.r),"HP:"+str(self.HP),"ATK:"+str(self.ATK),"SPD:"+str(self.SPD),"GridScore:"+str(self.GridScore),"GainHP:"+str(self.GainHP),"GainATK:"+str(self.GainATK))


#关键物品位置
class STATEKEYPOS:
    PosMe = (0,0)   #自己的位置
    PosBot = (0,0)  #对手的位置
    LPosGoldGrid = []   #金色格子位置集合
    LPosWall = []   #墙的位置集合
    LPosClear = []  #空的位置集合
    LPosHP = []     #加血的位置集合
    LPosATK = []    #加攻击的位置集合
    LPosSPD = []    #加速度的位置集合
    LPosGridNotMe = []  #所有不属于我方的格子集合

    #清空状态值
    def fclear(self):
        self.PosMe = (0,0)   #自己的位置
        self.PosBot = (0,0)  #对手的位置
        self.LPosGoldGrid = []   #金色格子位置集合
        self.LPosWall = []   #墙的位置集合
        self.LPosClear = []  #空的位置集合
        self.LPosHP = []     #加血的位置集合
        self.LPosATK = []    #加攻击的位置集合
        self.LPosSPD = []    #加速度的位置集合
        self.LPosGridNotMe = []  #所有不属于我方的格子集合


    #输出当前的状态值
    def debugPrintStatePos(self,pre=""):
        temp = "KeyPos [Me:"+str(self.PosMe)+"]\t[Bot:"+str(self.PosBot)+"]"
        print(pre+temp)
        temp = "\tWall:"
        for p in self.LPosWall:
            temp+=str(p)
        print(pre+temp)        
        temp = "\tClear:"
        for p in self.LPosClear:
            temp+=str(p)
        print(pre+temp)        
        temp = "\tHP:"
        for p in self.LPosHP:
            temp+=str(p)
        print(pre+temp)        
        temp = "\tATK:"
        for p in self.LPosATK:
            temp+=str(p)
        print(pre+temp)        
        temp = "\tSPD:"
        for p in self.LPosSPD:
            temp+=str(p)
        print(pre+temp)      
        temp = "\tGold Grid:"
        for p in self.LPosGoldGrid:
            temp+=str(p)
        print(pre+temp)             
        temp = "\tGrid of other':"
        for p in self.LPosGridNotMe:
            temp+=str(p)
        print(pre+temp)
        
#状态参数
class STATEPARAMETER:
    #全局状态参数
    RowMax = 0      #地图范围（RowMax，ColumnMax）
    ColumnMax = 0   #地图范围（RowMax，ColumnMax）
    #环境状态
    MapMatrix = [[],[]]         #地图矩阵
    MapMatrixLast = [[],[]]     #上一轮的地图矩阵
    GridStateMatrix = [[],[]]   #格子状态矩阵
    GoldGradLocation = (4,4)    #金色格子位置
    GoldGradPoint = 15          #金色格子点数
    #战斗状态
    RoundMax = 0        #最大回合数
    RoundCurrent = 0    #当前回合数
    #关键物品位置
    PosKeyThing = STATEKEYPOS()

    def __init__(self,RowMax=10,ColumnMax=10,GoldGradLocation=(4,4),GoldGradPoint=15,RoundMax=0):
        self.RowMax = RowMax
        self.ColumnMax = ColumnMax
        self.MapMatrix = [([0] * self.ColumnMax) for i in range(self.RowMax)]
        self.MapMatrixLast = [([0] * self.ColumnMax) for i in range(self.RowMax)]
        self.GridStateMatrix = [([0] * self.ColumnMax) for i in range(self.RowMax)]
        self.GoldGradLocation = GoldGradLocation
        self.GoldGradPoint = GoldGradPoint
        self.RoundMax = RoundMax
        self.RoundCurrent = 0

    #获得当前状态的主函数
    def ObtainCurrentState(self,robot,roundI):
        #获得当前地图状态
        RowMax = self.RowMax
        ColumnMax = self.ColumnMax
        for i in range(0,RowMax):
            for j in range(0,ColumnMax):
                self.MapMatrix[i][j] = robot.lookAtSpace((j+1,i+1))
        #self.debugPrintMapMatrix()

        #获得当前格子状态
        self.UpdataGridStateMatrix()
        #self.debugPrintGridStateMatrix()

        #更新关键物品的状态
        self.UpdatePosKeyThing()
        #self.PosKeyThing.debugPrintStatePos()

    #更新关键物品的状态
    def UpdatePosKeyThing(self):
        self.PosKeyThing.fclear()   #清空上一轮的状态
        RowMax = self.RowMax
        ColumnMax = self.ColumnMax
        for i in range(0,RowMax):
            for j in range(0,ColumnMax):
                tthing = self.MapMatrix[i][j]
                if tthing == "me":
                    self.PosKeyThing.PosMe = (i,j)
                elif tthing == "bot":
                    self.PosKeyThing.PosBot = (i,j)
                elif tthing == "wall":
                    self.PosKeyThing.LPosWall.append((i,j))
                elif tthing == "clear":
                    self.PosKeyThing.LPosClear.append((i,j))
                elif tthing == "HP":
                    self.PosKeyThing.LPosHP.append((i,j))
                elif tthing == "ATK":
                    self.PosKeyThing.LPosATK.append((i,j))
                elif tthing == "SPD":
                    self.PosKeyThing.LPosSPD.append((i,j))
        self.PosKeyThing.LPosGoldGrid.append((4,4))
        #得到不属于自己的格子
        ##优先加入金色格子
        if self.GridStateMatrix[self.GoldGradLocation[0]][self.GoldGradLocation[1]] !=1:
            self.PosKeyThing.LPosGridNotMe.append(self.GoldGradLocation)
        ##优先加入敌人的格子
        for i in range(0,RowMax):
            for j in range(0,ColumnMax):
                if self.GridStateMatrix[i][j]==-1 and self.MapMatrix[i][j]!="bot":
                    self.PosKeyThing.LPosGridNotMe.append((i,j))
        ##加入空白的格子
        for i in range(0,RowMax):
            for j in range(0,ColumnMax):
                if self.GridStateMatrix[i][j]!=1 and self.MapMatrix[i][j]!="bot":
                    self.PosKeyThing.LPosGridNotMe.append((i,j))
        return
                    
        
    #更新上一轮的地图状态为当前状态
    def UpdateMapMatrixLast(self):  
        RowMax = self.RowMax
        ColumnMax = self.ColumnMax
        for i in range(0,RowMax):
            for j in range(0,ColumnMax):
                self.MapMatrixLast[i][j] = self.MapMatrix[i][j]

    #更新格子状态矩阵GridStateMatrix
    def UpdataGridStateMatrix(self):
        (x,y)=self.FindMeInMapMatrix()
        self.GridStateMatrix[x][y] = 1
        (x,y)=self.FindBotInMapMatrix()
        self.GridStateMatrix[x][y] = -1

    #更新回合数
    def UpdataRoundCurrent(self):
        self.RoundCurrent += 1

    #找到me的当前位置
    def FindMeInMapMatrix(self):
        return self.FindValuePosition("me",self.MapMatrix)

    #找到me的上一轮位置
    def FindMeInMapMatrixLast(self):
        return self.FindValuePosition("me",self.MapMatrixLast)

    #找到bot的当前位置
    def FindBotInMapMatrix(self):
        return self.FindValuePosition("bot",self.MapMatrix)

    #找到bot的上一轮位置
    def FindBotInMapMatrixLast(self):
        return self.FindValuePosition("bot",self.MapMatrixLast)

    #找到数值为obj在matrix中的位置
    def FindValuePosition(self,obj,matrix):
        RowMax = self.RowMax
        ColumnMax = self.ColumnMax
        for i in range(0,RowMax):
            for j in range(0,ColumnMax):
                if matrix[i][j]==obj:
                    return (i,j)
        return (-1,-1)

    #计算格子得分
    def CalGridScore(self):
        score1 = 0
        score2 = 0
        RowMax = self.RowMax
        ColumnMax = self.ColumnMax
        for i in range(0,RowMax):
            for j in range(0,ColumnMax):
                if self.GridStateMatrix[i][j]==1:
                    score1 += 1
                elif self.GridStateMatrix[i][j]==-1:
                    score2 += 1
        #计算金色格子
        (x,y)=self.GoldGradLocation
        if self.GridStateMatrix[x][y]==1:
            score1 += self.GoldGradPoint-1
        elif self.GridStateMatrix[x][y]==-1:
            score2 += self.GoldGradPoint-1
        return (score1,score2)

    #得到某位置上一轮的状态
    def GetValueInMapMatrixLast(self,p):
        (x,y) = p
        return self.MapMatrixLast[x][y]
        

    def debugPrint(self):
        print("\tRound",self.RoundCurrent)

    def debugPrintMapMatrix(self,pre=""):
        self.debugPrintMatrix(pre,self.MapMatrix)

    def debugPrintMapMatrixLast(self,pre=""):
        self.debugPrintMatrix(pre,self.MapMatrixLast)

    def debugPrintGridStateMatrix(self,pre=""):
        self.debugPrintMatrix(pre,self.GridStateMatrix)

    def debugPrintMatrix(self,pre,matrix):
        RowMax = self.RowMax
        ColumnMax = self.ColumnMax
        for i in range(0,RowMax):
            temp=""
            for j in range(0,ColumnMax):
                temp += str(matrix[i][j]) + "\t"
            print(pre+temp)

class OPTIMALPATH:
    ColumnMax=0    #列数目
    RowMax=0       #行数目 
    mapMatrix=[]   #地图矩阵
    pathMatrix=[]  #结果保存矩阵
    SPD=0          #加速状态

    #mapMatrix： 地图矩阵，障碍点为“wall”
    #Dimention：地图的维度（RowMax，ColumnMax）
    #startP：起点坐标（x，y）
    #startR：其实的方向
    def OP_Diffusion2(self,mapMatrix,Dimention,startP,startR,SPD=0):
        self.mapMatrix=mapMatrix
        ColumnMax=Dimention[1]  #列数目
        RowMax=Dimention[0] #行数目        
        self.ColumnMax = ColumnMax
        self.RowMax = RowMax
        
        self.pathMatrix= [[[-1,[-1,-1,-1,-1],[[] for i in range(4)]] for i in range(ColumnMax)] for i in range(RowMax)]   #结果保存矩阵
        #self.pathMatrix= [[[-1,[-1,-1,-1,-1],[[],[],[],[]]] for i in range(ColumnMax)] for i in range(RowMax)]   #结果保存矩阵
        x=startP[0]
        y=startP[1]
        lastPSet=[]     #上一轮扩散得到的点
        lastRSet=[]     #上一轮扩散得到新方向的点

        #起始点初始化
        roundI = 0  #扩散轮数为0
        self.pathMatrix[x][y][0] = roundI     #距离为0
        self.pathMatrix[x][y][1][startR] = roundI #调整到该方向的轮数为0
        self.pathMatrix[x][y][2][startR].append(startP)    #清空路径
        lastPSet.append(startP)
        lastRSet=[]
        #self.debugPrintPathMatrix(roundI)
        for roundI in range(1,ColumnMax*RowMax):           
            curPSet=[]     #本轮扩散得到的点
            curRSet=[]     #本轮扩散得到新方向的点
            
            #点扩散
            for p in lastPSet:
                #找到该位置的方向
                temp = self.pathMatrix[p[0]][p[1]][0]
                if (temp!=roundI-1):
                    print("error!")
                tpr = self.tGetRotation(self.pathMatrix[p[0]][p[1]][1],roundI-1)
                ##前向扩散
                for ri in tpr:
                    newp = self.fGoOneStep(p,ri,roundI,0)
                    if newp==None:
                        pass
                    else:    #可以扩散
                        self.fAddNewPos(p,ri,newp,ri,roundI)
                        if newp not in curPSet:
                            curPSet.append(newp)
                
                ##后向扩散
                for ri in tpr:
                    newp = self.fGoOneStep(p,ri,roundI,1)
                    if newp==None:
                        pass
                    else:    #可以扩散
                        self.fAddNewPos(p,ri,newp,ri,roundI)
                        if newp not in curPSet:
                            curPSet.append(newp)

                ##前进2步扩散
                if SPD==1:
                    for ri in tpr:
                        newp = self.fGoOneStep(p,ri,roundI,2)
                        if newp==None:
                            pass
                        else:    #可以扩散
                            self.fAddNewPos(p,ri,newp,ri,roundI)
                            if newp not in curPSet:
                                curPSet.append(newp)
                
                ##后向2步扩散
                if SPD==1:
                    for ri in tpr:
                        newp = self.fGoOneStep(p,ri,roundI,3)
                        if newp==None:
                            pass
                        else:    #可以扩散
                            self.fAddNewPos(p,ri,newp,ri,roundI)
                            if newp not in curPSet:
                                curPSet.append(newp)
                                                                                             
                ##角度扩散
                trnumber = len(tpr)
                if trnumber==1: #只有一个方向，则扩散出两个新方向
                    if p not in curRSet:
                        curRSet.append(p)
                    newr = (tpr[0]+1)%4
                    self.pathMatrix[p[0]][p[1]][1][newr] = roundI #更新距离
                    for path_p in self.pathMatrix[p[0]][p[1]][2][tpr[0]]: #更新路径
                        self.pathMatrix[p[0]][p[1]][2][newr].append(path_p)
                    self.pathMatrix[p[0]][p[1]][2][newr].append(p)
                    newr = (tpr[0]-1)%4
                    self.pathMatrix[p[0]][p[1]][1][newr] = roundI
                    for path_p in self.pathMatrix[p[0]][p[1]][2][tpr[0]]: #更新路径
                        self.pathMatrix[p[0]][p[1]][2][newr].append(path_p)
                    self.pathMatrix[p[0]][p[1]][2][newr].append(p)
                elif trnumber==2: #有两个方向
                    if abs(tpr[0]-tpr[1]) == 2: #两个方向是相对的，则再扩散出两个新方向
                        if p not in curRSet:
                            curRSet.append(p)
                        newr = (tpr[0]+1)%4
                        self.pathMatrix[p[0]][p[1]][1][newr] = roundI
                        for path_p in self.pathMatrix[p[0]][p[1]][2][tpr[0]]: #更新路径
                            self.pathMatrix[p[0]][p[1]][2][newr].append(path_p)
                        self.pathMatrix[p[0]][p[1]][2][newr].append(p)
                        newr = (tpr[0]-1)%4
                        self.pathMatrix[p[0]][p[1]][1][newr] = roundI
                        for path_p in self.pathMatrix[p[0]][p[1]][2][tpr[0]]: #更新路径
                            self.pathMatrix[p[0]][p[1]][2][newr].append(path_p)
                        self.pathMatrix[p[0]][p[1]][2][newr].append(p)
            
            #方向扩散                        
            for p in lastRSet:
                #找到该位置的方向
                temp = self.pathMatrix[p[0]][p[1]][0]
                if (temp!=roundI-2):
                    print("error!")
                tpr = self.tGetRotation(self.pathMatrix[p[0]][p[1]][1],roundI-1)
                ##前向扩散
                for ri in tpr:
                    newp = self.fGoOneStep(p,ri,roundI,0)
                    if newp==None:
                        pass
                    else:    #可以扩散
                        self.fAddNewPos(p,ri,newp,ri,roundI)
                        if newp not in curPSet:
                            curPSet.append(newp)
                
                ##后向扩散
                for ri in tpr:
                    newp = self.fGoOneStep(p,ri,roundI,1)
                    if newp==None:
                        pass
                    else:    #可以扩散
                        self.fAddNewPos(p,ri,newp,ri,roundI)
                        if newp not in curPSet:
                            curPSet.append(newp)
                
                ##前向2步扩散
                if SPD==1:
                    for ri in tpr:
                        newp = self.fGoOneStep(p,ri,roundI,2)
                        if newp==None:
                            pass
                        else:    #可以扩散
                            self.fAddNewPos(p,ri,newp,ri,roundI)
                            if newp not in curPSet:
                                curPSet.append(newp)

                ##后向2步扩散
                if SPD==1:
                    for ri in tpr:
                        newp = self.fGoOneStep(p,ri,roundI,3)
                        if newp==None:
                            pass
                        else:    #可以扩散
                            self.fAddNewPos(p,ri,newp,ri,roundI)
                            if newp not in curPSet:
                                curPSet.append(newp)


            #更新状态
            lastPSet = curPSet
            lastRSet = curRSet
            #self.debugPrintPathMatrix(roundI)
            if len(lastPSet)==0 and len(lastRSet)==0:
                break;

        #print(self.pathMatrix[9][9][2][0])
        return
    
    #mapMatrix： 地图矩阵，障碍点为“wall”
    #Dimention：地图的维度（RowMax，ColumnMax）
    #startP：起点坐标（x，y）
    #startR：其实的方向
    def OP_Diffusion(self,mapMatrix,Dimention,startP,startR):
        self.mapMatrix=mapMatrix
        ColumnMax=Dimention[1]  #列数目
        RowMax=Dimention[0] #行数目        
        self.ColumnMax = ColumnMax
        self.RowMax = RowMax
        
        self.pathMatrix= [[[-1,[-1,-1,-1,-1],[[] for i in range(4)]] for i in range(ColumnMax)] for i in range(RowMax)]   #结果保存矩阵
        #self.pathMatrix= [[[-1,[-1,-1,-1,-1],[[],[],[],[]]] for i in range(ColumnMax)] for i in range(RowMax)]   #结果保存矩阵
        x=startP[0]
        y=startP[1]
        lastPSet=[]     #上一轮扩散得到的点
        lastRSet=[]     #上一轮扩散得到新方向的点

        #起始点初始化
        roundI = 0  #扩散轮数为0
        self.pathMatrix[x][y][0] = roundI     #距离为0
        self.pathMatrix[x][y][1][startR] = roundI #调整到该方向的轮数为0
        self.pathMatrix[x][y][2][startR].append(startP)    #清空路径
        lastPSet.append(startP)
        lastRSet=[]
        #self.debugPrintPathMatrix(roundI)
        for roundI in range(1,ColumnMax*RowMax):           
            curPSet=[]     #本轮扩散得到的点
            curRSet=[]     #本轮扩散得到新方向的点
            
            #点扩散
            for p in lastPSet:
                #找到该位置的方向
                temp = self.pathMatrix[p[0]][p[1]][0]
                if (temp!=roundI-1):
                    print("error!")
                tpr = self.tGetRotation(self.pathMatrix[p[0]][p[1]][1],roundI-1)
                ##前向扩散
                for ri in tpr:
                    newp = self.fGoOneStep(p,ri,roundI,0)
                    if newp==None:
                        pass
                    else:    #可以扩散
                        self.fAddNewPos(p,ri,newp,ri,roundI)
                        if newp not in curPSet:
                            curPSet.append(newp)
                
                ##后向扩散
                for ri in tpr:
                    newp = self.fGoOneStep(p,ri,roundI,1)
                    if newp==None:
                        pass
                    else:    #可以扩散
                        self.fAddNewPos(p,ri,newp,ri,roundI)
                        if newp not in curPSet:
                            curPSet.append(newp)
                            
                #self.debugPrintPathMatrix(roundI)
                
                ##角度扩散
                trnumber = len(tpr)
                if trnumber==1: #只有一个方向，则扩散出两个新方向
                    if p not in curRSet:
                        curRSet.append(p)
                    newr = (tpr[0]+1)%4
                    self.pathMatrix[p[0]][p[1]][1][newr] = roundI #更新距离
                    for path_p in self.pathMatrix[p[0]][p[1]][2][tpr[0]]: #更新路径
                        self.pathMatrix[p[0]][p[1]][2][newr].append(path_p)
                    self.pathMatrix[p[0]][p[1]][2][newr].append(p)
                    newr = (tpr[0]-1)%4
                    self.pathMatrix[p[0]][p[1]][1][newr] = roundI
                    for path_p in self.pathMatrix[p[0]][p[1]][2][tpr[0]]: #更新路径
                        self.pathMatrix[p[0]][p[1]][2][newr].append(path_p)
                    self.pathMatrix[p[0]][p[1]][2][newr].append(p)
                elif trnumber==2: #有两个方向
                    if abs(tpr[0]-tpr[1]) == 2: #两个方向是相对的，则再扩散出两个新方向
                        if p not in curRSet:
                            curRSet.append(p)
                        newr = (tpr[0]+1)%4
                        self.pathMatrix[p[0]][p[1]][1][newr] = roundI
                        for path_p in self.pathMatrix[p[0]][p[1]][2][tpr[0]]: #更新路径
                            self.pathMatrix[p[0]][p[1]][2][newr].append(path_p)
                        self.pathMatrix[p[0]][p[1]][2][newr].append(p)
                        newr = (tpr[0]-1)%4
                        self.pathMatrix[p[0]][p[1]][1][newr] = roundI
                        for path_p in self.pathMatrix[p[0]][p[1]][2][tpr[0]]: #更新路径
                            self.pathMatrix[p[0]][p[1]][2][newr].append(path_p)
                        self.pathMatrix[p[0]][p[1]][2][newr].append(p)
            
            #方向扩散                        
            for p in lastRSet:
                #找到该位置的方向
                temp = self.pathMatrix[p[0]][p[1]][0]
                if (temp!=roundI-2):
                    print("error!")
                tpr = self.tGetRotation(self.pathMatrix[p[0]][p[1]][1],roundI-1)
                ##前向扩散
                for ri in tpr:
                    newp = self.fGoOneStep(p,ri,roundI,0)
                    if newp==None:
                        pass
                    else:    #可以扩散
                        self.fAddNewPos(p,ri,newp,ri,roundI)
                        if newp not in curPSet:
                            curPSet.append(newp)
                
                ##后向扩散
                for ri in tpr:
                    newp = self.fGoOneStep(p,ri,roundI,1)
                    if newp==None:
                        pass
                    else:    #可以扩散
                        self.fAddNewPos(p,ri,newp,ri,roundI)
                        if newp not in curPSet:
                            curPSet.append(newp)

            #更新状态
            lastPSet = curPSet
            lastRSet = curRSet
            #self.debugPrintPathMatrix(roundI)
            if len(lastPSet)==0 and len(lastRSet)==0:
                break;

        #print(self.pathMatrix[9][9][2][0])
        return

    #路径上加入一个新位置
    def fAddNewPos(self,oldp,oldr,newp,newr,roundI):
        #更新节点的距离
        temp=self.pathMatrix[newp[0]][newp[1]][0]
        if temp == -1:
            self.pathMatrix[newp[0]][newp[1]][0] = roundI
        elif temp == roundI-1:
            pass
        elif temp == roundI:
            pass
        else:
            print("error!")
        #更新方向的距离
        temp=self.pathMatrix[newp[0]][newp[1]][1][newr]
        if temp == -1:
            self.pathMatrix[newp[0]][newp[1]][1][newr] = roundI
            #更新路径信息            
            path = self.pathMatrix[oldp[0]][oldp[1]][2][newr]
            #path1 = self.pathMatrix[newp[0]][newp[1]][2][newr]
            for path_p in path:
                self.pathMatrix[newp[0]][newp[1]][2][newr].append(path_p)
            self.pathMatrix[newp[0]][newp[1]][2][newr].append(newp)
        return
    
    #向前前进一个点
    def fGoForth(self,p,r,roundI):
        action = 0  #goForth
        return self.fGoOneStep(p,r,roundI,action)

    #完成一个移动动作
    def fGoOneStep(self,p,r,roundI,action):
        newp = self.tGetGoOneStepP(p,r,action)
        #是否出界
        if newp[0]<0 or newp[0]>=self.RowMax or  newp[1]<0 or newp[1]>=self.ColumnMax:
            return None
        #当前点是否是墙
        tvalue = self.mapMatrix[newp[0]][newp[1]]
        if tvalue == "wall":
            return None
        #走两步的额外判断
        if action==2 or action==3:
            midp=((int)((p[0]+newp[0])/2),(int)((p[1]+newp[1])/2))            
            if midp[0]<0 or midp[0]>=self.RowMax or  midp[1]<0 or midp[1]>=self.ColumnMax:
                return None
            tvalue = self.mapMatrix[midp[0]][midp[1]]
            if tvalue == "wall":
                return None
        #当前点是否已经被扩散到了
        tvalue = self.pathMatrix[newp[0]][newp[1]][0]
        if tvalue < roundI and tvalue>=0: #本轮前被扩散到
            return None
        elif tvalue == roundI: #本轮被扩散到
            #self.pathMatrix[newp[0]][newp[1]][1][r] = roundI #仅更新该节点的方向
            if self.pathMatrix[newp[0]][newp[1]][1][r]==-1:#该方向还没有被扩散到
                return newp
        elif tvalue == -1:  #还未被扩散到
            #self.pathMatrix[newp[0]][newp[1]][0] = roundI #更新该节点的距离
            #self.pathMatrix[newp[0]][newp[1]][1][r] = roundI #更新该节点的方向
            return newp

    #工具小程序
    #返回动作后的下一个点
    def tGetGoOneStepP(self,p,r,action):
        if action == 0: #goForth       
            if r == 0:
                result = (p[0]-1,p[1])
            elif r == 1:
                result = (p[0],p[1]+1)
            elif r == 2:
                result = (p[0]+1,p[1])
            elif r == 3:
                result = (p[0],p[1]-1)
        elif action == 1: #goBack  
            if r == 0:
                result = (p[0]+1,p[1])
            elif r == 1:
                result = (p[0],p[1]-1)
            elif r == 2:
                result = (p[0]-1,p[1])
            elif r == 3:
                result = (p[0],p[1]+1)
        elif action == 2: #goForth2  
            if r == 0:
                result = (p[0]-2,p[1])
            elif r == 1:
                result = (p[0],p[1]+2)
            elif r == 2:
                result = (p[0]+2,p[1])
            elif r == 3:
                result = (p[0],p[1]-2)
        elif action == 3: #goBack2
            if r == 0:
                result = (p[0]+2,p[1])
            elif r == 1:
                result = (p[0],p[1]-2)
            elif r == 2:
                result = (p[0]-2,p[1])
            elif r == 3:
                result = (p[0],p[1]+2)
        elif action == 4: #turnLeft
            result = p
        elif action == 5: #turnRight
            result = p
        return result
        
    #工具小程序
    #返回Rs中有几个方向的距离为Value
    def tGetRotation(self,Rs,Value):
        result = []
        for i in range(0,4):
            if Rs[i]==Value:
                result.append(i)
        return result
            
    #输出结果
    def debugPrintPathMatrix(self,roundI=-1,pre=""):
        print(pre+"Round "+str(roundI))
        RowMax = self.RowMax
        ColumnMax = self.ColumnMax
        for i in range(0,RowMax):
            temp=str(i)+":\t"
            for j in range(0,ColumnMax):
                tt = str(self.pathMatrix[i][j][0])+ "[" 
                temp += tt
                if self.pathMatrix[i][j][1][0]==-1:
                       tt = " ,"
                else:
                       tt = str(self.pathMatrix[i][j][1][0]) + ","
                temp += tt
                if self.pathMatrix[i][j][1][1]==-1:
                       tt = " ,"
                else:
                       tt = str(self.pathMatrix[i][j][1][1]) + ","
                temp += tt
                if self.pathMatrix[i][j][1][2]==-1:
                       tt = " ,"
                else:
                       tt = str(self.pathMatrix[i][j][1][2]) + ","
                temp += tt
                if self.pathMatrix[i][j][1][3]==-1:
                       tt = " ,"
                else:
                       tt = str(self.pathMatrix[i][j][1][3])
                temp += tt + "]\t"
            print(pre+temp)

#战局分析与决策
class STRATEGY:
    def __init__(self,StateMe,StateBot,robot):
        self.StateMe = StateMe     #我方状态
        self.StateBot = StateBot   #敌方状态
        self.PathBot = []       #敌方的路径
        self.PathNearHP = []    #最近的HP
        self.PathNearSPD = []   #最近的SPD
        self.PathNearATK = []   #最近的ATK
        self.PathNearClear = [] #最近的clear
        self.PathNearGGrid = [] #最近的金色格子
        self.PossDangerous = [] #最可能被bot攻击的位置
        self.PossNextDangerous = [] #下一步可能会被bot攻击的位置
        self.PossAttack = []    #最佳攻击位置
        self.robot = robot
        self.FlagAction = False

    def fclear(self):
        self.PathBot = []       #敌方的路径
        self.PathNearHP = []    #最近的HP
        self.PathNearSPD = []   #最近的SPD
        self.PathNearATK = []   #最近的ATK
        self.PathNearClear = [] #最近的clear
        self.PathNearGGrid = [] #最近的金色格子
        self.PossDangerous = [] #最可能被bot攻击的位置
        self.PossAttack = []    #最佳攻击位置
        self.PossNextDangerous = [] #下一步可能会被bot攻击的位置
        
    #更新用于战局决策的状态
    def updateStrState(self,PosKeyThing,OptPath):
        self.fclear()
        #敌方的路径
        p = PosKeyThing.PosBot
        path = self.fGetBestPath(p,OptPath)
        for p in path: #self.fUpdateBestPath(self.PathBot,path)
            self.PathBot.append(p)            
        #最近的HP
        Ps = PosKeyThing.LPosHP
        path = self.fObtainNeastedPath(Ps,OptPath)
        for p in path: ##########self.fUpdateBestPath(self.PathNearHP,path)
            self.PathNearHP.append(p)            
        #最近的SPD
        Ps = PosKeyThing.LPosSPD
        path = self.fObtainNeastedPath(Ps,OptPath)
        for p in path: #self.fUpdateBestPath(self.PathNearSPD,path)
            self.PathNearSPD.append(p)
        #最近的ATK
        Ps = PosKeyThing.LPosATK
        path = self.fObtainNeastedPath(Ps,OptPath)
        for p in path: #self.fUpdateBestPath(self.PathNearATK,path)
            self.PathNearATK.append(p)
        #最近的clear
        Ps = PosKeyThing.LPosGridNotMe
        path = self.fObtainNeastedPath(Ps,OptPath)
        for p in path: #self.fUpdateBestPath(self.PathNearClear,path)
            self.PathNearClear.append(p)
        #最近的金色格子
        Ps = PosKeyThing.LPosGoldGrid
        path = self.fObtainNeastedPath(Ps,OptPath)
        for p in path: #self.fUpdateBestPath(self.PathNearGGrid,path)
            self.PathNearGGrid.append(p)
        #最可能被bot攻击的位置和最佳攻击位置
        self.fGetBotNextPos(PosKeyThing)
        return

    #做逃跑动作，优先逃跑
    def fGoAway(self,PosKeyThing,SPD=0):
        p = self.StateMe.p
        r = self.StateMe.r
        #前进2步
        if SPD==1:
            (p1,r1)=self.fCalNextPos(p,r,0)#前进一步
            if self.fJedgePos(PosKeyThing,p1):
                (p1,r1)=self.fCalNextPos(p1,r1,0)#再前进一步
                if self.fJedgePos(PosKeyThing,p1):
                    self.FlagAction = True
                    self.robot.goForth2()  
                    return self.FlagAction
        #后退2步
        if SPD==1:
            (p1,r1)=self.fCalNextPos(p,r,1)#后退一步
            if self.fJedgePos(PosKeyThing,p1):
                (p1,r1)=self.fCalNextPos(p1,r1,1)#再后退一步
                if self.fJedgePos(PosKeyThing,p1):
                    self.FlagAction = True
                    self.robot.goBack2()  
                    return self.FlagAction
        #前进1步
        (p1,r1)=self.fCalNextPos(p,r,0)#前进一步
        if self.fJedgePos(PosKeyThing,p1):
            self.FlagAction = True
            self.robot.goForth()  
            return self.FlagAction
        #后退1步
        (p1,r1)=self.fCalNextPos(p,r,1)#后退一步
        if self.fJedgePos(PosKeyThing,p1):
            self.FlagAction = True
            self.robot.goBack()  
            return self.FlagAction
        return False
                
    #做出决策
    def MakeDecision(self,robot,PosKeyThing):
        #进攻决策
        if robot.lookInFront() == "bot":
            #如果血量太小，逃跑
            HPme = self.StateMe.HP
            HPbot = self.StateBot.HP
            if HPme<HPbot-10:  #逃跑
                if self.fGoAway(PosKeyThing,self.StateMe.SPD):    #逃跑成功
                    return self.FlagAction
            #否则，进攻
            robot.attack()
            self.FlagAction = True
            return self.FlagAction

        #如果处于被攻击位置
        p = self.StateMe.p
        r = self.StateMe.r
        pvot = self.StateBot.p
        if (len(self.PossDangerous)!=0) and (p==self.PossDangerous[0]): #当前位置被攻击
            #如果血量太小，逃跑
            HPme = self.StateMe.HP
            HPbot = self.StateBot.HP
            if HPme<HPbot-10:  #逃跑
                if self.fGoAway(PosKeyThing,self.StateMe.SPD):    #逃跑成功
                    return self.FlagAction
            #处于左面
            (p1,r1)=self.fCalNextPos(p,r,2)
            (p2,r2)=self.fCalNextPos(p1,r1,0)
            if p2==pvot: #需要左转  
                self.FlagAction = self.fTurnLeft()
                if self.FlagAction:
                    return self.FlagAction                           
            #处于右边
            (p1,r1)=self.fCalNextPos(p,r,3)
            (p2,r2)=self.fCalNextPos(p1,r1,0)
            if p2==pvot: #需要右转  
                self.FlagAction = self.fTurnRight()
                if self.FlagAction:
                    return self.FlagAction 
            #处于后边
            (p1,r1)=self.fCalNextPos(p,r,3)
            (p1,r1)=self.fCalNextPos(p1,r1,3)
            (p2,r2)=self.fCalNextPos(p1,r1,0)
            if p2==pvot: #需要右转  
                self.FlagAction = self.fTurnRight()
                if self.FlagAction:
                    return self.FlagAction

        ##如果血量不够，逃跑
        #if (len(self.PathBot)<4 and (len(self.PathBot)>=3):
        #    
        
        #进入下一轮进攻位置
        thresholdP = 0.25
        if len(self.PathNearHP)==0:
            thresholdP = 0.25
        else:
            thresholdP = 1.1-0.1*len(self.PathNearHP)
            if thresholdP<0.25:
                thresholdP=0.25
        p = self.StateMe.p
        r = self.StateMe.r
        HPme = self.StateMe.HP
        HPbot = self.StateBot.HP
        ##是否已经处于下一轮攻击位置
        tempP = random.uniform(0,1)
        if (p,r) in self.PossAttack:
            if tempP>thresholdP: #如果概率被选中
                self.FlagAction = True
                self.robot.doNothing()
                return self.FlagAction        
        ##是否需要前进
        result=self.fCalNextPos(p,r,0)
        if result[0]==None:
            pass
        else:
            #if (result in self.PossAttack):
            if (result in self.PossAttack) and (result[0] not in self.PossNextDangerous or HPme>HPbot):
                if (len(self.PossDangerous)==0) or (result[0]!=self.PossDangerous[0]): #前进点不危险                    
                    if tempP>thresholdP: #如果概率被选中
                        self.FlagAction = self.fGoforth()
                        if self.FlagAction:
                            return self.FlagAction       
        ##是否需要前进2步
        result=self.fCalNextPos(p,r,0)
        if result[0]==None or self.StateMe.SPD == 0:
            pass
        elif self.fJedgePos(PosKeyThing,result[0]):
            result=self.fCalNextPos(result[0],r,0)            
            if result[0]==None:
                pass
            else:
                #if (result in self.PossAttack):
                if (result in self.PossAttack) and (result[0] not in self.PossNextDangerous or HPme>HPbot):
                    if (len(self.PossDangerous)==0) or (result[0]!=self.PossDangerous[0]): #前进点不危险                    
                        if tempP>thresholdP: #如果概率被选中
                            self.FlagAction = self.fGoforth(2)
                            if self.FlagAction:
                                return self.FlagAction 
        ##是否需要后退
        result=self.fCalNextPos(p,r,1)
        if result[0]==None:
            pass
        else:            
            #if (result in self.PossAttack):
            if (result in self.PossAttack) and (result[0] not in self.PossNextDangerous or HPme>HPbot):
                if (len(self.PossDangerous)==0) or (result[0]!=self.PossDangerous[0]): #前进点不危险                    
                    if tempP>thresholdP: #如果概率被选中                 
                        self.FlagAction = self.fGoBack()
                        if self.FlagAction:
                            return self.FlagAction       
        ##是否需要后退2步
        result=self.fCalNextPos(p,r,1)
        if result[0]==None or self.StateMe.SPD == 0:
            pass
        elif self.fJedgePos(PosKeyThing,result[0]):
            result=self.fCalNextPos(result[0],r,1)            
            if result[0]==None:
                pass
            else:
                #if (result in self.PossAttack):
                if (result in self.PossAttack) and (result[0] not in self.PossNextDangerous or HPme>HPbot):
                    if (len(self.PossDangerous)==0) or (result[0]!=self.PossDangerous[0]): #前进点不危险                    
                        if tempP>thresholdP: #如果概率被选中
                            self.FlagAction = self.fGoBack(2)
                            if self.FlagAction:
                                return self.FlagAction 
        ##是否需要左转
        result=self.fCalNextPos(p,r,2)
        if result[0]==None:
            pass
        else:
            #if (result in self.PossAttack):
            if (result in self.PossAttack) and (result[0] not in self.PossNextDangerous or HPme>HPbot):
                if (len(self.PossDangerous)==0) or (result[0]!=self.PossDangerous[0]): #前进点不危险                                        
                    if tempP>thresholdP: #如果概率被选中
                        self.FlagAction = self.fTurnLeft()
                        if self.FlagAction:
                            return self.FlagAction 
        ##是否需要右转
        result=self.fCalNextPos(p,r,3)
        if result[0]==None:
            pass
        else:
            #if (result in self.PossAttack):
            if (result in self.PossAttack) and (result[0] not in self.PossNextDangerous or HPme>HPbot):
                if (len(self.PossDangerous)==0) or (result[0]!=self.PossDangerous[0]): #前进点不危险                    
                    if tempP>thresholdP: #如果概率被选中
                        self.FlagAction = self.fTurnRight()
                        if self.FlagAction:
                            return self.FlagAction
                    
        #加血
        PathLength = len(self.PathNearHP)
        if PathLength !=0:
            if self.fChooseAction(robot,self.StateMe.p,self.StateMe.r,self.PathNearHP[1]):
                return self.FlagAction
        #加攻击
        PathLength = len(self.PathNearATK)
        if PathLength !=0:
            if self.fChooseAction(robot,self.StateMe.p,self.StateMe.r,self.PathNearATK[1]):
                return self.FlagAction
        #加速度
        if self.StateMe.SPD == 0:   #如果没有加速
            PathLength = len(self.PathNearSPD)
            if PathLength !=0:
                if self.fChooseAction(robot,self.StateMe.p,self.StateMe.r,self.PathNearSPD[1]):
                    return self.FlagAction
        #加格子
        PathLength = len(self.PathNearClear)
        if PathLength !=0 and PathLength<=8:
            if self.fChooseAction(robot,self.StateMe.p,self.StateMe.r,self.PathNearClear[1]):
                return self.FlagAction
            
        #随机决策
        random.choice([robot.turnLeft,robot.turnRight,robot.goForth,robot.goForth2])()
        return self.FlagAction

    def fGoforth(self,s=1):
        if s==1:
            self.FlagAction = True
            self.robot.goForth()  
            return self.FlagAction
        elif s==2:
            if self.StateMe.SPD!=1:
                self.FlagAction = False
            else:
                self.FlagAction = True
                self.robot.goForth2()  
            return self.FlagAction
    
    def fGoBack(self,s=1):
        if s==1:
            self.FlagAction = True
            self.robot.goBack()  
            return self.FlagAction
        elif s==2:
            if self.StateMe.SPD!=1:
                self.FlagAction = False
            else:
                self.FlagAction = True
                self.robot.goBack2()  
            return self.FlagAction
    
    def fTurnLeft(self):          
        self.FlagAction = True
        self.robot.turnLeft()    
        return self.FlagAction
    
    def fTurnRight(self):          
        self.FlagAction = True
        self.robot.turnRight()  
        return self.FlagAction

    

    def fChooseAction(self,robot,oldp,oldr,newp):
        if oldp == newp:
            if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                self.FlagAction = random.choice([self.fTurnLeft,self.fTurnRight])()
                #self.FlagAction = self.fTurnLeft()                
                if self.FlagAction:
                    return self.FlagAction 
            #random.choice([robot.turnLeft,robot.turnRight])()
        elif oldp[0]==newp[0]:
            if (oldp[1]+1==newp[1]) and oldr==1:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoforth()                
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goForth()
                #return True
            elif (oldp[1]+1==newp[1]) and oldr==3:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoBack()  
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goBack()
                #return True
            elif (oldp[1]==newp[1]+1) and oldr==1:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoBack() 
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goBack()
                #return True
            elif (oldp[1]==newp[1]+1) and oldr==3:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoforth() 
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False  
                #robot.goForth()
                #return True
            elif (oldp[1]+2==newp[1]) and oldr==1:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoforth(2)                
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goForth()
                #return True
            elif (oldp[1]+2==newp[1]) and oldr==3:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoBack(2)  
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goBack()
                #return True
            elif (oldp[1]==newp[1]+2) and oldr==1:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoBack(2) 
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goBack()
                #return True
            elif (oldp[1]==newp[1]+2) and oldr==3:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoforth(2) 
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False  
        elif oldp[1]==newp[1]:
            if (oldp[0]+1==newp[0]) and oldr==0:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoBack()   
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goBack()
                #return True
            elif (oldp[0]+1==newp[0]) and oldr==2:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoforth()
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goForth()
                #return True
            elif (oldp[0]==newp[0]+1) and oldr==0:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoforth()  
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goForth()
                #return True
            elif (oldp[0]==newp[0]+1) and oldr==2:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoBack()
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goBack()
                #return True
            elif (oldp[0]+2==newp[0]) and oldr==0:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoBack(2)   
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goBack()
                #return True
            elif (oldp[0]+2==newp[0]) and oldr==2:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoforth(2)
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goForth()
                #return True
            elif (oldp[0]==newp[0]+2) and oldr==0:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoforth(2)  
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
                #robot.goForth()
                #return True
            elif (oldp[0]==newp[0]+2) and oldr==2:
                if (len(self.PossDangerous)==0) or (newp!=self.PossDangerous[0]): #前进点不危险
                    self.FlagAction = self.fGoBack(2)
                    if self.FlagAction:
                        return self.FlagAction
                else:
                    return False
        print("point in fChooseAction 242")
        self.debugPrintStrState()
        return self.FlagAction

    #计算下一步的位置
    def fCalNextPos(self,p,r,action):
        newp = None
        newr =0
        if action==0: #前进
            newr=r
            if r==0:
                newp=(p[0]-1,p[1])
            elif r==1:
                newp=(p[0],p[1]+1)
            elif r==2:
                newp=(p[0]+1,p[1])
            elif r==3:
                newp=(p[0],p[1]-1)
        elif action==1: #后退
            newr=r
            if r==0:
                newp=(p[0]+1,p[1])
            elif r==1:
                newp=(p[0],p[1]-1)
            elif r==2:
                newp=(p[0]-1,p[1])
            elif r==3:
                newp=(p[0],p[1]+1)            
        elif action==2: #左转
            newp = p
            newr = (r-1)%4
        elif action==3: #右转
            newp = p
            newr = (r+1)%4
        return (newp,newr)

    #获得攻击的位置
    def fGetAttackPos(self,p,r):
        if r == 0:
            newp = ((p[0]-1,p[1]))
        elif r == 1:
            newp = ((p[0],p[1]+1))
        elif r == 2:
            newp = ((p[0]+1,p[1]))
        elif r == 3:
            newp = ((p[0],p[1]-1))
        return newp            
        
    #预测会被bot攻击的位置
    def fGetBotNextPos(self,PosKeyThing):
        Pbot = self.StateBot.p
        Rbot = self.StateBot.r
        #计算最危险的位置
        Pdangerous = []
        if Rbot == 0:
            Pdangerous.append((Pbot[0]-1,Pbot[1]))
        elif Rbot == 1:
            Pdangerous.append((Pbot[0],Pbot[1]+1))
        elif Rbot == 2:
            Pdangerous.append((Pbot[0]+1,Pbot[1]))
        elif Rbot == 3:
            Pdangerous.append((Pbot[0],Pbot[1]-1))
        for p in Pdangerous:
            if self.fJedgePos(PosKeyThing,p):
                self.PossDangerous.append(p)
        #下一步可能会被bot攻击的位置 self.PossNextDangerous = []
        PnextBotPRs = self.fGetNextPos(PosKeyThing,Pbot,Rbot,self.StateBot.SPD)
        for i in PnextBotPRs:
            attp = self.fGetAttackPos(i[0],i[1])
            if self.fJedgePos(PosKeyThing,attp):
                self.PossNextDangerous.append(attp)
        
        #计算攻击位置和方向
        PAttacks = []
        if Rbot == 0:
            #如果敌方不动，计算可以攻击敌人的位置
            PAttacks.append(((Pbot[0],Pbot[1]-1),1))  #左边   下一步的可能被攻击位置
            PAttacks.append(((Pbot[0],Pbot[1]+1),3))  #右边   下一步的可能被攻击位置
            PAttacks.append(((Pbot[0]+1,Pbot[1]),0))  #后边   下一步的可能最佳攻击位置
            #如果敌方前进，计算可以攻击敌人的位置
            (p1,r1) = self.fCalNextPos(Pbot,Rbot,0)  #如果下一步敌方前进
            if self.fJedgePos(PosKeyThing,p1):  #如果下一步敌方前进，并且该位置允许进入
                PAttacks.append(((Pbot[0]-2,Pbot[1]),2))  #大前边   下一步的可能被攻击位置
                PAttacks.append(((Pbot[0]-1,Pbot[1]-1),1))  #左前   下一步的可能最佳攻击位置
                PAttacks.append(((Pbot[0]-1,Pbot[1]+1),3))  #右前   下一步的可能最佳攻击位置
            #如果敌方后退，计算可以攻击敌人的位置
            (p1,r1) = self.fCalNextPos(Pbot,Rbot,1)  #如果下一步敌方后退
            if self.fJedgePos(PosKeyThing,p1):  #如果下一步敌方前进，并且该位置允许进入            
                PAttacks.append(((Pbot[0]+2,Pbot[1]),0))  #大后边   下一步的可能最佳攻击位置
                PAttacks.append(((Pbot[0]+1,Pbot[1]-1),1))  #左后   下一步的可能最佳攻击位置
                PAttacks.append(((Pbot[0]+1,Pbot[1]+1),3))  #右后   下一步的可能最佳攻击位置
        elif Rbot == 1:
            #如果敌方不动，计算可以攻击敌人的位置
            PAttacks.append(((Pbot[0],Pbot[1]-1),1))  #左边   下一步的可能最佳攻击位置
            PAttacks.append(((Pbot[0]+1,Pbot[1]),0))  #后边   下一步的可能被攻击位置
            PAttacks.append(((Pbot[0]-1,Pbot[1]),2))  #前边   下一步的可能被攻击位置
            #如果敌方前进，计算可以攻击敌人的位置
            (p1,r1) = self.fCalNextPos(Pbot,Rbot,0)  #如果下一步敌方前进
            if self.fJedgePos(PosKeyThing,p1):  #如果下一步敌方前进，并且该位置允许进入
                PAttacks.append(((Pbot[0],Pbot[1]+2),3))  #大右边   下一步的可能被攻击位置           
                PAttacks.append(((Pbot[0]-1,Pbot[1]+1),2))  #右前   下一步的可能最佳攻击位置
                PAttacks.append(((Pbot[0]+1,Pbot[1]+1),0))  #右后   下一步的可能最佳攻击位置
            #如果敌方后退，计算可以攻击敌人的位置
            (p1,r1) = self.fCalNextPos(Pbot,Rbot,1)  #如果下一步敌方后退
            if self.fJedgePos(PosKeyThing,p1):  #如果下一步敌方前进，并且该位置允许进入               
                PAttacks.append(((Pbot[0]-1,Pbot[1]-1),2))  #左前   下一步的可能最佳攻击位置            
                PAttacks.append(((Pbot[0],Pbot[1]-2),1))  #大左边   下一步的可能最佳攻击位置
                PAttacks.append(((Pbot[0]+1,Pbot[1]-1),0))  #左后   下一步的可能最佳攻击位置
        elif Rbot == 2:
            #如果敌方不动，计算可以攻击敌人的位置
            PAttacks.append(((Pbot[0],Pbot[1]-1),1))  #左边   下一步的可能被攻击位置
            PAttacks.append(((Pbot[0],Pbot[1]+1),3))  #右边   下一步的可能被攻击位置
            PAttacks.append(((Pbot[0]-1,Pbot[1]),2))  #前边   下一步的可能最佳攻击位置
            #如果敌方前进，计算可以攻击敌人的位置
            (p1,r1) = self.fCalNextPos(Pbot,Rbot,0)  #如果下一步敌方前进
            if self.fJedgePos(PosKeyThing,p1):  #如果下一步敌方前进，并且该位置允许进入
                PAttacks.append(((Pbot[0]+2,Pbot[1]),0))  #大后边   下一步的可能被攻击位置 
                PAttacks.append(((Pbot[0]+1,Pbot[1]-1),1))  #左后   下一步的可能最佳攻击位置
                PAttacks.append(((Pbot[0]+1,Pbot[1]+1),3))  #右后   下一步的可能最佳攻击位置
            #如果敌方后退，计算可以攻击敌人的位置
            (p1,r1) = self.fCalNextPos(Pbot,Rbot,1)  #如果下一步敌方后退
            if self.fJedgePos(PosKeyThing,p1):  #如果下一步敌方前进，并且该位置允许进入                                
                PAttacks.append(((Pbot[0]-2,Pbot[1]),2))  #大前边   下一步的可能最佳攻击位置          
                PAttacks.append(((Pbot[0]-1,Pbot[1]-1),1))  #左前   下一步的可能最佳攻击位置 
                PAttacks.append(((Pbot[0]-1,Pbot[1]+1),3))  #右前   下一步的可能最佳攻击位置
        elif Rbot == 3:
            #如果敌方不动，计算可以攻击敌人的位置
            PAttacks.append(((Pbot[0],Pbot[1]+1),3))  #右边   下一步的可能最佳攻击位置
            PAttacks.append(((Pbot[0]+1,Pbot[1]),0))  #后边   下一步的可能被攻击位置
            PAttacks.append(((Pbot[0]-1,Pbot[1]),2))  #前边   下一步的可能被攻击位置
            #如果敌方前进，计算可以攻击敌人的位置
            (p1,r1) = self.fCalNextPos(Pbot,Rbot,0)  #如果下一步敌方前进
            if self.fJedgePos(PosKeyThing,p1):  #如果下一步敌方前进，并且该位置允许进入            
                PAttacks.append(((Pbot[0],Pbot[1]-2),1))  #大左边   下一步的可能被攻击位置            
                PAttacks.append(((Pbot[0]-1,Pbot[1]-1),2))  #左前   下一步的可能最佳攻击位置
                PAttacks.append(((Pbot[0]+1,Pbot[1]-1),0))  #左后   下一步的可能最佳攻击位置
            #如果敌方后退，计算可以攻击敌人的位置
            (p1,r1) = self.fCalNextPos(Pbot,Rbot,1)  #如果下一步敌方后退
            if self.fJedgePos(PosKeyThing,p1):  #如果下一步敌方前进，并且该位置允许进入            
                PAttacks.append(((Pbot[0],Pbot[1]+2),3))  #大右边   下一步的可能最佳攻击位置
                PAttacks.append(((Pbot[0]-1,Pbot[1]+1),2))  #右前   下一步的可能最佳攻击位置
                PAttacks.append(((Pbot[0]+1,Pbot[1]+1),0))  #右后   下一步的可能最佳攻击位置
        for i in PAttacks:
            p = i[0]
            if self.fJedgePos(PosKeyThing,p):
                self.PossAttack.append(i)              
        return

    #计算下一步可能的位置
    def fGetNextPos(self,PosKeyThing,p,r,SPD=0):
        PRs = []
        #doNothing()
        newp=p
        newr=r
        PRs.append((newp,newr))
        #turnLeft()
        newr = (r-1)%4
        PRs.append((newp,newr))
        #turnRight()
        newr = (r+1)%4
        PRs.append((newp,newr))
        #goForth()
        if r==0:
            newp = (p[0]-1,p[1])
        elif r==1:
            newp = (p[0],p[1]+1)
        elif r==2:
            newp = (p[0]+1,p[1])
        elif r==3:
            newp = (p[0],p[1]-1)
        newr=r
        if self.fJedgePos(PosKeyThing,newp):
            PRs.append((newp,newr))
        #goBack()
        if r==0:
            newp = (p[0]+1,p[1])
        elif r==1:
            newp = (p[0],p[1]-1)
        elif r==2:
            newp = (p[0]-1,p[1])
        elif r==3:
            newp = (p[0],p[1]+1)
        newr=r
        if self.fJedgePos(PosKeyThing,newp):
            PRs.append((newp,newr))
        #goForth2()
        if SPD==1:            
            if r==0:
                newp = (p[0]-2,p[1])
            elif r==1:
                newp = (p[0],p[1]+2)
            elif r==2:
                newp = (p[0]+2,p[1])
            elif r==3:
                newp = (p[0],p[1]-2)
            newr=r
            if self.fJedgePos(PosKeyThing,newp):
                PRs.append((newp,newr))
        #goBack2()
        if SPD==1:            
            if r==0:
                newp = (p[0]+2,p[1])
            elif r==1:
                newp = (p[0],p[1]-2)
            elif r==2:
                newp = (p[0]-2,p[1])
            elif r==3:
                newp = (p[0],p[1]+2)
            newr=r
            if self.fJedgePos(PosKeyThing,newp):
                PRs.append((newp,newr))
        return PRs
    #判断该点是否出界
    def fJedgePos(self,PosKeyThing,p):
        result = False
        if p in PosKeyThing.LPosWall:
            return False
        elif p in PosKeyThing.LPosClear:
            return True
        elif p in PosKeyThing.LPosHP:
            return True
        elif p in PosKeyThing.LPosATK:
            return True
        elif p in PosKeyThing.LPosSPD:
            return True
        elif p == self.StateMe.p:
            return True
        elif p == self.StateBot.p:
            return False
        return result
        
    
    #获得给定点集合中的最短路径
    def fObtainNeastedPath(self,Ps,OptPath):
        bestP = -1
        bestD = 100000000
        for p in Ps:
            if OptPath[p[0]][p[1]][0] < bestD and OptPath[p[0]][p[1]][0]>=0:
                bestP = p
                bestD = OptPath[p[0]][p[1]][0]
        if bestP != -1:
            path = self.fGetBestPath(bestP,OptPath)
        else:
            path = []
        return path          

    
    #获得给定点的最短路径
    def fGetBestPath(self,p,OptPath):
        if p==-1:
            print("error in fGetBestPath")
            return
        AllPaths = OptPath[p[0]][p[1]][2]
        #找到方向
        r=-1
        d=1000000
        for i in range(0,4):
            if len(AllPaths[i])<d and len(AllPaths[i])>0:
                r = i
                d = len(AllPaths[i])
        #找到最优路径
        path = AllPaths[r]
        return path

    #更新最优路径
    def fUpdateBestPath(self,Spath,path):
        Spath = []
        for p in path:
            Spath.append(p)
        return
    #结果输出
    def debugPrintStrState(self,pre=""):
        print(pre+"STRATEGY state:")
        Ppre=pre+"\t"
        self.StateMe.debugPrintCurState(Ppre)
        self.StateBot.debugPrintCurState(Ppre)
        
        temp = "\tPath to Bot("+str(len(self.PathBot))+"):"
        for p in self.PathBot:
            temp+=str(p)
        print(pre+temp)        
        temp = "\tPath to HP("+str(len(self.PathNearHP))+"):"
        for p in self.PathNearHP:
            temp+=str(p)
        print(pre+temp)        
        temp = "\tPath to SPD("+str(len(self.PathNearSPD))+"):"
        for p in self.PathNearSPD:
            temp+=str(p)
        print(pre+temp)        
        temp = "\tPath to ATK("+str(len(self.PathNearATK))+"):"
        for p in self.PathNearATK:
            temp+=str(p)
        print(pre+temp)        
        temp = "\tPath to Clear("+str(len(self.PathNearClear))+"):"
        for p in self.PathNearClear:
            temp+=str(p)
        print(pre+temp)        
        temp = "\tPath to Golden Grid("+str(len(self.PathNearGGrid))+"):"
        for p in self.PathNearGGrid:
            temp+=str(p)
        print(pre+temp)        
        temp = "\tDangerous Position("+str(len(self.PossDangerous))+"):"
        for p in self.PossDangerous:
            temp+=str(p)
        print(pre+temp)
        temp = "\tNext Dangerous Position("+str(len(self.PossNextDangerous))+"):"
        for p in self.PossNextDangerous:
            temp+=str(p)
        print(pre+temp)
        temp = "\tAttack Position("+str(len(self.PossAttack))+"):"
        for p in self.PossAttack:
            temp+=str(p)
        print(pre+temp)

        return

            

class AI:
    def __init__(self):
        #Anything the AI needs to do before the game starts goes here.
        #自然状态相关参数
        self.StateParameters = STATEPARAMETER()
        self.StateMe = BOTPARAMETER()
        self.StateBot = BOTPARAMETER()
        #分析出局势
        self.OptPath = OPTIMALPATH()
        #决策模块
        self.StratMaking = None
        
    def turn(self):
        try:
            #更新当前的状态
            temp = self.StateParameters.RoundCurrent
            ########print("Round:"+str(temp))
            ##更新环境
            self.StateParameters.ObtainCurrentState(self.robot,temp)
            ########self.StateParameters.debugPrintMapMatrix()
            ########self.StateParameters.debugPrintGridStateMatrix()
            ########self.StateParameters.PosKeyThing.debugPrintStatePos()
            ##更新敌我状态
            self.UpdataStateMe()     #更新me的状态
            ########self.StateMe.debugPrintCurState()
            self.UpdataStateBot()   #更新bot的状态
            ########self.StateBot.debugPrintCurState()          

            #更新战局状态
            ##计算最有路径
            Dimention=(self.StateParameters.RowMax,self.StateParameters.ColumnMax)
            startP=self.StateMe.p
            startR=self.StateMe.r
            self.OptPath.OP_Diffusion2(self.StateParameters.MapMatrix,Dimention,startP,startR,self.StateMe.SPD)
            ########self.OptPath.debugPrintPathMatrix(self.StateParameters.RoundCurrent)
            ##为了做决策的战局状态分析
            self.StratMaking = STRATEGY(self.StateMe,self.StateBot,self.robot)
            self.StratMaking.updateStrState(self.StateParameters.PosKeyThing,self.OptPath.pathMatrix)
            ########self.StratMaking.debugPrintStrState()

            #做出决策
            self.StratMaking.MakeDecision(self.robot,self.StateParameters.PosKeyThing)
            
            #
            self.StateParameters.UpdateMapMatrixLast()
            
        except (RuntimeError,Exception):
            print("error in turn!")
            if self.robot.lookInFront() == "bot":
                self.robot.attack()
                return
            else:
                random.choice([self.robot.turnLeft,self.robot.turnRight,self.robot.goForth,self.robot.goForth2])()



        self.StateParameters.UpdataRoundCurrent()

    
    #更新me的状态
    def UpdataStateMe(self):
        self.StateMe.name = self.robot.name
        p = self.robot.position
        p=(p[1]-1,p[0]-1)
        self.StateMe.p = p
        self.StateMe.r = self.robot.rotation
        self.StateMe.HP = self.robot.health
        self.StateMe.ATK = self.robot.ATK
        self.StateMe.SPD = self.robot.speedUP
        (score1,score2) = self.StateParameters.CalGridScore()
        self.StateMe.GridScore = score1

    #更新bot的状态
    def UpdataStateBot(self):
        if self.StateMe.name == "red":
            self.StateBot.name = "blue"
        else:
            self.StateBot.name = "red"
        (score1,score2) = self.StateParameters.CalGridScore()
        self.StateBot.GridScore = score2
        if self.robot.detectEnemy()== None:
            (p, r) = self.robot.locateEnemy()
            p=(p[1]-1,p[0]-1)
            self.StateBot.p = p
            self.StateBot.r = r
            value = self.StateParameters.GetValueInMapMatrixLast(p)
            if value == "HP":
                self.StateBot.GainHP += 1
            elif value == "ATK":
                self.StateBot.GainATK +=1
            elif value == "SPD":                
                self.StateBot.SPD = 1
        else:
            (p, r, HP, ATK, SPD) = self.robot.detectEnemy()
            p=(p[1]-1,p[0]-1)
            self.StateBot.p = p
            self.StateBot.r = r
            self.StateBot.HP = HP
            self.StateBot.ATK =ATK
            self.StateBot.SPD = SPD
            self.StateBot.GainHP = 0
            self.StateBot.GainATK = 0
            

    def GetCurMapMatrix(self):
        RowMax = self.StateParameters.RowMax
        ColumnMax = self.StateParameters.ColumnMax
        for i in range(0,RowMax):
            for j in range(0,ColumnMax):
                self.StateParameters.MapMatrix[i][j] = self.robot.lookAtSpace((j+1,i+1))




#------------------------------
if __name__=="__main__":
    test=OPTIMALPATH()
    ColumnMax=10
    RowMax=10
    mapMatrix= [(["clear"] * ColumnMax) for i in range(RowMax)]
    mapMatrix[2][4] = "wall"
    mapMatrix[4][8] = "wall"
    mapMatrix[3][8] = "wall"
    mapMatrix[2][7] = "wall"
    test.OP_Diffusion2(mapMatrix,(RowMax,ColumnMax),(2,1),3,1)
    test.debugPrintPathMatrix()







































































