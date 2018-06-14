# # Redundant Connection
# 【题目】：
# 684. Redundant Connection
# give you a list of edges, remove one edge so that these edges can construct a tree


# 【算法】：
# 联通问题，union find，一个node只能被连去main part一次，如果有第二次，就会是多余的

# 【细节】：
# 1.审题，只是给了edges的list，并未给node个数n。首先，如果是树，n = v + 1, 现在多了一个edge，所以len(edges) == n
# 2.root初始化，node number from 1 to n, so it shoud be length of n + 1, from 0 to n

def find_redundant(edges):
	def find(x):
		if roots[x] == x:
			return x
		roots[x] = find(roots[x])
		return roots[x]

	n = len(edges)
	roots = [i for i in range(n + 1)]

	for edge in edges:
		root_1 = find(edge[0])
		root_2 = find(edge[1])
		if root_1 == root_2:
			return edge
		roots[root_1] = root_2

	return None

# 【follow up】:
# if the edge have direction?
# 【算法】
# There are two cases for the tree structure to be invalid.
# 1) A node having two parents;
#    including corner case: e.g. [[4,2],[1,5],[5,2],[5,3],[2,4]]
# 2) A circle exists

# 1) Check whether there is a node having two parents. 
#     If so, store them as candidates A and B, and set the second edge invalid. 
# 2) Perform normal union find. 
#     If the tree is now valid 
#            simply return candidate B
#     else if candidates not existing 
#            we find a circle, return current edge; 
#     else 
#            remove candidate A instead of B.
# 【Corner case】
# 首先一个node不可以有两个parent，但是是不是删除任何一个edge都行呢？
# 或者是和无向图一样的情况
# 难点在于想Corner case, 比如
# 3   	 2  <- 4
#  \>  </
#    1
def find_redundant(edges):
	def find(x):
		if roots[x] == x:
			return x
		roots[x] = find(roots[x])
		return roots[x]

	n = len(edges)
	roots = [i for i in range(n + 1)]

	for edge in edges:
		root_1 = find(edge[0])
		root_2 = find(edge[1])
		if root_1 == root_2:
			return edge
		roots[root_2] = root_1

	return None


