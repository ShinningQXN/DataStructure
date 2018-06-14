# 【描述】
# 一个maze，给定一个初始state，判断用最少步骤变为[[1,2,3],[4,5,0]]的状态

# leetcode 773

# 【解法】：
# BFS

# 【细节】：
# 1.当判断两个object是否相同或者看是否在set里面的时候，一个最好的方法是serilization，就是用string表示state
# 2.上下左右rotate在二维转一维后是 dx = [1,-1,3,-3]来做，但是2，3位置互换是不合法的
# 3.当遇到需要实现的函数时，分开写
# 4.str swap，pyhton和Java一样，需要先变为list，再swap


def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        def swap(s, i, j):
            lst = list(s)
            lst[i], lst[j] = lst[j], lst[i]
            return ''.join(lst)

        n, m, steps = len (board), len(board[0]), 0

        # get begining state
        start = ''
        for i in range (n):
            for j in range (m):
                start += (str (board[i][j]))
        target = '123450'

        # bfs init
        queue = collections.deque ()
        visited = set ()
        queue.append (start)
        visited.add (start)

        dx = [1, -1, 3, -3]
        # bfs
        while len (queue) > 0:
            size = len (queue)
            while size > 0:
                curr = queue.popleft ()
                if curr == target:
                    return steps
                # print curr
                index = curr.index ('0')
                for i in range (len (dx)):
                    new_index = index + dx[i]
                    if new_index < 0 or new_index >= 6 or (index == 2 and new_index == 3) or (index == 3 and new_index == 2):
                        continue
                    new_str = swap (curr, index, new_index)
                    print (new_str)
                    if new_str not in visited:
                        queue.append (new_str)
                        visited.add (new_str)
                size -= 1
            steps += 1
        return -1


print [[1,2,3],[4,5,0]]
print [[1,2,3],[0,4,5]]

