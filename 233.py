import queue # 有点大炮打蚊子？
import os

"""
就是干 by lzy
"""


class AI:
	"""
	和另一个类似思路的AI对打了几盘
	胜负很大程度上取决于加速器离哪边比较近
	"""
	def __init__(self):
		self.space = []
		self.dir = 0
		self.speed_up = False
		self.escape_cnt = 0
	def validi(self, x, y):
		return (x>=1 and x <=10 and y>=1 and y<=10)
	def getp(self, x, y):
		"""
		约定 p 指[0, 99]来映射x, y
		x y默认[1, 10]
		需要明确x，y的定义
		"""
		return (y-1) * 10 + (x-1)
	def geti(self, p):
		return (p%10+1, p//10+1)
	def validp(self, p):
		x, y = self.geti(p)
		return self.validi(x, y)
	
	def print_field(self, l):
		for i in range(10):
			print(l[i*10:i*10+10])
		print()
	def get_nearby_list(self, x, y):
		"""
		返回一个点(x, y)上下左右的点的列表，第三个数字表示方向
		需要valid检查
		"""
		return [(x+1, y, 1), (x-1, y, 3), (x, y+1, 2), (x, y-1, 0)]

	def step(self, cx, cy):
		"""
		bfs求最短路，并且向那个方向走一步
		找不到最短路返回None
		"""
		q = queue.Queue()
		# print(cx, cy)
		x, y, dir = self.x, self.y, self.dir
		self.d = []
		d = self.d = [1000] * 100 # inf
		d[self.getp(cx, cy)] = 0
		q.put(self.getp(cx, cy))
		
		(ex, ey), edir = self.robot.locateEnemy()
		frontx, fronty = self.robot.calculateCoordinates(distance=1, direction=edir, position=(ex, ey)) # 对手面前的那一格，需要绕开，这里当墙处置
		
		while not q.empty():
			up = q.get() # 最短路的源节点
			ux, uy = self.geti(up)
			for vx, vy, vdir in self.get_nearby_list(ux, uy): # 遍历当前节点的出边
				if self.validi(vx, vy) and not self.robot.lookAtSpace((vx, vy)) in ("wall", "bot") and (vx != frontx or vy != fronty):
					# 如果是墙就不搜了
					vp = self.getp(vx, vy)
					if d[up]+1 < d[vp]:
						d[vp] = d[up]+1
						q.put(vp)
		

		# 上面这一段我是照着C++写的hhh
		# 之后追加的加速器处理，有点乱
		if self.robot.speedUP != 0:
			nearby_list_spd = [(x+2, y, 1, x+1, y), (x-2, y, 3, x-1, y), (x, y+2, 2, x, y+1), (x, y-2, 0, x, y-1)]
			for vx, vy, vdir, Tx, Ty in nearby_list_spd:
				vp = self.getp(vx, vy)
				p = self.getp(x, y)
				Tp = self.getp(Tx, Ty)
				if self.validi(vx, vy) and d[vp] < d[p] and self.space[Tp] != "wall" and self.space[Tp] != "bot":
					if dir == vdir:
						self.robot.goForth2()
						return 1
					if (dir+2) % 4 == vdir:
						self.robot.goBack2()
						return 1
					if (dir+1) % 4 == vdir:
						self.robot.turnRight()
						return 1
					if (dir+3) % 4 == vdir:
						self.robot.turnLeft()
						return 1

		for vx, vy, vdir in self.get_nearby_list(x, y):
			vp = self.getp(vx, vy)
			p = self.getp(x, y)
			if self.validi(vx, vy) and d[vp] < d[p]:
				# print(vx, vy)
				# self.print_field(d)
				# 往靠近目标的地方移动
				if dir == vdir:
					self.robot.goForth()
					return 1
				if (dir+2) % 4 == vdir:
					self.robot.goBack()
					return 1
				if (dir+1) % 4 == vdir:
					self.robot.turnRight()
					return 1
				if (dir+3) % 4 == vdir:
					self.robot.turnLeft()
					return 1
		return None

	def find_item(self, item_info):
		"""
		返回一个坐标tuple，找不到返回None
		"""
		for i in range(1, 11):
			for j in range(1, 11):
				if self.space[self.getp(i, j)] == item_info:
					return (i, j)
		return None

	def atk_enemy(self):
		

		if self.robot.lookInFront() == "bot":
			self.robot.attack()
			return 1
		(ex, ey), edir = self.robot.locateEnemy()
		tdir = (edir-2) % 4
		tx, ty = self.robot.calculateCoordinates(distance=1, direction=tdir, position=(ex, ey)) # 绕对手后
		if self.validi(ex, ey):
			if self.step(ex, ey):
				return 1
		return None


	def turn(self):
        
		self.health = self.robot.health
		self.atk = self.robot.ATK
		# 获取整个战场
		self.space = []
		for i in range(1, 11):
			for j in range(1, 11):
				self.space.append(self.robot.lookAtSpace((j, i)))

		self.dir = self.robot.rotation
		self.x, self.y = self.robot.position
		# 敌人在附近
		tmp = self.robot.detectEnemy()
		if tmp is None:
			pass
		else:
			# 判断能不能打过
			(ex, ey), er, ehp, eatk, espd = tmp
			# if ((self.robot.health // eatk) > (ehp // self.robot.ATK) + 1):
			if True:
				if self.atk_enemy() == 1:
					return
			# 怂什么就是干
			# else: # 打不过对面
			# 	self.escape_cnt = 100 # 逃跑计数器
			# 	if self.step((ex+3)%10 + 1, (ey+3)%10 + 1) == 1: # 逃跑
			# 		return
		del tmp

		if self.robot.speedUP==0:
			item_list = ["SPD", "ATK", "HP"]
		else:
		 	item_list = ["ATK", "HP"]
		
		for item_name in item_list:
			tmp = self.find_item(item_name)
			if tmp is None: # 如果找不到就找下一个，找到了又能走过去就继续
				continue
			self.escape_cnt -= 2
			tx, ty = tmp
			if self.step(tx, ty) == 1:
				return
		

		(ex, ey), edir = self.robot.locateEnemy()
		if self.escape_cnt > 0:
			if self.step((ex+5)%10 + 1, (ey+5)%10 + 1) == 1:
				return
		
		# if self.step(5, 5) == 1:
		if self.step(ex, ey) == 1:
			return
		print("nothing to do")
		self.robot.doNothing()
		
		return
		
		
if __name__ == "__main__":
	os.system("python {}".format("tankbattle_debug.py"))
