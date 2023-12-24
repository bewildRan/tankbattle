import queue

class AI:
    def __init__(self):
        # Anything the AI needs to do before the game starts goes here.
        pass
    def newXY (self, x, y, r):#寻找前一格
        if r == 0:#朝上
            return (x, y-1)
        if r == 1:#朝右
            return (x+1, y)
        if r == 2:#朝下
            return (x, y+1)
        if r == 3:#朝左
            return (x-1, y)
    def backXY (self, x, y, r):#寻找前一格
        if r == 0:#朝上
            return (x, y+1)
        if r == 1:#朝右
            return (x-1, y)
        if r == 2:#朝下
            return (x, y-1)
        if r == 3:#朝左
            return (x+1, y)
    def bfs (self, x, y, r, f, u, v): # 广搜寻找最短路径
        q = queue.Queue() # 队列
        hash_table = [[[1000 for i in range(11)] for i in range(11)]for i in range(11)]

        q.put(int(x))#起点x
        q.put(int(y))#起点y
        q.put(int(r))#起点r
        q.put(int(0))#操作串
        q.put(int(0))#步骤数
        hash_table[x][y][r]=0#起点进入哈希表

        while not q.empty():#队列不为空时
            x = q.get()#节点的x
            y = q.get()#节点的y
            r = q.get()#节点的r
            l = q.get()#路径
            d = q.get()

            if self.robot.lookAtSpace((x,y))=='HP' or self.robot.lookAtSpace((x,y))=='ATK' or self.robot.lookAtSpace((x,y))=='SPD':#当前节点是特殊物品，返回路径
                return l

            #右转
            dx = x#目标x
            dy = y#目标y
            dr = r#目标r
            dl = l * 10 + 1#目标路径
            dd = d + 1

            if  dr == 3:#右转
                dr = 0
            else:
                dr += 1

            if hash_table[dx][dy][dr] > dd:  #目标状态可以更新
                hash_table[dx][dy][dr] = dd
                q.put(int(dx))
                q.put(int(dy))
                q.put(int(dr))
                q.put(int(dl))
                q.put(int(dd))
            #左转
            dx = x  #目标x
            dy = y  #目标y
            dr = r  #目标r
            dl = l * 10 +2
            dd = d + 1
            if  dr == 0:  #左转
                dr = 3
            else:
                dr -= 1

            if hash_table[dx][dy][dr] > dd:  #如果没去过
                hash_table[dx][dy][dr] = dd  #加入哈希表
                q.put(int(dx))
                q.put(int(dy))
                q.put(int(dr))
                q.put(int(dl))
                q.put(int(dd))
            #前进
            dxy = AI.newXY(self, x, y, r)  #前方坐标
            dx = dxy[0]  #目标坐标x
            dy = dxy[1]  #目标坐标y
            dr = r  #目标坐标r
            dl = l * 10 + 3
            dd = d + 1
            if not (dx==u and dy==v):
                if not (self.robot.lookAtSpace((dx, dy)) == 'wall' or self.robot.lookAtSpace((dx, dy)) == 'bot'):#前方不是墙或者对手
                    if hash_table[dx][dy][dr] > dd:#不在哈希表里
                        hash_table[dx][dy][dr] = dd#进哈希表
                        q.put(int(dx))
                        q.put(int(dy))
                        q.put(int(dr))
                        q.put(int(dl))
                        q.put(int(dd))

            #后退
            dxy = AI.backXY(self, x, y, r)  #后方坐标
            dx = dxy[0]  #目标坐标x
            dy = dxy[1]  #目标坐标y
            dr = r  #目标坐标r
            dl = l * 10 + 4
            dd = d + 1
            if not (dx == u and dy == v):
                if not (self.robot.lookAtSpace((dx, dy)) == 'wall' or self.robot.lookAtSpace((dx, dy)) == 'bot'):#前方不是墙或者对手
                    if hash_table[dx][dy][dr] > dd:#不在哈希表里
                        hash_table[dx][dy][dr] = dd#进哈希表
                        q.put(int(dx))
                        q.put(int(dy))
                        q.put(int(dr))
                        q.put(int(dl))
                        q.put(int(dd))


            if f :
                #前进2
                dxy = AI.newXY(self, x, y, r)  #前方坐标
                dx = dxy[0]  #目标坐标x
                dy = dxy[1]  #目标坐标y
                if not (dx == u and dy == v):
                    if x<=10 and x>=1 and y<=10 and y>=1:
                        if not (self.robot.lookAtSpace((dx, dy)) == 'wall' or self.robot.lookAtSpace((dx, dy)) == 'bot'):#前方不是墙或者对手
                            dxy = AI.newXY(self, dx, dy, r)
                            dx = dxy[0]
                            dy = dxy[1]
                            dr = r  #目标坐标r
                            dl = l * 10 + 5
                            dd = d + 1
                            if not (dx == u and dy == v):
                                if x<=10 and x>=1 and y<=10 and y>=1:
                                    if not (self.robot.lookAtSpace((dx, dy)) == 'wall' or self.robot.lookAtSpace((dx, dy)) == 'bot'):#前方不是墙或者对手
                                        if hash_table[dx][dy][dr] > dd:#不在哈希表里
                                            hash_table[dx][dy][dr] = dd#进哈希表
                                            q.put(int(dx))
                                            q.put(int(dy))
                                            q.put(int(dr))
                                            q.put(int(dl))
                                            q.put(int(dd))
                #后退2
                dxy = AI.backXY(self, x, y, r)  #前方坐标
                dx = dxy[0]  #目标坐标x
                dy = dxy[1]  #目标坐标y
                if not (dx == u and dy == v):
                    if x<=10 and x>=1 and y<=10 and y>=1:
                        if not (self.robot.lookAtSpace((dx, dy)) == 'wall' or self.robot.lookAtSpace((dx, dy)) == 'bot'):#前方不是墙或者对手
                            dxy = AI.backXY(self, dx, dy, r)
                            dx = dxy[0]
                            dy = dxy[1]
                            dr = r  #目标坐标r
                            dl = l * 10 + 6
                            dd = d + 1
                            if not (x == u and y == v):
                                if x<=10 and x>=1 and y<=10 and y>=1:
                                    if not (self.robot.lookAtSpace((dx, dy)) == 'wall' or self.robot.lookAtSpace((dx, dy)) == 'bot'):#前方不是墙或者对手
                                        if hash_table[dx][dy][dr] > dd:#不在哈希表里
                                            hash_table[dx][dy][dr] = dd#进哈希表
                                            q.put(int(dx))
                                            q.put(int(dy))
                                            q.put(int(dr))
                                            q.put(int(dl))
                                            q.put(int(dd))



        hash_table.clear()
        return 0#寻找路径失败
    def bfsto (self, x, y, r, f, ex, ey, u, v, w):
        q = queue.Queue()  # 队列
        hash_table = [[[1000 for i in range(11)] for i in range(11)] for i in range(11)]

        q.put(int(x))  # 起点x
        q.put(int(y))  # 起点y
        q.put(int(r))  # 起点r
        q.put(int(0))  # 操作串
        q.put(int(0))  # 步骤数
        hash_table[x][y][r] = 0  # 起点进入哈希表

        while not q.empty():  # 队列不为空时
            x = q.get()  # 节点的x
            y = q.get()  # 节点的y
            r = q.get()  # 节点的r
            l = q.get()  # 路径
            d = q.get()

            if x == u and y == v and (r == w or w == -1):
                return l

            # 右转
            dx = x  # 目标x
            dy = y  # 目标y
            dr = r  # 目标r
            dl = l * 10 + 1  # 目标路径
            dd = d + 1

            if dr == 3:  # 右转
                dr = 0
            else:
                dr += 1

            if hash_table[dx][dy][dr] > dd:  # 目标状态可以更新
                hash_table[dx][dy][dr] = dd
                q.put(int(dx))
                q.put(int(dy))
                q.put(int(dr))
                q.put(int(dl))
                q.put(int(dd))
            # 左转
            dx = x  # 目标x
            dy = y  # 目标y
            dr = r  # 目标r
            dl = l * 10 + 2
            dd = d + 1
            if dr == 0:  # 左转
                dr = 3
            else:
                dr -= 1

            if hash_table[dx][dy][dr] > dd:  # 如果没去过
                hash_table[dx][dy][dr] = dd  # 加入哈希表
                q.put(int(dx))
                q.put(int(dy))
                q.put(int(dr))
                q.put(int(dl))
                q.put(int(dd))
            # 前进
            dxy = AI.newXY(self, x, y, r)  # 前方坐标
            dx = dxy[0]  # 目标坐标x
            dy = dxy[1]  # 目标坐标y
            dr = r  # 目标坐标r
            dl = l * 10 + 3
            dd = d + 1
            if not (dx == ex and dy == ey):
                if not (self.robot.lookAtSpace((dx, dy)) == 'wall' or self.robot.lookAtSpace(
                        (dx, dy)) == 'bot'):  # 前方不是墙或者对手
                    if hash_table[dx][dy][dr] > dd:  # 不在哈希表里
                        hash_table[dx][dy][dr] = dd  # 进哈希表
                        q.put(int(dx))
                        q.put(int(dy))
                        q.put(int(dr))
                        q.put(int(dl))
                        q.put(int(dd))

            # 后退
            dxy = AI.backXY(self, x, y, r)  # 后方坐标
            dx = dxy[0]  # 目标坐标x
            dy = dxy[1]  # 目标坐标y
            dr = r  # 目标坐标r
            dl = l * 10 + 4
            dd = d + 1
            if not (dx == ex and dy == ey):
                if not (self.robot.lookAtSpace((dx, dy)) == 'wall' or self.robot.lookAtSpace(
                        (dx, dy)) == 'bot'):  # 前方不是墙或者对手
                    if hash_table[dx][dy][dr] > dd:  # 不在哈希表里
                        hash_table[dx][dy][dr] = dd  # 进哈希表
                        q.put(int(dx))
                        q.put(int(dy))
                        q.put(int(dr))
                        q.put(int(dl))
                        q.put(int(dd))

            if f:
                # 前进2
                dxy = AI.newXY(self, x, y, r)  # 前方坐标
                dx = dxy[0]  # 目标坐标x
                dy = dxy[1]  # 目标坐标y
                if not (dx == ex and dy == ey):
                    if x <= 10 and x >= 1 and y <= 10 and y >= 1:
                        if not (self.robot.lookAtSpace((dx, dy)) == 'wall' or self.robot.lookAtSpace((dx, dy)) == 'bot'):  # 前方不是墙或者对手
                            dxy = AI.newXY(self, dx, dy, r)
                            dx = dxy[0]
                            dy = dxy[1]
                            dr = r  # 目标坐标r
                            dl = l * 10 + 5
                            dd = d + 1
                            if not (dx == ex and dy == ey):
                                if x <= 10 and x >= 1 and y <= 10 and y >= 1:
                                    if not (self.robot.lookAtSpace((dx, dy)) == 'wall' or self.robot.lookAtSpace(
                                            (dx, dy)) == 'bot'):  # 前方不是墙或者对手
                                        if hash_table[dx][dy][dr] > dd:  # 不在哈希表里
                                            hash_table[dx][dy][dr] = dd  # 进哈希表
                                            q.put(int(dx))
                                            q.put(int(dy))
                                            q.put(int(dr))
                                            q.put(int(dl))
                                            q.put(int(dd))
                # 后退2
                dxy = AI.backXY(self, x, y, r)  # 前方坐标
                dx = dxy[0]  # 目标坐标x
                dy = dxy[1]  # 目标坐标y
                if not (dx == ex and dy == ey):
                    if x <= 10 and x >= 1 and y <= 10 and y >= 1:
                        if not (self.robot.lookAtSpace((dx, dy)) == 'wall' or self.robot.lookAtSpace(
                                (dx, dy)) == 'bot'):  # 前方不是墙或者对手
                            dxy = AI.backXY(self, dx, dy, r)
                            dx = dxy[0]
                            dy = dxy[1]
                            dr = r  # 目标坐标r
                            dl = l * 10 + 6
                            dd = d + 1
                            if not (x == ex and y == ey):
                                if x <= 10 and x >= 1 and y <= 10 and y >= 1:
                                    if not (self.robot.lookAtSpace((dx, dy)) == 'wall' or self.robot.lookAtSpace(
                                            (dx, dy)) == 'bot'):  # 前方不是墙或者对手
                                        if hash_table[dx][dy][dr] > dd:  # 不在哈希表里
                                            hash_table[dx][dy][dr] = dd  # 进哈希表
                                            q.put(int(dx))
                                            q.put(int(dy))
                                            q.put(int(dr))
                                            q.put(int(dl))
                                            q.put(int(dd))

        hash_table.clear()
        return 0  # 寻找路径失败
    def getMove (self, x):
        ans = 0
        while not x == 0:
            ans = x % 10
            x = x // 10
        return ans
    def turn (self):
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
            return
        else:
            x, y=self.robot.position#当前坐标x，y
            r=self.robot.rotation#当前r
            f=self.robot.speedUP

            (Enp,Enr)=self.robot.locateEnemy()
            Ex=Enp[0]
            Ey=Enp[1]
            Er=Enr
            Ef=AI.newXY(self,Ex,Ey,Er)
            Exf=Ef[0]
            Eyf=Ef[1]
            Eb=AI.backXY(self,Ex,Ey,Er)
            Exb=Eb[0]
            Eyb=Eb[1]


            ans=AI.bfs(self, x, y, r, f, Exf, Eyf)#寻找最短路

            if not ans == 0:#如果没有寻找路径失败
                move_code=AI.getMove(self,ans)#执行所有操作中的第一个
                if move_code == 1:#操作编号1
                    self.robot.turnRight()#右转
                elif move_code == 2:#操作编号2
                    self.robot.turnLeft()#左转
                elif move_code == 3:#操作编号3
                    self.robot.goForth()#直走
                elif move_code == 4:
                    self.robot.goBack()
                elif move_code == 5:
                    self.robot.goForth2()
                else:
                    self.robot.goBack2()
            else:
                #ans = AI.bfsto(self, x, y, r, f, Exf, Eyf, 5, 5, -1)  # 寻找最短路
                ans = AI.bfsto(self, x, y, r, f, Exf, Eyf, Exb, Eyb, Er)  # 寻找最短路
                if not ans == 0:  # 如果没有寻找路径失败
                    move_code = AI.getMove(self, ans)  # 执行所有操作中的第一个
                    if move_code == 1:  # 操作编号1
                        self.robot.turnRight()  # 右转
                    elif move_code == 2:  # 操作编号2
                        self.robot.turnLeft()  # 左转
                    elif move_code == 3:  # 操作编号3
                        self.robot.goForth()  # 直走
                    elif move_code == 4:
                        self.robot.goBack()
                    elif move_code == 5:
                        self.robot.goForth2()
                    else:
                        self.robot.goBack2()
                else:
                    self.robot.turnRight()  # 右转