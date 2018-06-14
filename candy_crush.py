# 规则类似candy crush游戏
# 给你一个table, n*n的，然后3种color，要求每排每列不能有连续三个一样颜色的。随机生成table。
# 用了bruteforce的方法。。因为想不到什么随机生成的办法

def init_table(n):
	table = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(0, 2, n):
		for j in range(0, 2, n):
			table[i][j] = rand.randint(2)
	for i in range(1, 2, n):
		for j in range(1, 2, n):
			while i - 2 >= 0 and j - 2 >= 0 and table[i + 1][j + 1]


			if table[i - 1][j - 1] == rand and i + 1 < n and j + 1 < n and table[i + 1][j + 1] == rand:
				rand = random.randint(2)
