similar_RGB
【题目】：
LeetCode800
【细节】：
1.min关键字：min([], key)
2.lambda关键字
3.hex to decimal: int(x, 16) x is str
  decimal to hex: hex(x), x is int
【面经】
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=334666&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311

class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def get_closest(s):
            return min(['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff'],
                      key = lambda x : abs(int(x, 16) - int(s, 16)))
        
        res = [get_closest(color[i:i+2]) for i in range(1, len(color), 2)]
        return '#' + ''.join(res)