https://leetcode.com/problems/bulls-and-cows/description/
match问题
class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        mem = [0 for _ in range(10)]
        # for s in secret:
        #     mem[int(s)] += 1
        count_a, count_b = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                count_a += 1
                continue
            if mem[int(s)] < 0:
                count_b += 1
            mem[int(s)] += 1
            if mem[int(g)] > 0:
                count_b += 1
            mem[int(g)] -= 1
                           
        return str(count_a) + 'A' + str(count_b) + 'B'

好容易出错。。。