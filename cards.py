一堆卡片从一头拿，可以拿一二三张，两人轮流拿，求最高得分。小哥直接表示有负数的情况。我刚吃了饭有点懵，推出了正数的情况但是卡在了含负数的情况。然后小哥说那就先不考虑负数吧。随后还给了点 hint，然后就写出来了。并且让我在一个例子上过了一遍，问了问用什么 case 来测。

博弈类问题，九章给了几个例题
# https://www.lintcode.com/problem/coins-in-a-line/description
coin in a line I
一堆石头，一次只能拿一两个，拿最后那个石头的人能赢，问第一个拿的人能不能赢？
算法：
1、博弈类问题，需要画出步骤图，一共画三部，我方，对方，我方
2、每一步state用dp来表示, dp[i]表示剩i个石头的时候，第一个拿的人能不能赢。
3、找出状态转移方程 我方与对方的关系dp[i] = dp[i - 1] == false or d[i - 2] == False

细节：
一般n很小的时候需要单独讨论，容易出界，我合并了，i in range(max(n+1, 4))来做

coin in a line II
石头有价值，一次只能从左边拿一个或者两个
state，从第i个拿的时候，拿这个的人比另一个人多拿多少？
def firstWillWin(self, values):
    # write your code here
    n = len(values)
    
    if n == 0:
        return False
    if n == 1:
        return values[0] > 0
        
    dp = [0 for _ in range(n + 1)]
    dp[n] = values[n - 1]
    dp[n - 1] = max(values[n - 1] + values[n - 2], values[n - 2] - values[n - 1])
    
    for i in range(n - 2, 0, -1):
        dp[i] = max(values[i - 1] - dp[i + 1], values[i - 1] + values[i] - dp[i + 2])
        
    return dp[1] > 0

coin in a line III
可以从两头取
实现细节：
1. 需要二维
2. mem来记录， 需要memorial来做了，因为初始状态不好定义， 注意这个时候写递归方程的时候，mem就要用helper来替换了。。。

def firstWillWin(self, values):
    # write your code here
    def helper(values, i, j):
        if mem[i][j] == None:
            if i == j:
                mem[i][j] = values[i]
            else:
                mem[i][j] = max(values[i] - helper(values, i + 1, j), values[j] - helper(values, i, j - 1)) # 容易错，前面把helper写成了mem
        return mem[i][j]
    
    n = len(values)
    
    if n == 0:
        return False
        
    mem = [[None for _ in range(n)] for _ in range(n)]
    helper(values, 0, n - 1)
    return mem[0][n - 1] > 0