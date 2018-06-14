# 这轮面的不好。给一个int数组，return current element 到 next greater element 的距离。比如input 是[2, 1, 4, 700, 5]，return[2, 1, 1, -1, -1]。
# https://leetcode.com/problems/daily-temperatures/description/
# 求右边第一个最大，那么如果是递增栈的话，就一直递增了，所以需要递减栈，当遇到一个比栈顶大的，就while pop比现在这个小的，并且更新对应的

def next_larger(nums):
	result = [-1 for _ in xrange(len(nums))]
	stack = []
	for i in range(len(nums)):
		while len(stack) > 0 and nums[i] > nums[stack[-1]]:
			index = stack.pop()
			result[index] = i - index
		stack.append(i)

print ([1, 2, 4, 7, 5])
