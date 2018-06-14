# 第一轮: 印度大叔 人很好. more info on 1point3acres
# 定义 n-straight 指连续的n个数字, 输入是一个integer array 和n , 要求返回array 满不满足 n-straight 的要求, 即将array划分为x个n-straight
# eg 3-straight  [1,2,3,5,6,7]返回true, [1,2,3,4,5] 返回False. From 1point 3acres bbs
# follow up: 如果n-straight 指至少n个连续的数字, 应该怎么写函数

def n_straight(num, n):
	if num == None or len(num) <= 1:
		return True
	count = 1
	for i in range(1, len(num)):
		if num[i] == num[i - 1] + 1:
			count += 1
			count %= n
		else:
			if count == 0:
				count = 1
			else:
				return False
	return count % n == 0

print n_straight([1,2,3,4,5], 3)

print n_straight([1,2,3,5,6,7], 3)

def n_straight2(num, n):
	if num == None or len(num) <= 1:
		return True
	count = 1
	for i in range(1, len(num)):
		if num[i] == num[i - 1] + 1:
			count += 1
			# count %= n
		else:
			if count >= n:
				count = 1
			else:
				return False
	return count >= n

print n_straight2([1,2,3,4,5], 3)

print n_straight2([1,2,3,5,6,7], 3)
