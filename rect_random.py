# given a list of rectangles, write a method to choose a random point uniformly in the list of rectangles （maybe overlapped）
# 第一种是找一个最小的大框 把重叠的 矩形都包含住。然后在大框被 随机选点。如果选的点不被包含在任何一个已有的矩阵里面的话 就再次随机选点 知道选中为止。第二种是对重叠的矩形进行分割
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=426300&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
def get_random()