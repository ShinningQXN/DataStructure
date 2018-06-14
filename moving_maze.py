# 第二轮，moving puzzle，3x3的grid，放了随机打乱的1-8个数字，和一个empty，最小步数让它还原成1-8
# 【易错点】：
# 1.string swap，无论python还是java，都需要先变成array再swap，我尝试用了s[:i]+s[j]+s[i+1,j]+s[i]+s[j+1:], 但是这种写法只有i < j才成立
# 2.queue 用popleft， 别忘了popleft
# 3.有可能invalid，所以最后要return-1

def moving_puzzle(board):
	m, n = len(board), len(board[0])

	# get start and end state
	start = ""
	for i in range(m):
		for j in range(n):
			start += board[i][j]
	end = "123450"

	if start == end: return 0

	def swap(s, i, j):
		s = list(s)
		s[i], s[j] = s[j], s[i]
		return "".join(s)

	steps = 0
	dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
	queue = collections.deque([start])
	visited = set([start])

	while queue:
		steps += 1
		size = len(queue)
		for _ in range(size):
			curr = queue.popleft()
			index = curr.index('0')
			x, y = int(index / n), index % n
			for i in range(4):
				xx , yy = x + dx[i], y + dy[i]
				if xx < 0 or yy < 0 or xx >= m or yy >= n: continue
				next_state = swap(curr, index, xx * n + yy)
				if next_state == end:
					return steps
				if next_state not in visited:
					visited.add(next_state)
					queue.append(next_state)

	return -1





