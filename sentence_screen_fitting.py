# 【题目】：
# 给定行数和列数，能fit多少sentence进去， LeetCode418. Sentence Screen Fitting
# 【算法】：
# 1.暴力解
# 2.类似DP，记录开头为第i个单词的时候，第二行是哪个单词

# 【细节】：
# python3别忘了int（a/b）

# 【解法一】：暴力解
class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        index = 0
        while rows > 0:
            col = cols
            while col - len(sentence[index % len(sentence)]) >= 0:
                col -= len(sentence[index % len(sentence)]) + 1
                index += 1
            rows -= 1
        return int((index) / len(sentence))

# 【解法二】：大化小

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        n = len(sentence)
        dp = [0 for _ in range(n)]
        
        for i in range(n):
            col = cols
            index = i
            while col - len(sentence[index % n]) >= 0:
                col -= len(sentence[index % n]) + 1
                index += 1
            dp[i] = index
        
        count = 0
        index = 0
        while rows > 0:
            post = dp[index]
            count += int(post / n)
            index = post % n
            rows -= 1
        
        return count



