第二面国人小哥，先问了一些简单的数据结构，然后开始做题，
+++++/+++/++/++ 加号代表石头，/代表河，问青蛙能不能从左跳到右，青蛙起始速度0，每次跳到石头上可以adjust speed by 【-1，0， 1】， 比如第一跳速度1，第二跳速度可以是0， 1， 2随便选，我用dp做的，将将写完，肯定很多bug。估计凉凉了。


def fun(s):
	mem = [None for _ in range(len(s))]
	def dfs(pos, speed):
		if pos >= len(s):
			return False
		if mem[pos] != None:
			return mem[pos]
		if pos == len(s):
			return True

		flag = False
		for v in [-1, 0, 1]:
			flag = flag or dfs(pos + speed, speed + i)
		mem[pos] = flag
	return dfs(0, 1)




	