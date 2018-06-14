# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=425526&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
# 第二题  假设 list是【1，2，3，4，5，1，2，8】 set 是 【2，1，8】 那就是返回true  因为list中有【1，2，8】这个是复合的。  如果set是【5，1，8】那就是false 因为虽然有【5，1，2，8】但不是连续的
def contains(nums, sets):
	sets = set(sets)
	tmp = set()
	count = 0
	for item in nums:
		if item in sets and item not in tmp:
			tmp.add(item)
			count += 1
			if count == len(sets):
				return True
		else:
			count = 0
			tmp = set()
	return False

print contains([5, 1,2,8], [1,2,8])
print contains([5, 1,2,1,8], [1,2,8])
print contains([5,1,2,8], [5,1,8])
