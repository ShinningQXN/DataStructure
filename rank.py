# 一面，韩裔小哥：给一个长度为N的数组A，数组每个元素是0到N-1之间的整数，A = j表示数组j号元素的排名在i的前面，且A = -1表示i是第一名。给出数组A，求所有数组元素的完整排名。
# 例如输入A = [2,3,-1,0,1]，输出B = [2,0,3,1,4]。Follow up 1: 你原来的做法用了hashmap（避免下标为-1的情况），能否直接用数组来做？ Follow up 2: 如何不用计算完整排名，推出排名垫底的元素？

# 【算法】：
# 每次需要找下一个值在哪里，有两种方法，一种是hashmap，一种是从后往前

def rank(A):
	x = 0
	for i in range(len(A)):
		x ^= i ^ A[i]

	last = 0 ^ x ^ -1

	result  = []
	while last != -1:
		result.append(last)
		last = A[last]
	return result[::-1]

print(rank([2,3,-1,0,1]))
print(rank([-1]))
