# 第三轮 一个第一次当面试官的小哥 来源一亩.三分地论坛. 
# 给一个integer array, 表示每辆车在路上的速度, 假设他们都往同一个方向开, 开的快的会被开的慢的卡住,  问你最后整个路上的车, 会被分成几组 ,每组有几辆车
# follow up, 往这个车队里加一辆车(所有可能的位置), 返回所有可能的下一步的结果

def cluster(nums):
	result = []
	min_val = nums[0]
	min_index = 0
	for i in range(len(nums)):
		if nums[i] < min_val:
			result.append(i - min_index)
			min_val = nums[i]
			min_index = i
	result.append(len(nums) - min_index)
	return result

print cluster([4, 2, 5, 1])
[1,2]
