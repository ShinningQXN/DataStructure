# 【题目】：
# 返回所有factor的combination
# 【算法】：
# dfs，但是写的有点问题。。。想复杂了
# 【细节】：
# 基本上还是dfs的套路，画出路径图，其中有一些需要剪枝，并且要把路径当中的一些可能解放入result里面，非常值得借鉴


class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def factor(n, i, combi, combis):
            while i * i <= n:
                if n % i == 0:
                    combis += [combi + [i, int(n / i)]]
                    factor(int(n / i), i, combi + [i], combis)
                    
                i += 1
            return combis
        return factor(n, 2, [], [])

