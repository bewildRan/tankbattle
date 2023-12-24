# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:14:44 2018

@author: 52784
"""

import random
        
class AI:
    
    def __init__(self):
        self.firstturn = True
        self.fang = None
    def turn(self):  
        # print(self.robot.locateEnemy())   # 返回坐标和方向((9, 5), 3)   用处不大
        self.attr = []      # 存取全局棋盘信息
        # 2层for循环将整个棋盘信息存到attr列表中
        for i in range(1, 11):
            for j in range(1, 11):
                self.attr.append(self.robot.lookAtSpace((j,i)))
                
        # for i in range(10):
        #     for j in range(10):
        #         print(self.attr[i*10+j], end=' ')
        #     print()
        #self.robot.doNothing()
        # 定位自己的位置 并转换成坐标
        self.my_pos_ori = self.attr.index('me')
        self.my_pos = (self.my_pos_ori//10+1, self.my_pos_ori%10+1)
        # 获取敌人位置
        self.enemy_pos_ori = self.attr.index('bot')
        self.enemy_pos = (self.enemy_pos_ori//10+1, self.enemy_pos_ori%10+1)

        # 根据初始位置判断自己的方向
        if self.firstturn:
            if self.my_pos_ori == 40:
                self.fang = 'right'
                self.firstturn = False
                print(self.fang)
            elif self.my_pos_ori == 49:
                self.fang = 'left'
                self.firstturn = False
                print(self.fang)
        
        self.ATK_pos = None
        self.ATK_pos_ori = None
        self.HP_pos = None
        self.HP_pos_ori = None
        self.ATK_flag = 0
        self.HP_flag = 0
        self.ATK_dist = 100
        self.HP_dist = 100
        
        # 寻找攻击和加血道具位置
        #self.ATK_pos_ori = [i for i, s in enumerate(self.attr) if s == "ATK"]
        #self.HP_pos_ori = [i for i, s in enumerate(self.attr) if s == "HP"]       
        try:
            self.ATK_pos_ori = self.attr.index('ATK')
            self.HP_pos_ori = self.attr.index('HP')
        except:
            pass

        # 将下标转换为坐标 并计算与我的折线距离
        if self.ATK_pos_ori != None:
            self.ATK_pos = (self.ATK_pos_ori//10+1, self.ATK_pos_ori%10+1)
            self.ATK_dist = abs(self.ATK_pos[0]-self.my_pos[0]) + abs(self.ATK_pos[1]-self.my_pos[1])
            #self.ATK_flag = 1
            
        if self.HP_pos_ori != None:
            self.HP_pos = (self.HP_pos_ori//10+1, self.HP_pos_ori%10+1)
            self.HP_dist = abs(self.HP_pos[0]-self.my_pos[0]) + abs(self.HP_pos[1]-self.my_pos[1])
            #self.HP_flag = 1
            
        # print(self.ATK_pos, self.HP_pos, self.ATK_dist, self.HP_dist)
            
        # 找到棋盘上离我最近的技能点
        if self.ATK_dist<100 or self.HP_dist<100:
            if self.ATK_dist < self.HP_dist:    # 如果攻击技能点离我近
                pass        #还没想到一个好的路径
                
                
        # 追着打功能
        # 以自己为中心建立坐标系 me(0,0)  右和上为正  定位敌人相对坐标
        self.enemy_rela_pos = (self.enemy_pos[1]-self.my_pos[1], self.my_pos[0]-self.enemy_pos[0])
        # print(self.enemy_rela_pos)
        
        if self.fang == 'right':
            if self.enemy_rela_pos[0] > 0:
                #if self.enemy_rela_pos[0] == 1 and self.enemy_rela_pos[1] == 0:
                if self.robot.lookInFront() == 'bot':
                    self.robot.attack()
                else:
                    if self.robot.lookInFront() == 'wall':
                        if self.enemy_rela_pos[1] >= 0:
                            self.fang = 'up'
                            self.robot.turnLeft()
                        else:
                            self.fang = 'down'
                            self.robot.turnRight()
                    else:
                        self.robot.goForth()
            else:
                if self.enemy_rela_pos[1] >= 0:
                    self.fang = 'up'
                    self.robot.turnLeft()
                elif self.enemy_rela_pos[1] < 0:
                    self.fang = 'down'
                    self.robot.turnRight()
        elif self.fang == 'left':
            if self.enemy_rela_pos[0] < 0:
                if self.robot.lookInFront() == 'bot':
                    self.robot.attack()
                else:
                    if self.robot.lookInFront() == 'wall':
                        if self.enemy_rela_pos[1] >= 0:
                            self.fang = 'up'
                            self.robot.turnRight()
                        else:
                            self.fang = 'down'
                            self.robot.turnLeft()
                    else:
                        self.robot.goForth()
            else:
                if self.enemy_rela_pos[1] >= 0:
                    self.fang = 'up'
                    self.robot.turnRight()
                elif self.enemy_rela_pos[1] < 0:
                    self.fang = 'down'
                    self.robot.turnLeft()
        elif self.fang == 'up':
            if self.enemy_rela_pos[1] > 0:
                if self.robot.lookInFront() == 'bot':
                    self.robot.attack()
                else:
                    if self.robot.lookInFront() == 'wall':
                        if self.enemy_rela_pos[0] >= 0:
                            self.fang = 'right'
                            self.robot.turnRight()
                        else:
                            self.fang = 'left'
                            self.robot.turnLeft()
                    else:
                        self.robot.goForth()
            else:
                if self.enemy_rela_pos[0] >= 0:
                    self.fang = 'right'
                    self.robot.turnRight()
                elif self.enemy_rela_pos[0] < 0:
                    self.fang = 'left'
                    self.robot.turnLeft()
        elif self.fang == 'down':
            if self.enemy_rela_pos[1] < 0:
                if self.robot.lookInFront() == 'bot':
                    self.robot.attack()
                else:
                    if self.robot.lookInFront() == 'wall':
                        if self.enemy_rela_pos[0] >= 0:
                            self.fang = 'right'
                            self.robot.turnLeft()
                        else:
                            self.fang = 'left'
                            self.robot.turnRight()
                    else:
                        self.robot.goForth()
            else:
                if self.enemy_rela_pos[0] >= 0:
                    self.fang = 'right'
                    self.robot.turnLeft()
                elif self.enemy_rela_pos[0] < 0:
                    self.fang = 'left'
                    self.robot.turnRight()
        else:
            self.robot.doNothing()
            
            
            
            
            
            
            
            
        
        #self.robot.doNothing()
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        if self.firstturn==True:
            self.robot.goForth()
            self.firstturn = False
            return
        elif self.robot.lookInFront() == "HP":
            self.robot.goForth()
            return
        elif self.robot.lookInFront() == "SPD":
            self.robot.goForth()
            return
        elif self.robot.lookInFront() == "ATK":
            self.robot.goForth()
            return
           
        elif self.robot.lookInFront() == "bot":
            self.robot.attack()
            return
        elif self.robot.lookInFront() == "wall":
            self.robot.turnLeft()
            return
        else:
            random.choice([self.robot.goForth,self.robot.turnLeft,self.robot.goForth])()
            return
            '''