# 【题目】：
# 一个矩阵上，一些地方是人，一些地方是bike，找到最近的bike
首先如何定义optimal
NP-hard, 用greedy无法得到最优解
第一个想到是用bfs，但是其实是有点大材小用了，因为距离可以直接的出来，用heap记录每个人到每辆车的距离，然后让人去找车，如果车被占用了，就找下一辆

def find_bike(grid):
	people = []
	bikes = []
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				people.append([i, j])
			elif grid[i][j] == 2:
				bikes.append([i, j])

	for i in range(len(people)):
		for j in range(len(bikes)):
			pq.heappush(pair(i, j, abs(people[i][0] - bikes[j][0]) + abs(people[i][1] - bikes[j][1]) ))

	while pq and len(people_) < len(people) and len(bike_)  < len(bikes):
		curr = pq.heappop()
		if curr 

