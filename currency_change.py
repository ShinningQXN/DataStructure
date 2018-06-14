# 汇率转换。应该是道面经题，但是我在地里没有找到。给定这样一个list：[[USD, 0.85, EURO], [EURO, 130, Yen]], 求任意两个货币之间的汇率。
# followup是如果想要query常用的几个货币之间的汇率应该怎么做。答曰用cache。
# https://leetcode.com/problems/evaluate-division/description/
# 非常经典,有点难写

【算法】：
老大哥问题，并且需要知道和老大哥之间的关系

【模板】：
def dfs(root, curr):
	if curr in maps:
		return
	maps[curr] = root
	for nei in curr.neighbors:
		dfs(root, nei)

def dfs(root, curr, rate):
	if curr in maps:
		return
	maps[curr] = [root, rate]
	for nei in curr.neighbors:
		dfs(root, nei, rate * nei_rate)

【具体解法】
def change(arr, curr1, curr2):










