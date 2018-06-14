# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=425692&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%255B3046%255D%255Bvalue%255D%3D1%26searchoption%255B3046%255D%255Btype%255D%3Dradio&page=1

# 给一个2d boolean array代表empty seats。每次进来一个query寻找k个连续的empty seats。这k个seats必须是上下左右相邻的，并且seats 是randomly selected。我是keep了一个empty LinkedList，每次random一个index，找到这个index上的empty spot and run dfs，然后 recursively寻找它的上下左右spot。
# 没有思路