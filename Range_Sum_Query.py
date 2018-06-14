Range Sum Query
【segment tree】
1. frequently query a range and frequently update the value
2. is a binary tree
3. build: O(2N) time and O(2N) space, query: O(lgN), update: O(lgN)
4. root[0, n] > root.left[0, n / 2], root.right[n / 2 + 1, n]
5. 叶子节点是start == end

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""
# build O(N)
def build(self, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        if start == end:
            return root
        root.left = self.build(start, int((start + end) / 2))
        root.right = self.build(int((start + end) / 2 + 1), end)
        return root


# https://www.lintcode.com/problem/segment-tree-modify/description
# update O(lgN)
def modify(self, root, index, value):
    if index < root.start or index > root.end:
        return
    
    if root.start == root.end:
        root.max = value
        return
    
    self.modify(root.left, index, value)
    self.modify(root.right, index, value)
    
    root.max = max(root.left.max, root.right.max)

# query，容易出错的，其实只要node在范围内，就可以了，多看看
https://www.lintcode.com/problem/segment-tree-query/description

def query(self, root, start, end):
    # write your code here
    if start > root.end or end < root.start:
        return None
    
    if start <= root.start and end >= root.end:
        return root.max
        
    left = self.query(root.left, start, end) # 这里直接把start和end穿进去就可以了
    right = self.query(root.right, start, end)
    
    if left == None:
        return right
    elif right == None:
        return left
    else:
        return max(left, right)
